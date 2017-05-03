from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerAction, PlayerState
from soccersimulator.utils import Vector2D
from tools import Strats, Action, Item

class Solo(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Strats(state,id_team,id_player)
        if tools.coups_denvoi:
            return tools.fonce
        return tools.solo


class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
    def compute_strategy (self, state, id_team, id_player):
        tools=Strats(state,id_team,id_player)
        if tools.coups_denvoi:
            return tools.fonce
        return tools.attaque
        
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Strats(state,id_team,id_player)
        return tools.defense
        
    
class MVP_Milieu(Strategy):
    def __init__(self):
        Strategy.__init__(self, "MVP_Milieu")
    def compute_strategy (self, state, id_team, id_player):
        tools = Strats(state,id_team,id_player)
        return tools.defmilieu


            
class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Strats(state,id_team,id_player)
        return tools.fonce

        


        
