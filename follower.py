#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# coeff for a PID controller
p = 3
i = 0.1
d = 1

# Boundaries for changing speed level
MIN = -200
MAX = 200

def bound(value, min, max):
	if (value > max):
		return max
	if (value < min):
		return min 
	return value

def main():
	r = LargeMotor('outB')
	l = LargeMotor('outC')
	us = UltrasonicSensor() 
	
	assert us.connected, "Connect a single US sensor to any sensor port"
	# Put the US sensor into distance mode.
	us.mode='US-DIST-CM'

	# Set initial values 
	dist = us.value()
	speed = 200
	err_sum = 0
	prev_err = 0

	# Main loop for 600 iterations. 600 * 0.01 ~ 6s
	for x in range(1,600):
		error = (us.value() - dist)
		change = error * p + err_sum * i + (error - prev_err) * d
		change = bound(change, MIN, MAX)

		lspeed = speed - change
		rspeed = speed + change
		
		# Some sort of log
		print("Value: " + str(us.value()) + ", Error: " + str(error) + ", l: " + str(lspeed) + ", r: " + str(rspeed) + ", err_sum: "  + str(err_sum))
		
		l.run_forever(speed_sp=lspeed)
		r.run_forever(speed_sp=rspeed)
		sleep(0.01)   # Give the motor time to move
		
		# Limit error in optimal values
		err_sum = bound(err_sum + error, -1000, 1000)
		prev_err = error
		
	
	r.reset()
	l.reset()

if __name__ == '__main__':
	main()
