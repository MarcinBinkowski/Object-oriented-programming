#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class Constants:
    """Class used to store all constats used to create reports"""
    api_key = "RGAPI-5d94c520-e62f-41df-ad45-efeae525d27a"

    urls = {
        "summoner_id": "https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}",
        "league": "https://{}.api.riotgames.com/lol/league/v4/positions/by-summoner/{}?api_key={}",
        "champions": "https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}",
        "mastery": "https://{}.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/{}?api_key={}",
        "opgg": "http://{}.op.gg/summoner/userName={}",
        "icons": "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/{}.png",
    }

    regions = {
        "ru": "ru",
        "kr": "kr",
        "br": "br1",
        "oc": "oc1",
        "jp": "jp1",
        "na": "na1",
        "eune": "eun1",
        "euw": "euw1",
        "tr": "tr1",
        "lan": "la1",
        "las": "la2",
        "pbe": "pbe1"
    }

    all_about_champions_json = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json").json()