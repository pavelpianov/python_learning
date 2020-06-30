#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
	while True:
		c = 0
		while c != 3:
			move_right()
			if cell_is_filled():
				c += 1
			elif not cell_is_filled():
				c = 0
			if wall_is_on_the_right():
				break
		break


if __name__ == '__main__':
	run_tasks()
