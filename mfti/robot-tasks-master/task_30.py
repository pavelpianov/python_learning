#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
	while True:
		a = 0
		while not wall_is_on_the_right():
			a += 1
			move_right()
		move_left(a)

		stopGoingDown = False
		i = 0

		while not stopGoingDown:
			stopGoingRight = False
			i += 1
			j = 0
			while not stopGoingRight:
				j += 1
				if i != j and not (i + j == a + 2):
					fill_cell()
				if not wall_is_on_the_right():
					move_right()
				elif wall_is_on_the_right():
					stopGoingRight = True
			if not wall_is_beneath():
				move_down()
			elif wall_is_beneath():
				stopGoingDown = True
			while not wall_is_on_the_left():
				move_left()

		break

if __name__ == '__main__':
	run_tasks()
