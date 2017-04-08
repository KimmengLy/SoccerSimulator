# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:59:55 2017

@author: 3415266
"""

from soccersimulator import settings, SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
from sklearn.tree 	import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import pickle
import os.path
from tools import Strats, Action

## Strategie aleatoire
class FonceStrategy(Strategy):
    def __init__(self):
        super(FonceStrategy,self).__init__("Fonce")
    def compute_strategy(self,state,id_team,id_player):
        tools=Strats(state,id_team,id_player)
        return tools.fonce
        
class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()

class Attaquant(Strategy):
    def __init__(self):
        super(Attaquant,self).__init__("Attaquant")
    def compute_strategy (self, state, id_team, id_player):
        tools=Strats(state,id_team,id_player)
        if tools.coups_denvoi:
            return tools.fonce
        return tools.attaque
        
class Defenseur(Strategy):
    def __init__(self):
        super(Defenseur,self).__init__("Defenseur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Strats(state,id_team,id_player)
        return tools.defense

class Passeur(Strategy):
    def __init__(self):
        super(Passeur,self).__init__("Passeur")
    def compute_strategy (self, state, id_team, id_player):
        tools = Action(state,id_team,id_player)
        return tools.passe_coeq

class Solo(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Solo")
    def compute_strategy (self, state, id_team, id_player):
        tools=Strats(state,id_team,id_player)
        if tools.coups_denvoi:
            return tools.fonce
        return tools.solo

#######
## Construction des equipes
#######

team1 = SoccerTeam("team1")
strat_j1 = KeyboardStrategy()
strat_j1.add('f',FonceStrategy())
#strat_j1.add('p',StaticStrategy())
#strat_j1.add('a',Attaquant())
strat_j1.add('d',Defenseur())
strat_j1.add('s',Solo())




team1.add("Jexp 1",strat_j1)
#team1.add("Jexp 2",Attaquant())
team2 = SoccerTeam("team2")
team2.add("Solo", Solo())
#team2.add("rien 2", StaticStrategy())



### Transformation d'un etat en features : state,idt,idp -> R^d
def my_get_features(state,idt,idp):
    """ extraction du vecteur de features d'un etat, ici distance a la balle, distance au but, distance balle but """
    p_pos= state.player_state(idt,idp).position
    f1 = p_pos.distance(state.ball.position)
    f2= p_pos.distance( Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
    f3 = state.ball.position.distance(Vector2D((2-idt)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.))
    return [f1,f2,f3]


def entrainement(fn):
    simu = Simulation(team1,team2)
    show_simu(simu)
    # recuperation de tous les etats
    training_states = strat_j1.states
    # sauvegarde dans un fichier
    dump_jsonz(training_states,fn)

def apprentissage(fn):
    ### chargement d'un fichier sauvegarder
    states_tuple = load_jsonz(fn)
    ## Apprentissage de l'arbre
    data_train, data_labels = build_apprentissage(states_tuple,my_get_features)
    dt = apprend_arbre(data_train,data_labels,depth=10)
    # Visualisation de l'arbre
    affiche_arbre(dt)
    genere_dot(dt,"test2_")
    #sauvegarde d'un arbre 
    pickle.dump(dt,open("tree2.pkl","wb"))
    return dt

def jouer_arbre():
    ####
    # Utilisation de l'arbre
    ###
    #charger un arbre
    dtree = pickle.load(open(os.path.join(os.path.dirname(__file__),"tree2.pkl"),"rb"))
    dic = {"Fonce":FonceStrategy(),"Solo":Solo(),"Attaquant":Attaquant(),"Defenseur":Defenseur(),"Passeur":Passeur()}
    treeStrat1 = DTreeStrategy(dtree,dic,my_get_features)
    #treeStrat2 = DTreeStrategy(dtree,dic,my_get_features)
    team3 = SoccerTeam("Arbre Team")
    team3.add("Joueur 1",treeStrat1)
    #team3.add("Joueur 2",treeStrat2)
    simu = Simulation(team3,team2)
    show_simu(simu)

if __name__=="__main__":
    fn = "test_states.jz"
    #if not os.path.isfile(fn):
    entrainement(fn)
    dt = apprentissage(fn)
    jouer_arbre()