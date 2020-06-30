#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
	while True:
		c = 0
		stop = False

		while not wall_is_on_the_right() and not stop:
			
			if not c:
				move_right()
				fill_cell()
				c += 1

			elif c:
				for i in range(c):
					if not wall_is_on_the_right():
						move_right()
					else:
						stop = True
						break
				if not stop and not wall_is_on_the_right():
					fill_cell()
				c += 1

		
		break

if __name__ == '__main__':
	run_tasks()
