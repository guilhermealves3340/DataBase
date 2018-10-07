# on importe le pilote
import sys
sys.path.append("./lib")
import lcddriver
from time import *
import serial

sr = serial.Serial('dev/ttyACM1', 9600)

# on initialise le lcd
lcd = lcddriver.lcd()       #OBJETO LCD

# on reinitialise le lcd
lcd.lcd_clear()

while True:

    # on affiche des caracteres sur chaque ligne
    
    lcd.lcd_display_string("Temperatura", 1)
    lcd.lcd_display_string("35 °C", 2)

