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
        
    @property
    def ball_position2(self):
        """renvoi les coordonées x et y de la balle sous la forme d'un couple (x,y)"""
        return self.state.ball.position*5.0
    
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
    
        
    def equipier_pos(self):
        """renvoi la position de l'équipier le plus proche"""
        #float d_min
        #d_min= GAME_WIDTH
        #(id_team,id player) joueur proche   
        
        liste= self.state.players
        for (i,j) in liste:
            """players renvoi la liste des clés (id_team,id_player)"""
            #(id_team,id_player) joueur
            
            
            if((self.key[0]==i) and (self.key[1]!=j)): # and (self.distance_joueur(i,j)<d_min)):
                #d_min=self.distance_joueur(i,j)
                self.key= (i, j)
            return self.my_position()
    
    def distance_balle(self):
        """renvoi la distance  entre 2 joueurs sous la forme d'un nombre flottant"""
        xa=self.my_position().x
        xb=self.state.ball.position.x
        ya=self.my_position().y
        yb=self.ball_position.y
        return (sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)))
        
    def distance(self, p):
        """renvoi la distance  entre 2 joueurs sous la forme d'un nombre flottant"""
        xa=self.my_position().x
        xb=p.x
        ya=self.my_position().y
        yb=p.y
        return (sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)))
        
    def distance_joueur(self, i, j):
        return self.my_position().distance(self.state.player_state(i, j))

    
       
    def Vect_anticipe(self):    
        return self.state.ball.position + self.state.ball.vitesse*10
    
    def test_aller(self, p):
        if (self.distance(p)<10):
            return SoccerAction(p/250-self.my_position()/250,Vector2D())   
        return SoccerAction(p-self.my_position(),Vector2D())
  
class Action(Item): 
    @property
    def shoot_but(self):
        if self.key[0] == 2 :
            return SoccerAction(Vector2D(),Vector2D(0, GAME_HEIGHT/2)-self.state.ball.position)
        return SoccerAction(Vector2D(),Vector2D(GAME_WIDTH, GAME_HEIGHT/2)-self.state.ball.position)
  
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
        
    def ralentir(self, p):
        return SoccerAction(p/50.0 -self.my_position()/50.0,Vector2D())
        

    
    def dribble(self):
        if self.key[0] == 2 :
            return SoccerAction(Vector2D(),Vector2D(-1.5,0))
        return SoccerAction(Vector2D(),Vector2D(1.5,0))
    
    def passe(self):
        return SoccerAction(Vector2D(),self.equipier_pos-self.ball_position)
    
    def shoot_vers(self, p):
        return SoccerAction(Vector2D(), p-self.ball_position)
    

        
    
 



