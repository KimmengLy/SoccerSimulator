# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:51:09 2017

@author: 3520909
"""
from soccersimulator import SoccerTeam
import mon_golf

def get_golf_team():
    team = SoccerTeam(name="FUT team")
    team.add("TheLegend27",mon_golf.GolfStrategy())
    return team
    
def get_slalom_team1():
    team = SoccerTeam(name="FUT team")
    team.add("TheLegend27",mon_golf.SlalomStrategy())
    return team
    
def get_slalom_team2():
    team = SoccerTeam(name="FUT team")
    team.add("TheLegend27",mon_golf.SlalomStrategy())
    team.add("TheLegend27",mon_golf.SlalomStrategy())
    return team