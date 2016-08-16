class AlphaBetaAgent(MultiAgentSearchAgent):


    def getAction(self, state):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        
        self.totalNoMoves=float(gameState.getNumAgents())
        returning=self.Value(gameState,-float("infinity"),+float("infinity"),-1,self.totalNoMoves-1,1)
        return random.choice(returning)
        util.raiseNotDefined()

      
    def Value(self,State,alpha,beta, depthExpanded, Agentnumber ,flag=0):
        depthExpanded+=1
        
        if State.isLose() or State.isWin() or (Agentnumber+1==self.totalNoMoves and (self.depth == float(depthExpanded)/self.totalNoMoves)):
            return self.evaluationFunction(State)
        if Agentnumber+1==self.totalNoMoves:
            return self.Maxvalue(State,alpha,beta,depthExpanded,flag)
        if Agentnumber+1 < self.totalNoMoves:
            return self.Minvalue(State,alpha,beta,depthExpanded,Agentnumber+1)
        util.raiseNotDefined()
    def Maxvalue(self,State,alpha,beta,depthExpanded,flag=0):
        
        v=-float("infinity")
        LegalActions=State.getLegalActions(0)
        if flag ==1:
            Scoredic={}
        for action in LegalActions:
            Successor=State.generateSuccessor(0,action)
            score = self.Value(Successor,alpha,beta,depthExpanded,0)
            v=max(v,score)
            if flag ==1:
                if score not in Scoredic:
                    Scoredic[score]=[]
                Scoredic[score]+=[action]
            if v>beta:
                if flag==0:
                    return v
                else:
                    return Scoredic[max(Scoredic)]
            alpha=max(alpha,v)
        if flag ==1:
            return Scoredic[max(Scoredic)]
        else:
            return v
        
            util.raiseNotDefined()
    def Minvalue(self,State,alpha,beta,depthExpanded,Agentnumber):
            
            v=float("infinity")
            LegalActions=State.getLegalActions(Agentnumber)
            for action in LegalActions:
                Successor=State.generateSuccessor(Agentnumber,action)
                v=min(v,self.Value(Successor,alpha,beta,depthExpanded,Agentnumber))
                if v < alpha:
                    return v
                beta=min(beta,v)

            return v
