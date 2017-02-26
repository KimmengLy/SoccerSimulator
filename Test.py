from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import show_simu
from tools import Item, Action
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH
import MesStrategies
            
## Strategie de test

class Testcoeq(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Testcoeq")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        tool = Item(state,id_team,id_player)
        return tools.aller(tool.equipier_pos()) # tools.shoot_vers(Item(state,id_team,id_player).equipier_pos())

class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        return tools.aller(tools.ball_position)+tools.shoot_but
      
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        tool = Item(state,id_team,id_player)
        if id_team == 1:
            if state.ball.position.x<(GAME_WIDTH/4.0) :
                #if tool.distance(tool.Vect_anticipe()) <= 0.5:
                    #return tools.ralentir(tool.Vect_anticipe())+tools.shoot_but
                return tools.aller(tools.ball_position)+tools.shoot_but#tools.shoot_but#+tools.shoot_vers(Item(state,id_team,id_player).equipier_pos())
            return tools.aller(tools.position_defenseur)
        if state.ball.position.x>(GAME_WIDTH*(3.0/4)) :
            return tools.aller(tool.Vect_anticipe())+tools.shoot_but
        return tools.aller(tools.position_defenseur) 


class DefTest(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        tool = Item(state,id_team,id_player)
        if id_team == 1:
            if tools.distance_balle() <= 1.65:
                return tools.aller_vect_ralenti()+tools.shoot_but
            if state.ball.position.x<(GAME_WIDTH/4.0)+10 :
                return tools.aller_vect()+tools.shoot_but
        return tools.aller(tool.position_defenseur)
        

class Immobile(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Immobile")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        return tools.immobile()


if __name__ == "__main__":
    team1 = SoccerTeam(name="team1")
    team2 = SoccerTeam(name="team2")
    #team1.add("El Matador",Test()) #Strategie Fonceur
    #team1.add("Omonstro",Testcoeq()) #Strategie Attaquant
    team2.add("messi",DefTest()) #Strategie Defenseu
    
    team1.add("ujfgj",MesStrategies.Solo()) #Strategie Attaquant
    #team2.add("messi2",Attaquant())
    #Creation d'une partie
    simu = Simulation(team1, team2)
    #Jouer et afficher la partie
    show_simu(simu)

