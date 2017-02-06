from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction, PlayerState
from soccersimulator.gui import show_state,show_simu
from tools import Item, Action
from soccersimulator.utils import Vector2D
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH

## Strategie de test
class TestStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        tools = Action(state,id_team,id_player)
        return tools.aller(tools.ball_position) + tools.shoot_but


class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            return tools.aller(tools.ball_position)+tools.shoot_but
        return SoccerAction(Vector2D(),Vector2D()) 
        

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


class Dribbleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbleur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        if PlayerState.can_shoot :
            return tools.aller(tools.ball_position)+tools.dribble
        return SoccerAction(Vector2D(),Vector2D()) 
        
