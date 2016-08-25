# grid_world
Classic grid world

'b' - robots
'h' - humans
'p' - pellets (aisle/ food/ reward points)
'f' - human standing over a pellet

The robot is running MinMax
Human takes random actions

The robot overestimates human's adversarial behaviour. Hence is afraid to eat the last pellet

Need to change this to ExpectiMax to see the difference

Evaluation function  :
0.1 * min_human_dist - 0.3 * min_pellet_dist + 0.05 * min_obstacle_dist	 + 100 * state.pellets_eaten + 500 * state.win_status - 5000 * state.lose_status;	

