#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import Constants
from time import sleep

import requests


class NewUser:

    def __init__(self, summoner, region, api_key=Constants.api_key):
        self.api_key = api_key

        self.summoner = summoner  # summoner name
        self.region = Constants.regions[region]
        self.region_op_gg = region
        self.summoner_info = self.get_summoner_info()
        self.ID = self.summoner_info["id"]
        self.profile_icon_id = self.summoner_info["profileIconId"]
        self.league_info = self.get_summoner_league_info()
        self.champions_info = self.get_summoner_champions_info()
        self.all_masteries = self.get_masteries_info()
        self.lvl = self.summoner_info["summonerLevel"]

    def get_summoner_info(self):
        """ Get summoner info json using his nickname"""
        return requests.get(Constants.urls["summoner_id"].format(
                            self.region, self.summoner, self.api_key)).json()

    def get_summoner_league_info(self):
        """ Get info about summoners league json"""
        return requests.get(Constants.urls["league"].format(
                            self.region, self.ID, self.api_key)).json()

    def get_masteries_info(self):
        """ Get info about all champions masteries json"""
        return requests.get(Constants.urls["mastery"].format(
                            self.region, self.ID, self.api_key)).json()

    def get_summoner_champions_info(self):
        """ Get info about all champions json"""
        return requests.get(Constants.urls["champions"].format(
                            self.region, self.ID, self.api_key)).json()