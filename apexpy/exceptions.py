
class CustomBaseException(Exception):
    """
    Base exception, exceptions are raised depending on the received code from the api.

    .. code-block:: python

        API_ERROR_MAP = { 401: UnauthorizedError, 400: NotFoundError, 403: UnauthorizedError, 404: PlayerNotFoundError, 500: ServerError}
    """
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class ApiKeyNotProvidedError(CustomBaseException):
    """
    Raised when the api key is not directly provided and doesn't exist in os.environ
    """
    pass


class UnauthorizedError(CustomBaseException):
    pass


class NotFoundError(CustomBaseException):
    pass


class PlayerNotFoundError(CustomBaseException):
    pass


class ServerError(CustomBaseException):
    pass
