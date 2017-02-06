#!/usr/bin/bash
# -*- coding: utf-8 -*
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction, SoccerState
from soccersimulator.gui import show_state,show_simu
from soccersimulator.utils import Vector2D
from soccersimulator.settings import GAME_HEIGHT, GAME_WIDTH
from math import sqrt

class Item(object):
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.key = (id_team,id_player)
    
    @property
    def ball_position(self):
        """renvoi les coordonées x et y de la balle sous la forme d'un couple (x,y)"""
        return self.state.ball.position
    
    def my_position(self):
        """renvoi la position d'un joueur sous la forme d'un couple (x,y)"""
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
        
    @property
    def position_centre(self):
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)
        
    @property
    def position_defenseur(self):
        if self.key[0] == 2 :
            return Vector2D(GAME_WIDTH*(15.0/16),GAME_HEIGHT/2)
        return Vector2D(GAME_WIDTH/16.0,GAME_HEIGHT/2)
    
    def distance(self,joueur2):
        """renvoi la distance  entre 2 joueurs sous la forme d'un nombre flottant"""
        xa=self.my_position().x
        xb=joueur2.my_position().x
        ya=self.my_position().y
        yb=joueur2.my_position().y

        return (sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)))
    
        
    def equipier__proche_pos(self):
        """renvoi la position de l'équipier le plus proche"""
        #float d_min
        d_min= GAME_WIDTH
        #(id_team,id player) joueur proche   
        joueur_proche=(0,0)
        for (i,j) in SoccerState.players():
            """players renvoi la liste des clés (id_team,id_player)"""
            #(id_team,id_player) joueur
            joueur=(i,j)
            if((self.id_team==i) and (self.id_player!=j) and (self.distance(joueur)<d_min)):
                d_min=self.distance(joueur)
                joueur_proche=joueur
        return joueur_proche.my_position()
    

            

            
            
                    
                
    
            
        
  
class Action(Item):
    
    @property
    def shoot_but(self):
        if self.key[0] == 2 :
            return SoccerAction(Vector2D(),Vector2D(0, GAME_HEIGHT/2)-self.state.ball.position)
        return SoccerAction(Vector2D(),Vector2D(GAME_WIDTH, GAME_HEIGHT/2)-self.state.ball.position)
  
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    
    
    def dribble(self):
        if self.key[0] == 2 :
            return SoccerAction(Vector2D(),Vector2D(-1,0))
        return SoccerAction(Vector2D(),Vector2D(1,0))
        
    


        
    
 



