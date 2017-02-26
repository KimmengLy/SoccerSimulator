from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction, PlayerState
from tools import Item, Action
from soccersimulator.utils import Vector2D
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH

class Solo(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        if id_team==1 :
            if  tools.ball_position.x>GAME_WIDTH*3/4.0 :
                return tools.aller(tools.ball_position)+tools.tir_angle()
            if tools.distance_ball() <= 1.65:
                return tools.ralentir(tools.ball_position)+tools.dribble()
        if tools.ball_position.x<(GAME_WIDTH/4.0):
                return tools.aller(tools.ball_position)+tools.tir_angle()
        if tools.distance_ball()<=1.65:
                return tools.ralentir(tools.ball_position)+tools.dribble()
        return tools.aller(tools.ball_position)


class Solo2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        
        if id_team==1 :
            if  tools.ball_position.x>(GAME_WIDTH*3/4.0)-10 :
                if tools.can_shoot :
                    return tools.tir_angle()
            if tools.can_shoot :
                    return tools.dribble()
            return tools.aller_vect()
        if tools.ball_position.x<(GAME_WIDTH/4.0)+10:
            if tools.can_shoot :
                return tools.tir_angle()
        if tools.can_shoot :
            return tools.dribble()
        return tools.aller_vect()
        
        
class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if tools.can_shoot :
            return tools.shoot_but
        return tools.aller(tools.ball_position)
        

class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            if id_team==1 :
                if state.ball.position.x>GAME_WIDTH/4.0 :
                    return tools.aller(tools.ball_position)+tools.shoot_but
                return tools.aller(tools.position_centre)
            if state.ball.position.x<GAME_WIDTH*(3.0/4) : 
                return tools.aller(tools.ball_position)+tools.shoot_but
        return tools.aller(tools.position_centre)
  
      
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            if id_team == 1:
                if state.ball.position.x<(GAME_WIDTH/4.0) :
                    return tools.aller(tools.ball_position)+ tools.shoot_but
                return tools.aller(tools.position_defenseur)
            if state.ball.position.x>(GAME_WIDTH*(3.0/4)) :
                return tools.aller(tools.ball_position)+ tools.shoot_but
            return tools.aller(tools.position_defenseur) 
        return SoccerAction(Vector2D(),Vector2D())
        
class Def2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if tools.can_shoot :
            return tools.shoot_but
        if id_team == 1:
            if state.ball.position.x<(GAME_WIDTH/4.0)+10 :
                return tools.aller_vect()
        
        if state.ball.position.x>(GAME_WIDTH*(3.0/4)) :
            return tools.aller_vect()
        return tools.aller(tools.position_defenseur) 


class Dribbleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbleur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            return tools.aller(tools.ball_position)+tools.dribble
        return SoccerAction(Vector2D(),Vector2D()) 
        

