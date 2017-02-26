from soccersimulator import   SoccerTeam, Strategy
from MesStrategies import Solo2, Attaquant, Def2, Attaquant2

def get_team(i):
    team = SoccerTeam(name="Legendary")
    if (i==1):
        team.add("Eto'o",Solo2()) #Strategie Solo
    if (i==2):
        team.add("Messi",Attaquant2()) #Strategie Attaquant
        team.add("Puyol",Def2()) #Strategie Defenseur
    if (i==4):
        team.add("Drogba",Attaquant2()) #Strategie Attaquant
        team.add("Boateng",Def2()) #Strategie Defenseur
        team.add("Evra",Def2())
        team.add("Lampard",Attaquant2())
    return team 
            

## Creation d'une equipe
get_team(1)
get_team(2)
