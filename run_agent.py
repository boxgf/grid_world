from alpha_beta import *

from grid_world import *

if __name__ == '__main__':
	state = State(9,8)
	robots = [(1,1),]
	humans = [(1,5)]
	pellets = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8)]
	obstacles = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8)]
	state.setState(robots,humans,obstacles,pellets)
	
	
	agent = AlphaBetaAgent(3)
	while(True):
		state.display()
		action = agent.getAction(state)
		print action
		state.applyAction(0,action)
		print state.pellets_eaten
	
