#!/usr/bin/env python
# -*- coding: utf-8 -*-
from loldata import NewUser

def modify_masteries_data(summoner):
    """
    This function takes summoner object, returns
    list of three tuples consisting three top played champions (champion id, total points)
     and list containing tuple of least played champion id and points(champion id, total points)
    """
    masteries_list = []  # declaring list

    for i in range(len(summoner.champions_info)):  # for each champion in champions_info json
        champion_id = summoner.champions_info[i]["championId"]  # get champion Id
        champion_points = summoner.champions_info[i]["championPoints"]  # get champion points
        masteries_list.append((champion_id, champion_points))  # add tuple to masteries_list

    masteries_list.sort(key=lambda item: (item[1], item[0]), reverse=True)  # sort list with using second argument(points)
    five_most_played_champions = masteries_list[:5]  # get five most played champions from list
    least_played_champion = masteries_list[-1:]   # get last element from list (least played champion)
    return five_most_played_champions, least_played_champion  # return tuple


def get_all_champs_score(summoner):
    """
    This function returnes summed up points of all champions
    """
    answer = 0

    for i in range(len(summoner.champions_info)):  # for each champion in champions_info json
        champion_points = summoner.champions_info[i]["championPoints"]  # get champion points
        answer += int(champion_points)
    return answer

def top_three_champions_who_can_earn_chests(summoner):
    """
    This function takes summoner object and returns 3 most played champions summoner didn't get chest with yet
    """
    chests = []  # declaring list
    for i in range(len(summoner.champions_info)):  # for champion in list
        champion_id = summoner.champions_info[i]["championId"]  # get champion id
        champion_points = summoner.champions_info[i]["championPoints"]  # get champion points
        chest_available = summoner.champions_info[i]["chestGranted"]  # info about chest availability
        chests.append((champion_id, champion_points, chest_available))  # add tuple to list

    chests.sort(key=lambda item: (item[1], item[0], item[2]), reverse=True)  # sorts list by champion points
    chests = [x for x in chests if x[2] is False][:3]  # selects all champs who can earn chests and picks 3 most played
    return chests  # returns list

def win_rate(summoner):
    """
    This function takes summoner object and returns (wins, losses, winratio) tuples for both 5v5 queues
    """
    to_return = []
    try:
        number_of_wins_solo_duo = summoner.league_info[0]["wins"]  # solo_duo wins
        number_of_losses_solo_duo = summoner.league_info[0]["losses"]  # solo_duo losses
        win_rate_solo_duo = number_of_wins_solo_duo / (number_of_wins_solo_duo + number_of_losses_solo_duo)  # solo_duo winratio
        to_return = [(number_of_wins_solo_duo, number_of_losses_solo_duo, round(win_rate_solo_duo, 2))]
    except:
        pass
    try:
        number_of_wins_flex = summoner.league_info[1]["wins"]  # flex wins
        number_of_losses_flex = summoner.league_info[1]["losses"]  # flex losses
        win_rate_flex = number_of_wins_flex / (number_of_wins_flex + number_of_losses_flex)  # flex winratio
        to_return.append((number_of_wins_flex, number_of_losses_flex, round(win_rate_flex, 2)))
    except:
        pass
    return to_return

def get_leagues(summoner):
    league_info = summoner.league_info
    try:
        solo_duo_league = (league_info[0]["tier"], league_info[0]["rank"])
    except:
        solo_duo_league = "p"
    try:
        flex_league = (league_info[1]["tier"], league_info[1]["rank"])
    except:
        flex_league = "p"
    return solo_duo_league, flex_league


if __name__ == "__main__":
    my_summoner = NewUser("binq661", "eune")
    modify_masteries_data(my_summoner)
    top_three_champions_who_can_earn_chests(my_summoner)
    get_all_champs_score(my_summoner)

