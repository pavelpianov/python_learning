#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
	c = 0
	while True:
		while not wall_is_beneath():

			move_right()
			move_down()

			if wall_is_beneath():
				while not wall_is_on_the_left():
					move_left()
				move_right()
				break

			fill_cell()

			for i in range(c):
				move_left()
				fill_cell()
			
			if c:
				move_down()
				fill_cell()
				c += 1

			for i in range(c):
				move_right()
				fill_cell()

			c += 1

		break


if __name__ == '__main__':
	run_tasks()
