"""MCP23008 I2C LCD backpack"""
import time
# pip install adafruit-circuitpython-charlcd
import board
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C
# pip install adafruit-circuitpython-pcf8574
from adafruit_pcf8574 import PCF8574
from adafruit_character_lcd.character_lcd import Character_LCD_Mono


class Character_LCD_I2C_PCF(Character_LCD_Mono):

    def __init__(
        self,
        i2c,
        columns,
        lines,
        address = None,
        backlight_inverted = False,
    ) -> None:

        if address:
            pcf = PCF8574(i2c, address=address)
        else:
            pcf = PCF8574(i2c)
        super().__init__(
            pcf.get_pin(1),
            pcf.get_pin(2),
            pcf.get_pin(3),
            pcf.get_pin(4),
            pcf.get_pin(5),
            pcf.get_pin(6),
            columns,
            lines,
            backlight_pin=pcf.get_pin(7),
            backlight_inverted=backlight_inverted,
        )


LCD_COLS = 16
LCD_ROWS = 2
ADDR = 0x27

i2c = board.I2C()
lcd = Character_LCD_I2C(i2c, LCD_COLS, LCD_ROWS, ADDR)

# Turn backlight on
lcd.backlight = True
# Print a two line message
lcd.message = "Hello\nCircuitPython"
time.sleep(5)
lcd.clear()
# Print two line message right to left
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello\nCircuitPython"
time.sleep(5)
# Return text direction to left to right
lcd.text_direction = lcd.LEFT_TO_RIGHT
lcd.clear()
# Display cursor
lcd.cursor = True
lcd.message = "Cursor! "
time.sleep(5)
lcd.clear()
# Display blinking cursor
lcd.blink = True
lcd.message = "Blinky Cursor!"
time.sleep(5)
lcd.blink = False
lcd.clear()
# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg
# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()
# Turn backlight off
lcd.backlight = False
lcd.message = "Going to sleep\nCya later!"
time.sleep(5)
lcd.clear()
