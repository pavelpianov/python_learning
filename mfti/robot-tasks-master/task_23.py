#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
	pass


if __name__ == '__main__':
	run_tasks()
