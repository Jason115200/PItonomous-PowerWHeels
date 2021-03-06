#Create variables for our code
#Have an ultrasonic sensor light up an led when it reaches a certain distance

#Libraries
import RPi.GPIO as GPIO
import time

#GPIO mode (BOARD/BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction(IN/OUT)
GPIO.Setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.Setup(GPIO_ECHO, GIO.IN)

def distance()
    #set TRIGGER to high
    GPIO.output(GPIO_TRIGGER, True)

    #set Trigger after 0.01ms to low
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    #save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    #save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    #time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    #multiply with the sonic speed (34300 cm/s)
    #and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1 cm" % dist)
            time.sleep(1)

        #Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.Cleanup()
