import util
import random
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
		if min_human_dist == float('inf') : min_human_dist = 0
		if min_pellet_dist == float('inf'): min_pellet_dist = 0
		if min_obstacle_dist == float('inf'): min_obstacle_dist = 0 
		return .1 * min_human_dist - .3 * min_pellet_dist + 0.05 * min_obstacle_dist	 + 100 * state.pellets_eaten + 500 * state.win_status - 5000 * state.lose_status;	
    
    def getAction(self, state):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        
        self.totalNoMoves=float(state.getNumAgents())
        return self.Value(state,-float("infinity"),+float("infinity"),0, self.totalNoMoves - 1)

      
    def Value(self,state,alpha,beta, depthExpanded, Agentnumber):
        if  (Agentnumber+1 == self.totalNoMoves and (self.max_depth == float(depthExpanded)/self.totalNoMoves)):
            return self.evaluationFunction(state)
        if Agentnumber+1==self.totalNoMoves:
            return self.Maxvalue(state,alpha,beta,depthExpanded + 1)
        if Agentnumber+1 < self.totalNoMoves:
            return self.Minvalue(state,alpha,beta,depthExpanded + 1,Agentnumber + 1)
        
    def Maxvalue(self,state,alpha,beta,depthExpanded):
        if(depthExpanded == 1 ):
			best_action = {}
        v = -float("infinity")
        LegalActions=state.getLegalActions(0)
        
        for action in LegalActions:
            Successor=state.getActionSuccessor(0,action)
            #Successor.display()
            #self.evaluationFunction(Successor)
            score = self.Value(Successor,alpha,beta,depthExpanded,0)
            if(depthExpanded == 1 ):
				if score not in best_action : best_action[score] = []
				best_action[score].append(action)
            v=max(v,score)
            if v>beta:
                return v
            alpha=max(alpha,v)
        if(depthExpanded == 1):
			depth_0_best_action = {}
			for action in best_action[max(best_action)]:
				Successor=state.getActionSuccessor(0,action)
				score = self.Value(Successor,alpha,beta,depthExpanded,0)
				if score not in depth_0_best_action: depth_0_best_action[score] = []
				depth_0_best_action[score].append(action)
			return random.choice(depth_0_best_action[max(depth_0_best_action)])
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
