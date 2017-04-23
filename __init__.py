from soccersimulator import SoccerTeam
import MesStrategies
from arbres import my_get_features
from arbres_utils import DTreeStrategy


def get_team(i):
    dtree = pickle.load(open(os.path.join(os.path.dirname(__file__),"tree.pkl"),"rb"))
    dic = {"Fonce":FonceStrategy(),"Static":StaticStrategy(),"Solo":Solo(),"Attaquant":Attaquant(),"Defenseur":Defenseur(), "Passeur":Passeur()}
    treeStrat = DTreeStrategy(dtree,dic,my_get_features)
    team = SoccerTeam(name="FUT team")
    if (i==1):
        team.add("TheLegend27",MesStrategies.Solo()) 
    if (i==2):
        team.add("TheLegend27",MesStrategies.Attaquant()) 
        team.add("O Monstro",MesStrategies.Defenseur()) 
    if (i==4):
        team.add("El Matador",MesStrategies.Defenseur()) 
        team.add("O Monstro",MesStrategies.Solo()) 
        team.add("LeMur",MesStrategies.MVP_Milieu())
        team.add("El Matador",MesStrategies.Attaquant())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
get_team(4)
