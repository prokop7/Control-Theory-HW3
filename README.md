# Control-Theory-HW3
Assignment #3 for Control Theory [S18] course

## Description
```
Motion along the wall:
  Robot should keep moving on the same distance of the wall as it was at the beginning
```

## Uses
1. [**ev3dev**](http://www.ev3dev.org) as OS for a brick
2. **Python 3** as a main language

## Contains
1. [**follower.py**](https://github.com/prokop7/Control-Theory-HW3/blob/master/follower.py) as the main program to run
2. [**stop_engine.py**](https://github.com/prokop7/Control-Theory-HW3/blob/master/stop_engine.py) to stop engines if something went wrong

## Robot
1. Lego Mindstorm EV3 with US sensor. Left motor in port C, right motor in port B, US sensor in port 1.

## Solution
Solution for this task is a PID controller with tweaks. In my case with coefficients P=3, I=0.1, D=1. Under tweaks, I meant limiting the amount of error for the I coefficient. I did it to balance the system when it takes a lot of errors for a short time. Also, it reduce time of transient process.
I don't think that these values are the best. Because there is no best. It depends on what do you want form the transiet process. I got this values by experiments and my background experience. 
1. P = 3. The most significant value in the system. By increasing you will get faster response but also, it can lead to unstability.
2. I = 0.1. By my experience integral component can't be large. And should be used only to avoid stable error or do a some fast movements by fastest collecting errors. But the large values of sum_error shuold be wiped at the certain time. For that case there is another tweak. In my task I just limited this error in [-1000, 1000] and it can change my speed value only by [-100, 100] (1000\*0.1).
3. D = 1. This values doesn't bring stability for the smooth walls but it helps when you have a sharp edges, gaps, disturbances in sensor. It allows to compensate the error from P component.

## [YouTube Link](https://youtu.be/rBSXCNGxGx8)
