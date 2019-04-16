import json
import logging
import requests

from exceptions import InvalidMazeDataError, MazeCreationError

logger = logging.getLogger(__name__)


class TrustPilot:
    """
    Interface to TrustPilot's API.
    """

    base_url = "https://ponychallenge.trustpilot.com/pony-challenge/{path}"

    @staticmethod
    def _get_headers():
        return {
            "content-type": "application/json",
            "accept": "application/json"
        }

    @classmethod
    def create_maze(cls, maze_info):
        """
        Create a labyrinth.

        :raises: `InvalidMazeDataError` if the data provided are invalid.
        :raises: `MazeCreationError` if an unexpected error occured.
        """
        url = cls.base_url.format(path="maze")
        response = requests.post(
            url,
            headers=cls._get_headers(),
            data=json.dumps(maze_info)
        )
        if response.status_code == 200:
            return response.json()["maze_id"]
        elif response.status_code == 400:
            raise InvalidMazeDataError(response.text)
        else:
            raise MazeCreationError(response.status_code)

    @classmethod
    def get_maze(cls, maze_id):
        """
        Get a labyrinth based on an ID.

        :param maze_id: `str`; The labyrinth's ID
        :raises: `InvalidMazeDataError` if the ID is invalid
        :return: the labyrinth's content
        """
        url = cls.base_url.format(path=f"maze/{maze_id}")
        response = requests.get(url, headers=cls._get_headers())
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise InvalidMazeDataError()

    @classmethod
    def move(cls, maze_id, direction):
        """
        Make the pony move in the labyrinth in the given direction.

        :return: `str` the result of the move.
        """
        url = cls.base_url.format(path=f"maze/{maze_id}")
        response = requests.post(
            url,
            headers=cls._get_headers(),
            data=json.dumps({"direction": direction})
        )
        if response.status_code == 200:
            data = response.json()
            try:
                return data["state-result"]
            except KeyError:
                return data.get("state")
        elif response.status_code == 400:
            return "Invalid direction"
        else:
            return "Unknown error"
