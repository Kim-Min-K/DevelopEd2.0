import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
twistSwitch = 19
blueSwitch = 6
clickSwitch = 13
greenSwitch = 26
yellowSwitch = 5
redSwitch = 0

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
    pushYellow = getInput(yellowSwitch)
    switchBlue = getInput(clickSwitch)
    twishBlack = getInput(twistSwitch)

    return pushBlue,pushGreen,pushRed,pushYellow,switchBlue,twishBlack

def clearState(pushBlue,pushGreen,pushRed,pushYellow,switchBlue,twishBlack):
    pushBlue = False
    pushGreen = False
    pushRed = False
    pushYellow = False
    switchBlue = False
    twishBlack = False
    return pushBlue,pushGreen,pushRed,pushYellow,switchBlue,twishBlack
# while True:
#     pushBlue,pushGreen,pushRed,pushYellow,switchBlue,twishBlack = updateState()
#     print('Blue Button: {Blue} \n Green Button {green} \n Red Button {red} \n Yellow Button {yellow} \n Push Switch {push} \n Twist Swtich {twist}'.format(Blue = pushBlue, green = pushGreen, red = pushRed, yellow = pushYellow, push = switchBlue, twist =twishBlack))
