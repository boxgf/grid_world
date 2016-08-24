import util
class AlphaBetaAgent():

    totalNoMoves = None
    max_depth = None
    def __init__(self,depth):
		self.max_depth = depth
    def evaluationFunction(self, state):
		min_human_dist = min_pellet_dist = min_obstacle_dist = float('inf')
		for bot in state.bots:
			for human in state.humans:
				if min_human_dist > util.squaredEucledian(state.humans[human],state.bots[bot]):
					min_human_dist = util.squaredEucledian(state.humans[human],state.bots[bot])
			for pellet in state.pellets:
				if min_pellet_dist > util.squaredEucledian(pellet,state.bots[bot]):
					min_pellet_dist = util.squaredEucledian(pellet,state.bots[bot])
			for obstacle in state.obstacles:
				if min_obstacle_dist > util.squaredEucledian(obstacle,state.bots[bot]):
					min_obstacle_dist = util.squaredEucledian(obstacle,state.bots[bot])
		return 1.0/min_human_dist + min_pellet_dist + 1.0/min_obstacle_dist		
    
    def getAction(self, state):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        
        self.totalNoMoves=float(state.getNumAgents())
        returning=self.Value(state,-float("infinity"),+float("infinity"),0, self.totalNoMoves - 1)
        return random.choice(returning)

      
    def Value(self,state,alpha,beta, depthExpanded, Agentnumber):
        print 'max_depth =',self.max_depth,'depth_expanded =',depthExpanded,'depth/totalmoves =', float(depthExpanded)/self.totalNoMoves,'max_depth == prev frac', self.max_depth == float(depthExpanded)/self.totalNoMoves, Agentnumber+1 
        if  (Agentnumber+1 == self.totalNoMoves and (self.max_depth == float(depthExpanded)/self.totalNoMoves)):
            return self.evaluationFunction(state)
        if Agentnumber+1==self.totalNoMoves:
            return self.Maxvalue(state,alpha,beta,depthExpanded + 1)
        if Agentnumber+1 < self.totalNoMoves:
            return self.Minvalue(state,alpha,beta,depthExpanded + 1,Agentnumber + 1)
        
    def Maxvalue(self,state,alpha,beta,depthExpanded):
        
        v = -float("infinity")
        LegalActions=state.getLegalActions(0)
        
        for action in LegalActions:
            Successor=state.getActionSuccessor(0,action)
            score = self.Value(Successor,alpha,beta,depthExpanded,0)
            v=max(v,score)
            if v>beta:
                return v
            alpha=max(alpha,v)
        return v
        
            
    def Minvalue(self,state,alpha,beta,depthExpanded,Agentnumber):
            
            v = float("infinity")
            LegalActions=state.getLegalActions(Agentnumber)
            for action in LegalActions:
                Successor=state.getActionSuccessor(Agentnumber,action)
                v=min(v,self.Value(Successor,alpha,beta,depthExpanded,Agentnumber))
                if v < alpha:
                    return v
                beta=min(beta,v)

            return v
