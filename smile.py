from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]
w = [255,255,255]

smile = [
y,y,y,y,y,y,y,y,
y,w,w,y,y,w,w,y,
y,w,e,y,y,e,w,y,
y,w,w,y,y,w,w,y,
y,y,y,y,y,y,y,y,
y,e,y,y,y,y,e,y,
y,y,e,e,e,e,y,y,
y,y,y,y,y,y,y,y
]

wink = [
y,y,y,y,y,y,y,y,
y,w,w,y,y,y,e,y,
y,w,e,y,y,e,y,y,
y,w,w,y,y,y,e,y,
y,y,y,y,y,y,y,y,
y,e,y,y,y,y,e,y,
y,y,e,e,e,e,y,y,
y,y,y,y,y,y,y,y
]

happy = [
y,y,y,y,y,y,y,y,
y,y,e,y,y,e,y,y,
y,e,y,e,e,y,e,y,
y,y,y,y,y,y,y,y,
y,w,w,w,w,w,w,y,
y,e,e,e,e,e,e,y,
y,y,e,v,v,e,y,y,
y,y,y,y,y,y,y,y
]

oh = [
y,y,y,y,y,y,y,y,
y,w,w,y,y,w,w,y,
y,w,e,y,y,e,w,y,
y,w,w,y,y,w,w,y,
y,y,y,y,y,y,y,y,
y,y,y,e,e,y,y,y,
y,y,y,e,e,y,y,y,
y,y,y,y,y,y,y,y
]


sense.set_pixels(happy)
time.sleep(1)
sense.set_pixels(wink)
time.sleep(0.5)
sense.set_pixels(smile)

while True:
    shake = 1
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > shake or y > shake or z > shake:
        sense.set_pixels(oh)
	time.sleep(3)
	print str(x) + " X "
	print str(y) + " Y "
	print str(z) + " Z "

    else:
        sense.set_pixels(smile)
