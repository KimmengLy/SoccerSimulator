from soccersimulator import   SoccerTeam, Strategy
import MesStrategies

def get_team(i):
    team = SoccerTeam(name="TheLegend27")
    if (i==1):
        team.add("TheLegend27",MesStrategies.Solo()) #Strategie Solo
    if (i==2):
        team.add("TheLegend27",MesStrategies.Attaquant()) #Strategie Attaquant
        team.add("O Monstro",MesStrategies.Defenseur()) #Strategie Defenseur
    if (i==4):
        team.add("El Matador",MesStrategies.Defenseur()) #Strategie Attaquant
        team.add("O Monstro",MesStrategies.Solo()) #Strategie Defenseur
        team.add("LeMur",MesStrategies.Attaquant())
        team.add("El Matador",MesStrategies.Attaquant())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
