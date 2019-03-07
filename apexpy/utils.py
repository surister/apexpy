from typing import NamedTuple
import os


class Constants(NamedTuple):
    try:
        from dotenv import load_dotenv
        load_dotenv()
        try:
            API_KEY = os.environ['API_KEY']
        except KeyError:
            API_KEY = None
    except ModuleNotFoundError:
        API_KEY = None

    BASE_URL = 'https://public-api.tracker.gg/apex/v1/standard/profile/'


