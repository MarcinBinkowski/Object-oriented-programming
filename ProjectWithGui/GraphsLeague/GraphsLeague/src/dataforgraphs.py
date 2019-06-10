#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import Constants
from datamodifier import DataModifier   

from loldata import NewUser


class GraphData:
    """
    This class is used for generating objects which keep all data needed for generating charts for summoner
    """
    def __init__(self, summoner):
        self.summoner = summoner
        self.dataModifier = DataModifier(summoner)
        self.masteries = self.dataModifier.modify_masteries_data()
        self.best_scores = [x[1] for x in self.masteries[0]]
        self.best_ids = [x[0] for x in self.masteries[0]]
        self.best_names = self.get_champions_names(self.best_ids)

        self.best_with_chests = self.dataModifier.top_three_champions_who_can_earn_chests()
        self.best_with_chests_ids = [x[0] for x in self.best_with_chests]
        self.best_with_chests_names = self.get_champions_names(self.best_with_chests_ids)


        self.all_champions_score = self.dataModifier.get_all_champs_score()
        self.all_champions_score_modified = [self.all_champions_score - sum(self.best_scores)]

        self.donut_chart_data_scores = self.all_champions_score_modified + self.best_scores[::-1]
        self.donut_chart_data_names = ["Rest"] + self.best_names[::-1]


        self.win_data = self.dataModifier.win_rate()

    def get_champion_name(self, id_number):
        """
        This method returnes name of champion with given id
        """
        for name in Constants.all_about_champions_json["data"]:
            if Constants.all_about_champions_json["data"][name]["key"] == id_number:
                return name

    def get_champions_names(self, ids_list):
        """
        This method returnes list containing names of champions with given ids from list
        """
        temp = []
        for i in ids_list:
            temp.append(self.get_champion_name(str(i)))
        return temp




if __name__ == "__main__":
    graph_data = GraphData(NewUser("binq661", "eune"))

