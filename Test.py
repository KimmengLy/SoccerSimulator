from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import show_simu
from tools import Item, Action
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH
from MesStrategies import *
from mon_arbre import *
from arbres_utils import DTreeStrategy
import pickle
import os


            
## Strategie de test

class Testcoeq(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Testcoeq")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        return tools.aller_vect+tools.passe

class DefTest(Strategy):
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
    
class Immobile(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Immobile")
    def compute_strategy (self, state, id_team, id_player):
        tools=Action(state,id_team,id_player)
        return tools.immobile
        

                 
        
    


if __name__ == "__main__":
    dtree = pickle.load(open(os.path.join(os.path.dirname(__file__),"tree.pkl"),"rb"))
    dic = {"Fonce":FonceStrategy(),"Static":StaticStrategy(),"Solo":Solo(),"Attaquant":Attaquant(),"Defenseur":Defenseur(), "Passeur":Passeur()}
    treeStrat = DTreeStrategy(dtree,dic,my_get_features)
    
    team1 = SoccerTeam(name="team1")
    team2 = SoccerTeam(name="team2")
    
    team1.add("El Matador",treeStrat) #Strategie Fonceur
    team2.add("Solo",Solo())
    #team1.add("ujfgj",MesStrategies.Attaquant()) #Strategie Attaquant
    #team1.add("messi",MesStrategies.Defenceur())
    #Creation d'une partie
    simu = Simulation(team1, team2)
    #Jouer et afficher la partie
    show_simu(simu)

