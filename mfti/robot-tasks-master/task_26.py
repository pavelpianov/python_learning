#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
	while True:
		stopGoingDown = False
		while not wall_is_beneath() and not stopGoingDown:
			while not wall_is_on_the_right():
				fill_cross()
				if not wall_is_on_the_right():
					move_right(2)
				else:
					while not wall_is_on_the_left():
						move_left()
					break
			
			for i in range(4):
				if not wall_is_beneath():
					move_down()
				elif wall_is_beneath():
					move_up(2)
					stopGoingDown = True
					break
			
		break

def fill_cross():
	move_right()
	fill_cell()
	move_down()
	fill_cell()
	move_left()
	fill_cell()
	move_right(2)
	fill_cell()
	move_left()
	move_down()
	fill_cell()
	move_up(2)
	move_right()


if __name__ == '__main__':
	run_tasks()
