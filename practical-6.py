import time
# pip install RPLCD smbus2
from RPLCD.i2c import CharLCD


ADDR = 0x27
LCD_ROWS = 2
LCD_COLS = 16
BACKPACK = "PCF8574"

display = CharLCD(BACKPACK, ADDR, cols=LCD_COLS, rows=LCD_ROWS, backlight_enabled=False)


def scroll(string, row=0, delay=0.1):
    string = string.center(2*display.lcd.cols + len(string))

    for i in range(len(string)+1 - display.lcd.cols):
        display.cursor_pos = (row, 0)
        display.write_string(string[i:i+display.lcd.cols])
        time.sleep(delay)


def scroll_n(string, row=0, n=-1, delay=0.1):
    while n!=0:
        scroll(string, row, delay)
        n -= 1


display.cursor_mode = "blink"

display.write_string("Hello\r\nworld")
time.sleep(5)
display.clear()

display.cursor_mode = "line"
display.text_align_mode = "right"

display.cursor_pos = (0, display.lcd.cols-1)
display.write_string("Hello"[::-1])
display.crlf()
display.write_string("world"[::-1])
time.sleep(5)
display.clear()

display.cursor_mode = "hide"
display.text_align_mode = "left"

display.cursor_pos = (display.lcd.rows-1, 0)
display.write_string("Hello, world!")
time.sleep(5)
display.clear()

display.backlight_enabled = True

display.write_string("Hello,")
scroll_n("Asadullah Shaikh", row=1, n=5)
display.clear()

display.close()
