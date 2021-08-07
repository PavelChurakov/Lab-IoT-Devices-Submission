# !/usr/bin/env python

from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar
import random
import turtle

picar.setup()

tr = turtle.Turtle()
turtle.screensize(1000, 1000)
tr.color('black')
tr.pencolor("orange")
tr.shape('square')

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

fw_speed = 50
bw_speed = 40

back_distance = 20
turn_distance = 30
speed_reduct_distance = 50
last_angle = 135


def rand_abstmovement():
    while True and abs(tr.xcor()) < 500 and abs(tr.ycor()) < 500:
        if ua.get_distance() < back_distance:
            tr.speed(2)
            print("Let's go back!")
            ang = opposite_angle()
            print("Turn by angle ", ang)
            fw.turn(ang)
            print("Go back!")
            bw.forward()
            turn_turtle(tr, ang)
            print(time.time())
            run_turtle_back(tr, 2, 1, 0.1)
            print(time.time())
            ang = opposite_angle()
            print("Turn by angle", ang)
            fw.turn(ang)
            bw.backward()
            turn_turtle(tr, ang)
            run_turtle_forw(tr, 2, 1, 0.1)
            print("Go forward!")
            bw.speed = bw_speed
        elif ua.get_distance() < turn_distance:
            tr.speed(2)
            print("Go round!")
            ang = rand_dodge()
            print("Turn by angle ", ang)
            fw.turn(ang)
            bw.backward()
            turn_turtle(tr, ang)
            run_turtle_forw(tr, 2, 1, 0.1)
        else:
            fw.turn_straight()
            bw.backward()
            bw.speed = fw_speed
        while (ua.get_distance() > turn_distance + 15) and abs(tr.xcor()) < 500 and abs(tr.ycor()) < 500:
            tr.speed(4)
            print("Go forward!")
            fw.turn_straight()
            bw.backward()
            tr.fd(2)
        bw.speed = fw_speed / 2
        tr.speed(2)
        tr.fd(1)
    print("Stop!")
    bw.stop()
    fw.turn_straight()


def rand_dodge():
    angle = 90 + random.choice([-1, 1]) * fw.turning_max
    return angle


def opposite_angle():
    global last_angle
    if last_angle < 90:
        angle = last_angle + 2 * fw.turning_max
    else:
        angle = last_angle - 2 * fw.turning_max
    last_angle = angle
    return angle


def turn_turtle(tr, ang):
    if ang > 90:
        tr.right(ang - 90)
    else:
        tr.left(90 - ang)


def run_turtle_forw(tr, dist, t, delta):
    time_fw = 0
    while t > time_fw:
        tr.fd(dist)
        time.sleep(delta)
        time_fw += delta


def run_turtle_back(tr, dist, t, delta):
    time_fw = 0
    while t > time_fw:
        tr.bk(dist)
        time.sleep(delta)
        time_fw += delta


def stop():
    bw.stop()
    fw.turn_straight()


if __name__ == '__main__':
    try:
        rand_abstmovement()
    except KeyboardInterrupt:
        stop()




