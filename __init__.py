from soccersimulator import   SoccerTeam, Strategy
import MesStrategies

def get_team(i):
    team = SoccerTeam(name="FUT team")
    if (i==1):
        team.add("El Matador",MesStrategies.Solo_test()) #Strategie Solo
    if (i==2):
        team.add("El Matador",MesStrategies.Attaquant()) #Strategie Attaquant
        team.add("O Monstro",MesStrategies.Defenceur()) #Strategie Defenseur
    if (i==4):
        team.add("El Matador",MesStrategies.Defenceur()) #Strategie Attaquant
        team.add("O Monstro",MesStrategies.Defenceur()) #Strategie Defenseur
        team.add("LeMur",MesStrategies.Attaquant())
        team.add("El Matador",MesStrategies.Attaquant())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
