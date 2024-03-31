from ssd1289_16bit import ILI9341,color565
from machine import Pin, SPI
import utime
from FreeMono9pt7b import FreeMono9pt7b
from FreeSerifBold24pt7b import FreeSerifBold24pt7b
from gfxFont import gfxFont
from touch import Touch

RS = machine.Pin(21, machine.Pin.OUT)
WR = machine.Pin(22, machine.Pin.OUT)
RD = machine.Pin(26, machine.Pin.OUT)
CS = machine.Pin(27, machine.Pin.OUT)
RST = machine.Pin(28, machine.Pin.OUT)
FIRST = 0


led_onboard = Pin(25, Pin.OUT)

#spi2 = SPI(0,baudrate=5000000,sck=Pin(18), mosi=Pin(19), miso=Pin(16))

BLACK          = 0x0000      #   0,   0,   0
WHITE          = 0xFFFF      # 255, 255, 255
BLUE           = 0x001F      #   0,   0, 255
GREEN          = 0x07E0      #   0, 255,   0
RED            = 0xF800      # 255,   0,   0
NAVY           = 0x000F      #   0,   0, 128
DARKBLUE       = 0x0011      #   0,   0, 139
DARKGREEN      = 0x03E0      #   0, 128,   0
DARKCYAN       = 0x03EF      #   0, 128, 128
CYAN           = 0x07FF      #   0, 255, 255
TURQUOISE      = 0x471A      #  64, 224, 208
INDIGO         = 0x4810      #  75,   0, 130
DARKRED        = 0x8000      # 128,   0,   0
OLIVE          = 0x7BE0      # 128, 128,   0
GRAY           = 0x8410      # 128, 128, 128
GREY           = 0x8410      # 128, 128, 128
SKYBLUE        = 0x867D      # 135, 206, 235
BLUEVIOLET     = 0x895C      # 138,  43, 226
LIGHTGREEN     = 0x9772      # 144, 238, 144
DARKVIOLET     = 0x901A      # 148,   0, 211
YELLOWGREEN    = 0x9E66      # 154, 205,  50
BROWN          = 0xA145      # 165,  42,  42
DARKGRAY       = 0x7BEF      # 128, 128, 128
DARKGREY       = 0x7BEF      # 128, 128, 128
SIENNA         = 0xA285      # 160,  82,  45
LIGHTBLUE      = 0xAEDC      # 172, 216, 230
GREENYELLOW    = 0xAFE5      # 173, 255,  47
SILVER         = 0xC618      # 192, 192, 192
LIGHTGRAY      = 0xC618      # 192, 192, 192
LIGHTCYAN      = 0xE7FF      # 224, 255, 255
VIOLET         = 0xEC1D      # 238, 130, 238
AZUR           = 0xF7FF      # 240, 255, 255
BEIGE          = 0xF7BB      # 245, 245, 220
MAGENTA        = 0xF81F      # 255,   0, 255
TOMATO         = 0xFB08      # 255,  99,  71
GOLD           = 0xFEA0      # 255, 215,   0
ORANGE         = 0xFD20      # 255, 165,   0
SNOW           = 0xFFDF      # 255, 250, 250
YELLOW         = 0xFFE0      # 255, 255,   0

colors = [color565(255,0,0),color565(255,255,0),color565(0,255,0),color565(0,255,255),color565(0,0,255),color565(255,0,255),color565(0,0,0),color565(255,255,255)]


display = ILI9341(RS,WR,RD,CS,RST,FIRST,r=2)
xF = gfxFont( display, FreeSerifBold24pt7b )

    
display.ILI9341_FillScreen(WHITE)
   
display.ILI9341_FillRectangle(85, 50, 150, 50, color565(0,0,255))

display.ILI9341_FillRectangle(5, 140, 150, 50, color565(0,0,255))


display.ILI9341_FillRectangle(165, 140, 150, 50, color565(255,0,0))



#test1 = "Hello World!!"
#display.printstring(test1,0,0,2,GREEN)



xF.text(50, 180,"ON",WHITE)
xF.text(190, 180,"OFF",WHITE)

#display.print("LED OFF")

#LCD_Font(20, 65, "NODE 3", Open_Sans_Bold_8  , 1, BLUE);
class Screen(object): 

    def __init__(self,spi2):

        self.touch = Touch(spi2, 
                           cs=Pin(17), 
                           int_pin=Pin(20),
                           int_handler=self.touchscreen_press)

        self.dot = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

    def touchscreen_press(self, x, y):
        display.ILI9341_FillRectangle(0, 0, 120, 22, WHITE) 
        display.printstring("{0:03d}, {1:03d}".format(x, y),0,0,2,BLACK)
        
        if 115 <= x <= 185 and 75 <= y <= 175:
           led_onboard.value(1)
           display.ILI9341_FillRectangle(85, 50, 150, 50, color565(0,0,255))
           

        if 140 <= x <= 185 and 200 <= y <= 290: 
            led_onboard.value(0)
            display.ILI9341_FillRectangle(85, 50, 150, 50, color565(255,0,0))
            




def main():

    # Init SPI1 for touchscreen
    spi2 = SPI(0,baudrate=2500000,sck=Pin(18), mosi=Pin(19), miso=Pin(16))
    Screen(spi2)

while True: 
         main()

