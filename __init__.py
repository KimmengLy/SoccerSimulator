from soccersimulator import   SoccerTeam, Strategy
from MesStrategies import Fonceur, Attaquant, Defenseur

def get_team(i):
    team = SoccerTeam(name="FUT team")
    if (i==1):
        team.add("El Matador",Solo()) #Strategie 1v1
    if (i==2):
        team.add("El Matador",Attaquant()) #Strategie Attaquant
        team.add("O Monstro",Defenseur()) #Strategie Defenseur
    if (i==4):
        team.add("El Matador",Attaquant()) #Strategie Attaquant
        team.add("O Monstro",Defenseur()) #Strategie Defenseur
        team.add("LeMur",Defenseur())
        team.add("El Matador",Attaquant())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
