# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:56:45 2017

@author: 3520909
"""

from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
from tools import Strats
GOLF = 0.001
SLALOM = 10.


class DemoStrategy(Strategy):
    def __init__(self):
        super(DemoStrategy,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return SoccerAction()
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+Vector2D(zone.l,zone.l))
        return SoccerAction()
 
       
class GolfStrategy(Strategy):
    def __init__(self):
        super(GolfStrategy,self).__init__("Golf")
    def compute_strategy(self,state,id_team,id_player):
        tools=Strats(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return tools.solo
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return tools.aller(tools.ball_position)
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+Vector2D(zone.l,zone.l))
        if tools.can_shoot :
            vec_pos = (zone.position+Vector2D(zone.l,zone.l)/(distance)-tools.ball_position)
            return SoccerAction(Vector2D(),Vector2D( angle = vec_pos.angle, norm = vec_pos.norm/15 ))
        return tools.aller(tools.ball_position)

        
class SlalomStrategy(Strategy):
    def __init__(self):
        super(SlalomStrategy,self).__init__("Slalom")
    def compute_strategy(self,state,id_team,id_player):
        tools=Strats(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return tools.solo
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return tools.aller(tools.ball_position)
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+Vector2D(zone.l,zone.l))
        if tools.can_shoot :
            vec_pos = (zone.position+Vector2D(zone.l,zone.l)/distance)-tools.ball_position
            return SoccerAction(Vector2D(),Vector2D( angle = vec_pos.angle, norm = vec_pos.norm/20 ))
        return tools.aller(tools.ball_position)

"""team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",GolfStrategy())
team2.add("JohnSlalom", SlalomStrategy())
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team2,vitesse=SLALOM)
show_simu(simu)
simu = Parcours4(team1=team2,vitesse=SLALOM)
show_simu(simu)"""
