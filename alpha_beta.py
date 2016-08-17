class AlphaBetaAgent():

    totalNoMoves = None
    max_depth = None
    def __init__(self,depth):
		self.max_depth = depth
		
		
    def getAction(self, state):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        
        self.totalNoMoves=float(state.getNumAgents())
        returning=self.Value(state,-float("infinity"),+float("infinity"), self.totalNoMoves - 1,0)
        return random.choice(returning)
        util.raiseNotDefined()

      
    def Value(self,state,alpha,beta, depthExpanded, Agentnumber):
        print self.max_depth, float(depthExpanded)/self.totalNoMoves, self.max_depth == float(depthExpanded)/self.totalNoMoves, Agentnumber+1 
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
                if flag==0:
                    return v
                else:
                    return Scoredic[max(Scoredic)]
            alpha=max(alpha,v)
       
        else:
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
