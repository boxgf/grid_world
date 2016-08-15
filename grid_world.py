import numpy
import copy

class GridWorld:
	length = None
	breadth = None
	grid = None
	def __init__(self,l,b):
		self.length = l
		self.breadth = b
		self.grid = [['.' for i in xrange(self.length)] for j in xrange(self.breadth)]

class State:
	env = None
	bots = {}
	humans = {}
	pellets = []
	obstacles = []
	
	def __init__(self,l,b):
		self.env = GridWorld(l,b)
	def setState(self,robots,humans,obstacles,pellets):
		for i in xrange(len(robots)):
			self.bots['robot' + str(i)] = robots[i]
			
			self.env.grid[robots[i][0]][robots[i][1]] = 'b'
		for i in xrange(len(humans)):
			self.humans['human' + str(i)] = humans[i]
			self.env.grid[humans[i][0]][humans[i][1]] = 'h'
		self.obstacles	= obstacles	
		
		for i in obstacles:
			self.env.grid[i[0]][i[1]] = 'o'
		
		self.pellets = pellets
		
		for i in obstacles:
			self.env.grid[i[0]][i[1]] = 'p'
		
	def isValidPose(self, pose):
		return self.env.grid[pose[0]][pose[1]] == '' or self.env.grid[pose[0]][pose[1]] == 'p' 
	def isValidRobotPose(self, pose):
		return self.env.grid[pose[0]][pose[1]] != 'o' and self.env.grid[pose[0]][pose[1]] != 'h' and pose[0] < self.env.grid.length and pose[0] >= 0 and pose[1] < self.env.grid.breadth and pose[1] >= 0
	def isValidHumanPose(self,pose):
		s = 1
	def getRobotSuccessor(self, robot_index):
		s = 1
	def getSuccessors(self, agent_index):
		successors = []
		if agent_index < len(bots):	
			agent_pose = bots[agent_index]
			agent_char = 'b'
		else:
			agent_pose = humans[agent_index - len(bots) -1]
			agent_char = 'h'
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				if i == j == 0: continue
				if isValidPose(agent_pose[0]+i,agent_pose[0]+j):
					new_state = copy.deepcopy(self)
					if agent_char == 'h' and new_state[agent_pose[0]][agent_pose[1]] == 'f':
						new_state[agent_pose[0]][agent_pose[1]] = 'p'
					else:
						new_state[agent_pose[0]][agent_pose[1]] = '.'
						
					new_state[agent_pose[0]+i][agent_pose[1]+j] = agent_char
					
					successors.append(new_state)
					
				
	def display(self):
		for i in  self.env.grid:
			print i
		
		
if __name__ == '__main__':
	state = State(10,10)
	robots = [(5,5),]
	humans = [(3,3),(2,2)]
	pellets = [(0,0),(0,1),(0,2),(0,3),(0,4)]
	obstacles = [(9,9),]
	state.display()
	
	
	print state.env
