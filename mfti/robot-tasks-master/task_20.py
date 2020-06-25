#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	while True:
		for i in range(6):
		# while not wall_is_beneath():
			while not wall_is_on_the_right():
				move_right()
				if not wall_is_on_the_right():
					fill_cell()
			move_down()
			while not wall_is_on_the_left():
				move_left()
				if not wall_is_on_the_left():
					fill_cell()
			move_down()
		move_right()
		break


if __name__ == '__main__':
	run_tasks()
