from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerAction, PlayerState
from soccersimulator.utils import Vector2D
from soccersimulator.settings import GAME_WIDTH
from tools import Strats, Action

class Solo(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        
        if id_team==1 :
            if  tools.ball_position.x>(GAME_WIDTH*3/4.0)-10 :
                if tools.can_shoot :
                    return tools.shoot_angle
            if tools.can_shoot :
                    return tools.dribble
            return tools.aller_vect
        if tools.ball_position.x<(GAME_WIDTH/4.0)+10:
            if tools.can_shoot :
                return tools.shoot_angle
        if tools.can_shoot :
            return tools.dribble
        return tools.aller_vect
        

class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        
        if id_team==1 :
            if state.ball.position.x>GAME_WIDTH/4.0-10 :
                if  tools.distance_shoot :
                    if tools.can_shoot :
                        return tools.shoot_angle
                if tools.can_shoot :
                    return tools.dribble
                return tools.aller_vect
            return tools.aller(tools.position_centre)
        
        if state.ball.position.x<GAME_WIDTH*(3.0/4)+10 :
            if tools.distance_shoot:
                if tools.can_shoot :
                    return tools.shoot_angle
            if tools.can_shoot :
                return tools.dribble
            return tools.aller_vect
        return tools.aller(tools.position_centre)
        
        
class Defenceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if tools.can_shoot :
            return tools.passe
        if id_team == 1:
            if state.ball.position.x<(GAME_WIDTH/4.0)+10 :
                return tools.aller_vect
            return tools.aller(tools.position_defenseur)
        if state.ball.position.x>(GAME_WIDTH*(3.0/4)) :
            return tools.aller_vect
        return tools.aller(tools.position_defenseur) 
    
        
class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if tools.can_shoot :
            return tools.shoot_but
        return tools.aller(tools.ball_position)


class Dribbleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbleur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            return tools.aller(tools.ball_position)+tools.dribble
        return SoccerAction(Vector2D(),Vector2D()) 
        
class Solo_test(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo_test")
    def compute_strategy (self, state, id_team, id_player):
        tools=Strats(state,id_team,id_player)
        if tools.coups_denvoi:
            return tools.fonce
        return tools.solo_test
