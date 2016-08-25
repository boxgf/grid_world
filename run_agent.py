from alpha_beta import *
import random
from grid_world import *

if __name__ == '__main__':
	state = State(9,8)
	robots = [(1,2),]
	humans = [(2,1)]
	pellets = [(1,1),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)]#,(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8)
	obstacles = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8)]
	state.setState(robots,humans,obstacles,pellets)
	

	state.setState(robots,humans,obstacles,pellets)	
	agent = AlphaBetaAgent(3)
	state.display()

	while(not state.win_status and not state.lose_status):
		action = agent.getAction(state)
		print action
		state.applyAction(0,action)
		state.applyAction(1,random.choice(state.getLegalActions(1)))
		state.display()
		print 'pellets_eaten', state.pellets_eaten , 'Is win', state.win_status, 'Is Lose', state.lose_status, agent.evaluationFunction(state)
	
