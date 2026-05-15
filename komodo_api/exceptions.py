class KomodoException(Exception):
    """Error in api call."""

    error: str
    """Top level error message."""

    trace: list[str]
    """Traces."""

    code: int
    """status code of response."""

    def __init__(self, json: dict, code: int):
        self.error = json["error"]
        self.trace = json["trace"]
        self.code = code
