#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_30():

	c = 0

	while True:
		

		while not wall_is_on_the_right():

			if not wall_is_beneath():
				move_down()
			while not wall_is_on_the_right():
				if not wall_is_beneath():
					move_down()
					c = 0
				else:
					move_right()
			c += 1

		while not wall_is_on_the_left():
			if not wall_is_beneath():
				move_down()
			while not wall_is_on_the_left():
				if not wall_is_beneath():
					move_down()
					c = 0
				else:
					move_left()
			
			c += 1
		
		if c >= 2:
			break






if __name__ == '__main__':
	run_tasks()
