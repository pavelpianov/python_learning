#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
	while True:
		freedom = False
		while not wall_is_on_the_left():
			move_left()
			if not wall_is_above():
				freedom = True
				while not wall_is_above():
					move_up()
		while not wall_is_on_the_left():
			move_left()
		
		while not freedom and not wall_is_on_the_right():
			move_right()
			if not wall_is_above():
				while not wall_is_above():
					freedom = True
					move_up()
		while not wall_is_on_the_left():
			move_left()

		break


if __name__ == '__main__':
	run_tasks()
