from ev3dev.ev3 import *

if __name__ == '__main__':
	r = LargeMotor('outB')
	l = LargeMotor('outC')
	r.reset()
	l.reset()
