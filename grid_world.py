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
	pellets_eaten = 0
	bots = {}
	humans = {}
	pellets = []
	obstacles = []
	win_status = False
	lose_status = False
	def __init__(self,l,b):
		self.env = GridWorld(l,b)
	def getNumAgents(self):
		return len(self.bots) + len(self.humans)
	def setState(self,robots,humans,obstacles,pellets):

		for i in pellets:
			self.env.grid[i[0]][i[1]] = 'p'
			
		for i in xrange(len(humans)):
			self.humans['human' + str(i)] = humans[i]
			if self.env.grid[humans[i][0]][humans[i][1]] == 'p':
				self.env.grid[humans[i][0]][humans[i][1]] = 'f'
			else:
				self.env.grid[humans[i][0]][humans[i][1]] = 'h'
		self.obstacles	= copy.deepcopy(obstacles)
		for i in xrange(len(robots)):
			self.bots['robot' + str(i)] = copy.deepcopy(robots[i])
			
			self.env.grid[robots[i][0]][robots[i][1]] = 'b'
		for i in obstacles:
			self.env.grid[i[0]][i[1]] = 'o'
		
		self.pellets = copy.deepcopy(pellets)
		

		
	def isValidPose(self, pose,agent_index):
		return (pose[0] <= self.env.length and pose[0] >= 0 and pose[1] <= self.env.breadth and pose[1] >= 0) and ((self.env.grid[pose[0]][pose[1]] == '.' or self.env.grid[pose[0]][pose[1]] == 'p') or (agent_index != 0 and self.env.grid[pose[0]][pose[1]] == 'b'))

	def copy(self):
		copy_state = copy.deepcopy(self)
		copy_state.bots = copy.deepcopy(self.bots)
		copy_state.humans = copy.deepcopy(self.humans)
		copy_state.obstacles = copy.deepcopy(self.obstacles)
		copy_state.pellets = copy.deepcopy(self.pellets)
		return copy_state
	
	def getLegalActions(self, agent_index):
		legal_actions = []
		if agent_index < len(self.bots):	
			agent_pose = self.bots['robot'+str(agent_index)]
			agent_char = 'b'
		else:
			agent_pose = self.humans['human' + str(agent_index - len(self.bots))]
			agent_char = 'h'
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				if i==j==0: continue # remove this if staying is allowed
				if i==j==0 or self.isValidPose((agent_pose[0]+i,agent_pose[1]+j),agent_index):
					legal_actions.append((i,j),)
		return legal_actions
		
	def getActionSuccessor(self, agent_index, action):
	
		if agent_index < len(self.bots):	
			agent_pose = self.bots['robot'+str(agent_index)]
			agent_char = 'b'
		else:
			agent_pose = self.humans['human' + str(agent_index - len(self.bots))]
			agent_char = 'h'

		if action == (0,0) or self.isValidPose((agent_pose[0]+action[0],agent_pose[1]+action[1]),agent_index):
			new_state = self.copy()
			if action != (0,0):
				if new_state.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'b':
					new_state.win_status = False
					new_state.lose_status = True
				if agent_char == 'b' and new_state.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'p':
					new_state.pellets_eaten += 1
					new_state.pellets.remove((agent_pose[0]+action[0],agent_pose[1]+action[1]))

				if agent_char == 'h' and new_state.env.grid[agent_pose[0]][agent_pose[1]] == 'f':
					new_state.env.grid[agent_pose[0]][agent_pose[1]] = 'p'
				else:
					new_state.env.grid[agent_pose[0]][agent_pose[1]] = '.'
				
				if agent_char == 'h' and new_state.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'p':
					new_state.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] = 'f'
				else:
					new_state.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] = agent_char
					
				if agent_char == 'h':
					new_state.humans['human' + str(agent_index - len(self.bots))] = (agent_pose[0]+action[0],agent_pose[1]+action[1])
				else:
					new_state.bots['robot'+str(agent_index)] = (agent_pose[0]+action[0],agent_pose[1]+action[1])
					
			if len(new_state.pellets) == 0:
				new_state.win_status = True

			return new_state
		
		else:
			raise ValueError("The action is invalid")	
		
	def applyAction(self, agent_index, action):
	
		
		if agent_index < len(self.bots):	
			agent_pose = self.bots['robot'+str(agent_index)]
			agent_char = 'b'
		else:
			agent_pose = self.humans['human' + str(agent_index - len(self.bots))]
			agent_char = 'h'

		if action == (0,0) or self.isValidPose((agent_pose[0]+action[0],agent_pose[1]+action[1]),agent_index):
			
			if action != (0,0):
				if self.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'b':
					self.win_status = False
					self.lose_status = True
				if agent_char == 'b' and self.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'p':
					self.pellets_eaten += 1
					self.pellets.remove((agent_pose[0]+action[0],agent_pose[1]+action[1]))
				if agent_char == 'h' and self.env.grid[agent_pose[0]][agent_pose[1]] == 'f':
					self.env.grid[agent_pose[0]][agent_pose[1]] = 'p'
				else:
					self.env.grid[agent_pose[0]][agent_pose[1]] = '.'
				
				if agent_char == 'h' and self.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] == 'p':
					self.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] = 'f'
				else:
					self.env.grid[agent_pose[0]+action[0]][agent_pose[1]+action[1]] = agent_char
					
				if agent_char == 'h':
					self.humans['human' + str(agent_index - len(self.bots))] = (agent_pose[0]+action[0],agent_pose[1]+action[1])
				else:
					self.bots['robot'+str(agent_index)] = (agent_pose[0]+action[0],agent_pose[1]+action[1])
			
			if len(self.pellets) == 0:
				self.win_status = True

			return self
		
		else:
			raise ValueError("The action is invalid")
	
	def getAllSuccessors(self, agent_index):
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
				if i == j == 0 or self.isValidPose((agent_pose[0]+i,agent_pose[1]+j),agent_index):
					new_state = self.copy()
					if not (i == j == 0):
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
		
		

		
		
	
	
