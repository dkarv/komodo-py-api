import pytest
from komodo_api.lib import KomodoClient, ApiKeyInitOptions
from komodo_api.types import GetVersion, GetVersionResponse

from aioresponses import aioresponses

KEY = "KEY"
SECRET = "SECRET"
VERSION_RESPONSE = """{
    "version": "1.2.3"
}"""

@pytest.mark.asyncio
async def test_client():
    with aioresponses() as mocked:
        mocked.post("http://komodo.mock/read", status=200, body=VERSION_RESPONSE)
        async with KomodoClient("http://komodo.mock", ApiKeyInitOptions(KEY, SECRET)) as api:
            res = await api.read.getVersion(GetVersion())
            assert res == GetVersionResponse(version="1.2.3")
