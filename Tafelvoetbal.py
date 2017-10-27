import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 1
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)


def lsensor(scoreBlauw, scoreOranje):
    while True:
        if GPIO.input(4) == 1:
            print('pin 4 = 1')
            lcd.clear()
            scoreOranje += 1
            lcd.message(' Oranje scoort! \nDe score is ' + str(scoreOranje) + '-' + str(scoreBlauw))
            time.sleep(1)
            time.sleep(1)
            lcd.clear()
            lcd.message('Game on! \n Score: ' + str(scoreOranje) + '-' + str(scoreBlauw))
            time.sleep(4)
            if scoreOranje < 10:
                lsensor(scoreBlauw, scoreOranje)
        if scoreOranje == 10:
            lcd.clear()
            lcd.message(' Oranje wint  \n Score: ' + str(scoreOranje) + '-' + str(scoreBlauw))
            break

        if GPIO.input(13) == 1:
            print('pin 13 = 0')
            lcd.clear()
            scoreBlauw += 1
            lcd.message('Blauw scoort!\nDe score is ' + str(scoreOranje) + '-' + str(scoreBlauw))
            time.sleep(1)
            lcd.clear()
            lcd.message('Game on! \n Score: ' + str(scoreOranje) + '-' + str(scoreBlauw))
            time.sleep(4)

        if scoreBlauw == 10:
            lcd.clear()
            lcd.message(' Blauw wint  \nDe score is ' + str(scoreOranje) + '-' + str(scoreBlauw))
            break


scoreOranje = 0
scoreBlauw = 0


def test():
    while True:
        if GPIO.input(4) == 1:
            print('pin 4 = 1')
        if GPIO.input(13) == 1:
            print('pin 13 = 1')
        time.sleep(1)


keuze = input('1 = test sensoren, 2 = script')
if keuze == 2:
    lsensor(scoreOranje, scoreBlauw)
else:
    test()