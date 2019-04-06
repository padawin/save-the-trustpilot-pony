import json
import logging
import requests

from exceptions import InvalidMazeDataError, MazeCreationError

logger = logging.getLogger(__name__)


class TrustPilot:
    base_url = "https://ponychallenge.trustpilot.com/pony-challenge/{path}"

    @staticmethod
    def _get_headers():
        return {
            "content-type": "application/json",
            "accept": "application/json"
        }

    @classmethod
    def create_maze(cls, maze_info):
        url = cls.base_url.format(path="maze")
        response = requests.post(
            url,
            headers=cls._get_headers(),
            data=json.dumps(maze_info)
        )
        if response.status_code == 200:
            return response.json()["maze_id"]
        elif response.status_code == 400:
            raise InvalidMazeDataError()
        else:
            raise MazeCreationError(response.status_code)
