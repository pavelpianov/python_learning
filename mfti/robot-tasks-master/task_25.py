#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
	while True:
		move_down()
		
		while not wall_is_on_the_right():
			fill_cross()
			if not wall_is_on_the_right():
				move_right(2)
		
		move_left(2)
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
