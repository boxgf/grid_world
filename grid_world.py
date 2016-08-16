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
		
		for i in pellets:
			self.env.grid[i[0]][i[1]] = 'p'
		
	def isValidPose(self, pose):
		return self.env.grid[pose[0]][pose[1]] == '.' or self.env.grid[pose[0]][pose[1]] == 'p' 
	def isValidRobotPose(self, pose):
		return self.env.grid[pose[0]][pose[1]] != 'o' and self.env.grid[pose[0]][pose[1]] != 'h' and pose[0] < self.env.grid.length and pose[0] >= 0 and pose[1] < self.env.grid.breadth and pose[1] >= 0
	def isValidHumanPose(self,pose):
		s = 1
	def getRobotSuccessor(self, robot_index):
		s = 1
	def copy(self):
		copy_state = copy.deepcopy(self)
		copy_state.bots = copy.deepcopy(self.bots)
		copy_state.humans = copy.deepcopy(self.humans)
		copy_state.obstacles = copy.deepcopy(self.obstacles)
		copy_state.pellets = copy.deepcopy(self.pellets)
		return copy_state
		
		
	def getSuccessors(self, agent_index):
		successors = []
		if agent_index < len(self.bots):	
			agent_pose = self.bots['robot'+str(agent_index)]
			agent_char = 'b'
		else:
			agent_pose = self.humans['human' + str(agent_index - len(self.bots))]
			agent_char = 'h'
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				#if i == j == 0: continue
				if self.isValidPose((agent_pose[0]+i,agent_pose[1]+j)):
					new_state = self.copy()
					if agent_char == 'h' and new_state.env.grid[agent_pose[0]][agent_pose[1]] == 'f':
						new_state.env.grid[agent_pose[0]][agent_pose[1]] = 'p'
					else:
						new_state.env.grid[agent_pose[0]][agent_pose[1]] = '.'
					
					if agent_char == 'h' and new_state.env.grid[agent_pose[0]+i][agent_pose[1]+j] == 'p':
						new_state.env.grid[agent_pose[0]+i][agent_pose[1]+j] = 'f'
					else:
						new_state.env.grid[agent_pose[0]+i][agent_pose[1]+j] = agent_char
						
					if agent_char == 'h':
						new_state.humans['human' + str(agent_index - len(self.bots))] = (agent_pose[0]+i,agent_pose[1]+j)
					else:
						new_state.bots['robot'+str(agent_index)] = (agent_pose[0]+i,agent_pose[1]+j)

					successors.append(new_state)
					
		return successors	
				
	def display(self):
		first_row = ''
		for i in xrange(self.env.length):
			first_row += (str( i ) + ' ')
		print ' ',first_row
		for index in xrange(self.env.breadth):
			row = ''
			for i in self.env.grid[self.env.breadth - index - 1]:
				row += (str(i) + ' ')
			print self.env.breadth - index - 1, row


		print '------------------------------'
		
		
if __name__ == '__main__':
	state = State(9,8)
	robots = [(5,5),]
	humans = [(3,3),(2,2)]
	pellets = [(0,0),(2,1),(0,2),(0,3),(0,4)]
	obstacles = [(3,2),]
	state.setState(robots,humans,obstacles,pellets)
	state.display()
	
	for child in state.getSuccessors(2):
		for i in child.env.grid:
			for j in i:
				if j == 'f':
					print 'child'
					print child.humans
					child.display()
					print 'grand children'
					for grand_child in child.getSuccessors(2):
						print grand_child.humans
						grand_child.display()
		
	
	
