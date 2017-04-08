class SoccerState(object):
    """ Etat d'un tour du jeu. Contient la balle, l'ensemble des etats des joueurs, le score et
    le numero de l'etat.
    """
    def __init__(self,states=None,ball=None,**kwargs):
        self.states = states or dict()
        self.ball = ball or Ball()
        self.strategies = kwargs.pop('strategies',dict())
        self.score = kwargs.pop('score', {1: 0, 2: 0})
        self.step = kwargs.pop('step', 0)
        self.max_steps = kwargs.pop('max_steps', settings.MAX_GAME_STEPS)
        self.goal = kwargs.pop('goal', 0)
        self.__dict__.update(kwargs)

    def __str__(self):
        return ("Step: %d, %s " %(self.step,str(self.ball)))+\
               " ".join("(%d,%d):%s" %(k[0],k[1],str(p)) for k,p in sorted(self.states.items()))+\
               (" score : %d-%d" %(self.score_team1,self.score_team2))
    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return dict(states=dict_to_json(self.states),
                strategies=dict_to_json( self.strategies),
                ball=self.ball,score=dict_to_json(self.score),step=self.step,
                max_steps=self.max_steps,goal=self.goal)
    def player_state(self, id_team, id_player):
        """ renvoie la configuration du joueur
        :param id_team: numero de la team du joueur
        :param id_player: numero du joueur
        :return:
        """
        return self.states[(id_team, id_player)]

    @property
    def players(self):
        """ renvoie la liste des cles des joueurs (idteam,idplayer)
        :return: liste des cles
        """
        return sorted(self.states.keys())

    def nb_players(self, team):
        """ nombre de joueurs de la team team
        :param team: 1 ou 2
        :return:
        """
        return len([x for x in self.states.keys() if x[0] == team])

    def get_score_team(self, idx):
        """ score de la team idx : 1 ou 2
        :param idx: numero de la team
        :return:
        """
        return self.score[idx]
