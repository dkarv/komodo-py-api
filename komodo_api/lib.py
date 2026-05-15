from .responses import (
    ExecuteApi,
    ReadApi,
#    UserApi,
    WriteApi,
)

from .types import (
#    AuthRequest,
    ExecuteRequest,
    ReadRequest,
#    UserRequest,
    WriteRequest,
    WsLoginMessage,
    WsLoginMessageJwt,
    WsLoginMessageApiKeys,
    WsLoginMessageJwtInner,
    WsLoginMessageApiKeysInner,
    UpdateListItem,
    Update,
    GetUpdate,
    UpdateStatus,
    GetVersion,
)

from .exceptions import KomodoException

import aiohttp
import asyncio
import json
from typing import Any, Callable, Dict, Optional, Union, TypeVar
from enum import Enum
from pydantic import TypeAdapter
import logging

_logger = logging.getLogger(__name__)

class InitOptions:
    type_: str


class JwtInitOptions(InitOptions):
    type_: str = "jwt"
    jwt: str

    def __init__(self, jwt: str):
        self.jwt = jwt


class ApiKeyInitOptions(InitOptions):
    type_: str = "api-key"
    key: str
    secret: str

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret


class CancelToken:
    def __init__(self):
        self.cancelled = False

    def cancel(self):
        self.cancelled = True


class KomodoClient:
#    auth: AuthApi
    read: ReadApi
    write: WriteApi
#    user: UserApi
    execute: ExecuteApi
    url: str
    _session: aiohttp.ClientSession
    _ws_login: WsLoginMessage

    def __init__(self, url: str, options: InitOptions):
        self.url = url if url.endswith("/") else url + "/"
        headers = {
            "content-type": "application/json",
        }
        if options.type_ == "jwt":
            headers["authorization"] = options.jwt
            self._ws_login = WsLoginMessageJwt(params=WsLoginMessageJwtInner(jwt = options.jwt))
        elif options.type_ == "api-key":
            headers["x-api-key"] = options.key
            headers["x-api-secret"] = options.secret
            self._ws_login = WsLoginMessageApiKeys(params=WsLoginMessageApiKeysInner(key = options.key, secret = options.secret))
        else:
            raise ValueError(f"Unknown InitOptions type: {options.type_}")
        
        self._session = aiohttp.ClientSession(headers=headers)

#        self.auth = AuthApi(self.request)
        self.read = ReadApi(self.request)
        self.write = WriteApi(self.request)
#        self.user = UserApi(self.request)
        self.execute = ExecuteApi(self.request)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *err):
        await self.close()

    async def close(self):
        await self._session.close()

    Req = TypeVar("Req")
    Res = TypeVar("Res")

    async def request(self, path: str, request: Req, clz: type[Res]) -> Res:
        async with self._session.post(
            f"{self.url}{path}",
            data=request.model_dump_json(exclude_none=True),
        ) as response:
            if response.status == 200:
                text = await response.text()
                _logger.debug(f"Response: {text}")
                try:
                    return TypeAdapter(clz).validate_json(text)
                except Exception as e:
                    raise Exception(
                        f"Failed to parse response: {e}\nResponse text: {text}"
                    )
            else:
                error = await response.json()
                _logger.warning(f"Api error {error}")
                raise KomodoException(error, response.status)

    async def poll_update_until_complete(self, update: Update, sleep_seconds: int = 1) -> Update:
        while not update.status == UpdateStatus.COMPLETE:
            await asyncio.sleep(sleep_seconds)
            update = await self.read.getUpdate(GetUpdate(id = update.id.oid))
        return update

    async def core_version(self) -> str:
        res = await self.read.getVersion(GetVersion())
        return res.version

    async def get_update_websocket(
        self,
        on_update: Callable[[UpdateListItem], None],
        on_login: Optional[Callable] = None,
        on_open: Optional[Callable] = None,
        on_close: Optional[Callable] = None,
    ):
        async with self._session.ws_connect(
            self.url.replace("http", "ws") + "ws/update"
        ) as ws:
            if on_open:
                on_open()
            await ws.send_str(self._ws_login.model_dump_json(exclude_none=True))
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == "LOGGED_IN":
                        if on_login:
                            on_login()
                    else:
                        data = TypeAdapter(UpdateListItem).validate_json(msg.data)
                        on_update(data)
                if msg.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
                    break
            if on_close:
                on_close()

    async def subscribe_to_update_websocket(
        self,
        on_update: Callable[[UpdateListItem], None],
        on_login: Optional[Callable] = None,
        on_open: Optional[Callable] = None,
        on_close: Optional[Callable] = None,
        retry: bool = True,
        retry_timeout_ms: int = 5000,
        cancel: CancelToken = CancelToken(),
        on_cancel: Optional[Callable] = None,
    ):
        while not cancel.cancelled:
            try:
                await self.get_update_websocket(on_update, on_login, on_open, on_close)
            except Exception as e:
                print(f"WebSocket error: {e}")
                if retry:
                    await asyncio.sleep(retry_timeout_ms / 1000)
                else:
                    break
        if cancel.cancelled and on_cancel:
            on_cancel()