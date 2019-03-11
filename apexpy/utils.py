from os import environ
from typing import NamedTuple

from apexpy.exceptions import NotFoundError, PlayerNotFoundError, ServerError, UnauthorizedError


class Constants(NamedTuple):
    try:
        from dotenv import load_dotenv
        load_dotenv()

    except ModuleNotFoundError:
        pass

    try:
        API_KEY = environ['APEX_KEY']
    except KeyError:
        API_KEY = None

    BASE_URL = 'https://public-api.tracker.gg/apex/v1/standard/profile/'

    API_OK = 200

    API_ERROR_MAP = {

        401: UnauthorizedError,
        400: NotFoundError,
        403: UnauthorizedError,
        404: PlayerNotFoundError,
        500: ServerError,
    }

    PLATFORM_MAP = {
        'pc': 5,
        'xbox': 1,
        'psn': 2
    }
