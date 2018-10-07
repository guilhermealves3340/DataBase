# on importe le pilote
import sys
sys.path.append("./lib")
import lcddriver
from time import *

import serial

sr = serial.Serial('/dev/ttyACM0', 9600)

# on initialise le lcd
lcd = lcddriver.lcd()       #OBJETO LCD

# on reinitialise le lcd
lcd.lcd_clear()


lcd.lcd_display_string("TEMPERATURA", 1)

while True:

    
    x = sr.read(3)      #LENDO A TEMPERATURA 
    y = str(x)          #CONVERTENDO A TEMPERATURA QUE É UM OBJETO EM UMA STRING
    z = y[3]+y[4]
    g = int(z)

    if(g >= 50):
        lcd.lcd_display_string(z + " ALERTA", 2)

    
    lcd.lcd_display_string(z, 2)    #PRINTANDO NO DISPLAY A TEMPERATURA

