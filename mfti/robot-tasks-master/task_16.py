#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	while True:
		direction = 0
		while direction == 0:
			while not wall_is_above():
				move_up()
				direction = 1
			break

			while not wall_is_beneath():
				move_down()
				direction = 3
			break

			while not wall_is_on_the_left():
				move_left()
				direction = 4
			break

			while not wall_is_on_the_right():
				move_right()
				direction = 2
			break

		if direction == 1 or direction == 3:
			if not wall_is_on_the_left():
				while not wall_is_on_the_left():
					move_left()
			else:
				while not wall_is_on_the_right():
					move_right()

		elif direction == 2 or direction == 4:
			if wall_is_above():
				while not wall_is_above():
					move_up()
			else:
				while not wall_is_beneath():
					move_down()

		break


if __name__ == '__main__':
	run_tasks()
