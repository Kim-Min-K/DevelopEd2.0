import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
twistSwitch = 26
blueSwitch = 26
redSwitch = 26
greenSwitch = 26
yellowSwitch = 26
clickSwitch = 26

GPIO.setup(twistSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(blueSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(redSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(yellowSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(clickSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def getInput(value):
    
    if GPIO.input(value) == GPIO.HIGH:
        state = False
    else:
        state = True
    return state

def updateState():
    pushBlue = getInput(blueSwitch)
    pushGreen = getInput(greenSwitch)
    pushRed = getInput(redSwitch)
    pushBlue = getInput(blueSwitch)
    switchBlue =                  
