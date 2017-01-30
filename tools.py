from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH


class MyState(object):
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.key = (id_team,id_player)
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.state.my_position())
    def position_but1(self):
        return Vector2D(0, GAME_HEIGHT/2)
    def position_but2(self):
        return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        
        
    
 



