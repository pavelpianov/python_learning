#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	while True:
		if not wall_is_on_the_right() and not wall_is_beneath():
			move_right(9)
			move_down(9)
			break

		elif not wall_is_on_the_left() and not wall_is_beneath():
			move_left(9)
			move_down(9)
			break

		elif not wall_is_on_the_right() and not wall_is_above():
			move_right(9)
			move_up(9)
			break

		elif not wall_is_on_the_left() and not wall_is_above():
			move_left(9)
			move_up(9)
			break

if __name__ == '__main__':
	run_tasks()
