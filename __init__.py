from soccersimulator import SoccerTeam
import MesStrategies

def get_team(i):
    team = SoccerTeam(name="TheLegend")
    if (i==1):
        team.add("CR7",MesStrategies.Solo()) 
    if (i==2):
        team.add("Higuain",MesStrategies.Attaquant()) 
        team.add("Evra",MesStrategies.Defenseur()) 
    if (i==4):
        team.add("Puyol",MesStrategies.Defenseur()) 
        team.add("Messi",MesStrategies.Solo()) 
        team.add("Giuly",MesStrategies.MVP_Milieu())
        team.add("Ibrahimovic",MesStrategies.Attaquant())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
get_team(4)
