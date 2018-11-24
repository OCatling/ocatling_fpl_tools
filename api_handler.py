from pip._vendor import requests
from .api_url import *


class BaseAPI:
    def __init__(self):
        pass

    @staticmethod
    def _get_fpl_fixture_data():
        try:
            fpl_data = requests.get(FPL_DATA).json()
        except requests.exceptions.SSLError:
            fpl_data = requests.get(FPL_DATA, verify=False).json()
        return fpl_data

    @staticmethod
    def _get_player_data(player_id):
        try:
            player_data = requests.get(PLAYER_DATA.format(player_id)).json()
        except requests.exceptions.SSLError:
            player_data = requests.get(PLAYER_DATA.format(player_id), verify=False).json()
        return player_data


class ExtendedAPI:
    def __init__(self):
        pass

    """ 
    parse for self._get_fpl_data() 
    """
    def get_fpl_elements(self, *argv):
        return self._get_fpl_data()['elements']

    def get_fpl_phases(self, *argv):
        return self._get_fpl_data()['phases']

    def get_fpl_events(self, *argv):
        return self._get_fpl_data()['events']
