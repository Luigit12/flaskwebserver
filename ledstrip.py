import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from flask import Flask
app = Flask(__name__)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)


def makePage(body):
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>''' + body + '''
        <hr/>
        <ul>
            <li><a href="red">Red</a></li>
            <li><a href="yellow">Yellow</a></li>
            <li><a href="green">Green</a></li>
            <li><a href="off">All Off</a></li>
        </body>
    </html>
    '''

@app.before_request
def allOff():
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    print("turn everything off at the beginning")
   
@app.route('/')
def index():
    return makePage('Index')

@app.route('/red')
def red():
    GPIO.output(20,GPIO.HIGH)
    print("Red on")
    return makePage('Red')

@app.route('/yellow')
def yellow():
    GPIO.output(21,GPIO.HIGH)
    print('Blue on')
    return makePage('Yellow')

@app.route('/green')
def green():
    GPIO.output(26,GPIO.HIGH)
    print('green on')
    return makePage('Green')

@app.route('/off')
def off():
    GPIO.output(26,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    print('all off')
    return makePage('Off')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
