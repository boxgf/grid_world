from alpha_beta import *

from grid_world import *

if __name__ == '__main__':
	state = State(9,8)
	robots = [(5,5),]
	humans = [(3,3),(2,2)]
	pellets = [(0,0),(2,1),(0,2),(0,3),(0,4)]
	obstacles = [(3,2),]
	state.setState(robots,humans,obstacles,pellets)
	state.display()
	
	agent = AlphaBetaAgent(1)
	agent.getAction(state)
	
