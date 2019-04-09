import bs4 as bs
import urllib
import RPi.GPIO as GPIO
print("bs,urllib,gpio,time")
print("imported")
sigPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sigPin, GPIO.OUT)
print("pin setup done")

while True:
    urlThing = urllib.urlopen('http://192.168.0.10/diy/buttonStatus.php').read()
    output = bs.BeautifulSoup(urlThing, 'lxml')
    status = output.body.p.string
    if status == "ON":
        GPIO.output(sigPin, GPIO.HIGH)
    if status == "OFF":
        GPIO.output(sigPin, GPIO.LOW)
GPIO.cleanup()
