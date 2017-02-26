from soccersimulator import   SoccerTeam, Strategy
from MesStrategies import Solo2, Attaquant, Def2, Attaquant2

def get_team(i):
    team = SoccerTeam(name="Legendary")
    if (i==1):
        team.add("El Matador",Solo2()) #Strategie Solo
    if (i==2):
        team.add("El Matador",Attaquant2()) #Strategie Attaquant
        team.add("O Monstro",Def2()) #Strategie Defenseur
    if (i==4):
        team.add("El Matador",Attaquant2()) #Strategie Attaquant
        team.add("O Monstro",Def2()) #Strategie Defenseur
        team.add("LeMur",Def2())
        team.add("El Matador",Attaquant2())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
