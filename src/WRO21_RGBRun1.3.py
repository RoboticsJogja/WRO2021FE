#Libraries
import RPi.GPIO as GPIO
import time
 
#Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ultrasonicTrigger1 = 18
ultrasonicEcho1 = 16
ultrasonicTrigger2 = 21
ultrasonicEcho2 = 20

motorIN1 = 17
motorIN2 = 27
motorEN1 = 22

servoPIN = 13

colourS0 = 8
colourS1 = 25
colourS2 = 6
colourS3 = 5
colourOUT = 26
numCycles = 5

buttonPIN = 11
ledPIN = 9

GPIO.setup(ultrasonicTrigger1, GPIO.OUT) 
GPIO.setup(ultrasonicEcho1, GPIO.IN)
GPIO.setup(ultrasonicTrigger2, GPIO.OUT) 
GPIO.setup(ultrasonicEcho2, GPIO.IN)

GPIO.setup(motorIN1,GPIO.OUT)
GPIO.setup(motorIN2,GPIO.OUT)
GPIO.setup(motorEN1,GPIO.OUT)
GPIO.output(motorIN1,GPIO.LOW)
GPIO.output(motorIN2,GPIO.LOW)

GPIO.setup(servoPIN, GPIO.OUT)

GPIO.setup(colourOUT,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(colourS0,GPIO.OUT)
GPIO.setup(colourS1,GPIO.OUT)
GPIO.setup(colourS2,GPIO.OUT)
GPIO.setup(colourS3,GPIO.OUT)
GPIO.output(colourS0,GPIO.LOW)
GPIO.output(colourS0,GPIO.HIGH)

GPIO.setup(buttonPIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPIN,GPIO.OUT)

P1=GPIO.PWM(motorEN1,1000)
P1.start(25)
P2 = GPIO.PWM(servoPIN, 50)
P2.start(2.5)

counter1 = 0
counter2 = 0
x = 0

print("\n")

#Functions
def distance1():
    GPIO.output(ultrasonicTrigger1, True)
    time.sleep(0.01)
    GPIO.output(ultrasonicTrigger1, False)
    startTime = time.time()
    stopTime = time.time()
 
    while GPIO.input(ultrasonicEcho1) == 0:
        startTime = time.time()
 
    while GPIO.input(ultrasonicEcho1) == 1:
        stopTime = time.time()
 
    timeElapsed1 = stopTime - startTime
    distance1 = (timeElapsed1 * 34300) / 2
 
    return distance1


def distance2():
    GPIO.output(ultrasonicTrigger2, True)
    time.sleep(0.01)
    GPIO.output(ultrasonicTrigger2, False)
    startTime2 = time.time()
    stopTime2 = time.time()
 
    while GPIO.input(ultrasonicEcho2) == 0:
        startTime2 = time.time()
    while GPIO.input(ultrasonicEcho2) == 1:
        stopTime2 = time.time()
 
    timeElapsed2 = stopTime2 - startTime2
    distance2 = (timeElapsed2 * 34300) / 2
 
    return distance2


def setAngle(angle):
    duty = (angle / 18) + 2.75 #2.75
    GPIO.output(13, True)
    P2.ChangeDutyCycle(duty)
    time.sleep(0.1)
    GPIO.output(13, False)
    P2.ChangeDutyCycle(duty)
    #print ("Measured Duty = %.1f " % duty)



try:
    setAngle(105)
    lastError = 0
    dist1=1000
    dist2=1000
    dist1b=0
    dist2b=0
    #limit1 = 250
    #limit2 = 2000
    
    temp = 1
    delay = 0.001
    control = 100
    GPIO.output(ledPIN,GPIO.HIGH)
    
    while GPIO.input(buttonPIN) == GPIO.HIGH:
        print (".")
    
    P1.ChangeDutyCycle(70)
    GPIO.output(motorIN1,GPIO.LOW)
    GPIO.output(motorIN2,GPIO.HIGH)
    print("run")

    
    while counter2 < 50:
        time.time()
        dist1 = distance1() + 5     #kiri
        #if(dist1>limit2):
        #    dist1=dist1b
        #elif(dist1>limit1):
        #    dist1=limit1
                
        dist2 = distance2()         #kanan
        #if(dist2>limit2):
        #    dist2=dist2b
        #elif(dist2>limit1):
        #    dist2=limit1

        compare = dist2-dist1
        P = compare*0.082 #0.072
        D = (compare-lastError)*0.03 #0.03
        
        steer = P+D+90+15
        lastError = compare
        if(steer>145):
            steer = 145
        elif(steer<65):
            steer = 65
           
        setAngle(steer)

        dist1b=dist1
        dist2b=dist2


        GPIO.output(colourS2,GPIO.LOW)
        GPIO.output(colourS3,GPIO.LOW)
        time.sleep(delay)
        start = time.time()
        for impulse_count in range(numCycles):
          GPIO.wait_for_edge(colourOUT, GPIO.FALLING)
        duration = time.time() - start
        lineDetect = numCycles / duration / 100


        #print ("Measured Distance1 = %.1f cm" % dist1)
        #print ("Measured Distance2 = %.1f cm" % dist2)
        #print ("Steer = %.1f degree" % steer)
        #print("Line Detect = %.1f" % lineDetect)
        
        if lineDetect>4 and x == 1:
            x = 0
            temp=1
            #print("white")
        elif lineDetect<4 and x == 0:
            counter1 = counter1 + 1
            x = 1
            temp=0

        if counter>12:
            counter2 = counter2 +1
            
        #print("Counter = %.0f" % counter1)


    time.sleep(2)
    print("stop")
    GPIO.output(motorIN1,GPIO.LOW)
    GPIO.output(motorIN2,GPIO.LOW)    
    P2.stop()
    GPIO.cleanup()

except KeyboardInterrupt:
    print("stop")
    GPIO.output(motorIN1,GPIO.LOW)
    GPIO.output(motorIN2,GPIO.LOW)    
    P2.stop()
    GPIO.cleanup()
