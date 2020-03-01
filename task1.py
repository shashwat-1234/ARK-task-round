#!/usr/bin/env python
import sys

import click
#player = true is max, player = false is min agent 
from env import TicTacToeEnv, agent_by_mark, check_game_status,\
	after_action_state, tomark, next_mark

class HumanAgent(object):
	
	def __init__(self, mark):
		self.mark = mark

	def act(self, state, ava_actions):
		while True:
			uloc = input("Enter location[1-9], q for quit: ")
			if uloc.lower() == 'q':
				return None
			try:
				action = int(uloc) - 1
				if action not in ava_actions:
					raise ValueError()
			except ValueError:
				print("Illegal location: '{}'".format(uloc))
			else:
				break

		return action


class Computer(object):

	def __init__(self, mark):
		self.mark = mark

	def act(self, state, ava_actions):
		final_score = 10000
		final_move = 0
		for action in ava_actions:
			nstate = after_action_state(state, action)
			ava_actions.remove(action)
			final_score = min(final_score, value(nstate, ava_actions, 1, False))
			final_move = action
			ava_actions.append(action)
		return final_move                       

def value(state, ava_actions, nomov, player):
	
	gmstat = check_game_status(state[0])
	if gmstat>0 :
		if tomark(gmstat) == state[1] and player == True:
			return 10-nomov                                 #here it is used to check if the game
		else:                                                #is over or not  
			return -10
	elif gmstat == 0:
		return 0                                             #0 for draw and -ve for lose of current player
	
	finalVal = 0
	if(player):
		finalVal = -10000
		for action in ava_actions:
			ava_actions.remove(action)
			nstate = after_action_state(state, action)
			finalVal = max(finalVal, finalVal+value(nstate, ava_actions, nomov+1, False))
			ava_actions.append(action)
	else:
		finalVal = 10000
		for action in ava_actions:
			ava_actions.remove(action)
			nstate = after_action_state(state, action)
			finalVal = min(finalVal, finalVal+value(nstate, ava_actions, nomov+1, True))
			ava_actions.append(action)
	
	return finalVal


@click.command(help="Play human agent.")
@click.option('-n', '--show-number', is_flag=True, default=False,
			  show_default=True, help="Show location number in the board.")

def play(show_number):
	env = TicTacToeEnv(show_number=show_number)
	agents = [HumanAgent('O'),
			  Computer('X')]
	episode = 0
	while True:
		state = env.reset()
		_, mark = state
		done = False
		env.render()
		while not done:
			agent = agent_by_mark(agents, next_mark(mark))
			env.show_turn(True, mark)
			ava_actions = env.available_actions()
			action = agent.act(state, ava_actions)
			if action is None:
				sys.exit()

			state, reward, done, info = env.step(action)

			print('')
			env.render()
			if done:
				env.show_result(True, mark, reward)
				break
			else:
				_, _ = state
			mark = next_mark(mark)
		
		episode += 1


if __name__ == '__main__':
	play()
