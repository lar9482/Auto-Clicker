import pynput
import time

from pynput.mouse import Button, Controller, Listener


class auto_clicker:
	def __init__(self, delay):
		self.mouse = Controller()
		self.time_delay = delay

	def click_mouse(self):
		self.mouse.press(Button.left)
		self.mouse.release(Button.left)

	def start_auto_clicker(self):
		while True:
			time.sleep(self.time_delay)
			self.click_mouse()


delay_in_seconds = 0.000000000000000000000001
auto = auto_clicker(delay_in_seconds)
auto.start_auto_clicker()

