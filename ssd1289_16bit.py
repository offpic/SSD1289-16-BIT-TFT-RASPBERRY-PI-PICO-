#Writed ISMAIL ALHAJJ FREE CODE FOR ALL
import time
import ustruct
from micropython import const
import rp2
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
from FreeMono9pt7b import FreeMono9pt7b
#Open_Sans_Bold_8_ref = Open_Sans_Bold_8

_RDDSDR = const(0x0f) # Read Display Self-Diagnostic Result
_SLPOUT = const(0x11) # Sleep Out
_GAMSET = const(0x26) # Gamma Set
_DISPOFF = const(0x28) # Display Off
_DISPON = const(0x29) # Display On
_CASET = const(0x2a) # Column Address Set
_PASET = const(0x2b) # Page Address Set
_RAMWR = const(0x2c) # Memory Write
_RAMRD = const(0x2e) # Memory Read
_MADCTL = const(0x36) # Memory Access Control
_VSCRSADD = const(0x37) # Vertical Scrolling Start Address
_PIXSET = const(0x3a) # Pixel Format Set
_PWCTRLA = const(0xcb) # Power Control A
_PWCRTLB = const(0xcf) # Power Control B
_DTCTRLA = const(0xe8) # Driver Timing Control A
_DTCTRLB = const(0xea) # Driver Timing Control B
_PWRONCTRL = const(0xed) # Power on Sequence Control
_PRCTRL = const(0xf7) # Pump Ratio Control
_PWCTRL1 = const(0xc0) # Power Control 1
_PWCTRL2 = const(0xc1) # Power Control 2
_VMCTRL1 = const(0xc5) # VCOM Control 1
_VMCTRL2 = const(0xc7) # VCOM Control 2
_FRMCTR1 = const(0xb1) # Frame Rate Control 1
_DISCTRL = const(0xb6) # Display Function Control
_ENA3G = const(0xf2) # Enable 3G
_PGAMCTRL = const(0xe0) # Positive Gamma Control
_NGAMCTRL = const(0xe1) # Negative Gamma Control
_CHUNK = const(1024) #maximum number of pixels per spi write

cmap = ['00000000000000000000000000000000000', #Space
        '00100001000010000100001000000000100', #!
        '01010010100000000000000000000000000', #"
        '01010010101101100000110110101001010', ##
        '00100011111000001110000011111000100', #$
        '11001110010001000100010001001110011', #%
        '01000101001010001000101011001001101', #&
        '10000100001000000000000000000000000', #'
        '00100010001000010000100000100000100', #(
        '00100000100000100001000010001000100', #)
        '00000001001010101110101010010000000', #*
        '00000001000010011111001000010000000', #+
        '000000000000000000000000000000110000100010000', #,
        '00000000000000011111000000000000000', #-
        '00000000000000000000000001100011000', #.
        '00001000010001000100010001000010000', #/
        '01110100011000110101100011000101110', #0
        '00100011000010000100001000010001110', #1
        '01110100010000101110100001000011111', #2
        '01110100010000101110000011000101110', #3
        '00010001100101011111000100001000010', #4
        '11111100001111000001000011000101110', #5
        '01110100001000011110100011000101110', #6
        '11111000010001000100010001000010000', #7
        '01110100011000101110100011000101110', #8
        '01110100011000101111000010000101110', #9
        '00000011000110000000011000110000000', #:
        '01100011000000001100011000010001000', #;
        '00010001000100010000010000010000010', #<
        '00000000001111100000111110000000000', #=
        '01000001000001000001000100010001000', #>
        '01100100100001000100001000000000100', #?
        '01110100010000101101101011010101110', #@
        '00100010101000110001111111000110001', #A
        '11110010010100111110010010100111110', #B
        '01110100011000010000100001000101110', #C
        '11110010010100101001010010100111110', #D
        '11111100001000011100100001000011111', #E
        '11111100001000011100100001000010000', #F
        '01110100011000010111100011000101110', #G
        '10001100011000111111100011000110001', #H
        '01110001000010000100001000010001110', #I
        '00111000100001000010000101001001100', #J
        '10001100101010011000101001001010001', #K
        '10000100001000010000100001000011111', #L
        '10001110111010110101100011000110001', #M
        '10001110011010110011100011000110001', #N
        '01110100011000110001100011000101110', #O
        '11110100011000111110100001000010000', #P
        '01110100011000110001101011001001101', #Q
        '11110100011000111110101001001010001', #R
        '01110100011000001110000011000101110', #S
        '11111001000010000100001000010000100', #T
        '10001100011000110001100011000101110', #U
        '10001100011000101010010100010000100', #V
        '10001100011000110101101011101110001', #W
        '10001100010101000100010101000110001', #X
        '10001100010101000100001000010000100', #Y
        '11111000010001000100010001000011111', #Z
        '01110010000100001000010000100001110', #[
        '10000100000100000100000100000100001', #\
        '00111000010000100001000010000100111', #]
        '00100010101000100000000000000000000', #^
        '00000000000000000000000000000011111', #_
        '11000110001000001000000000000000000', #`
        '00000000000111000001011111000101110', #a
        '10000100001011011001100011100110110', #b
        '00000000000011101000010000100000111', #c
        '00001000010110110011100011001101101', #d
        '00000000000111010001111111000001110', #e
        '00110010010100011110010000100001000', #f
        '000000000001110100011000110001011110000101110', #g
        '10000100001011011001100011000110001', #h
        '00100000000110000100001000010001110', #i
        '0001000000001100001000010000101001001100', #j
        '10000100001001010100110001010010010', #k
        '01100001000010000100001000010001110', #l
        '00000000001101010101101011010110101', #m
        '00000000001011011001100011000110001', #n
        '00000000000111010001100011000101110', #o
        '000000000001110100011000110001111101000010000', #p
        '000000000001110100011000110001011110000100001', #q
        '00000000001011011001100001000010000', #r
        '00000000000111110000011100000111110', #s
        '00100001000111100100001000010000111', #t
        '00000000001000110001100011001101101', #u
        '00000000001000110001100010101000100', #v
        '00000000001000110001101011010101010', #w
        '00000000001000101010001000101010001', #x
        '000000000010001100011000110001011110000101110', #y
        '00000000001111100010001000100011111', #z
        '00010001000010001000001000010000010', #{
        '00100001000010000000001000010000100', #|
        '01000001000010000010001000010001000', #}
        '01000101010001000000000000000000000' #}~
]



ILI9341_WIDTH  =240
ILI9341_HEIGHT =320

_BIT7 = const(0x80)
_BIT6 = const(0x40)
_BIT5 = const(0x20)
_BIT4 = const(0x10)
_BIT3 = const(0x08)
_BIT2 = const(0x04)
_BIT1 = const(0x02)
_BIT0 = const(0x01)

ILI9341_MADCTL_MY  =0x80
ILI9341_MADCTL_MX  =0x40
ILI9341_MADCTL_MV  =0x20
ILI9341_MADCTL_ML  =0x10
ILI9341_MADCTL_RGB =0x00
ILI9341_MADCTL_BGR =0x08
ILI9341_MADCTL_MH  =0x04

def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3


@rp2.asm_pio(out_init=(rp2.PIO.OUT_HIGH,) * 16, out_shiftdir=PIO.SHIFT_RIGHT,autopull=True, pull_thresh=16)

def paral_prog():
    pull()
    out (pins, 16)



def color565(r, g, b):
    return (r & 0xf8) << 8 | (g & 0xfc) << 3 | b >> 3

class GFXglyph:
    def __init__(self, bitmapOffset, width, height, xAdvance, xOffset, yOffset):
        self.bitmapOffset = bitmapOffset
        self.width = width
        self.height = height
        self.xAdvance = xAdvance
        self.xOffset = xOffset
        self.yOffset = yOffset

class GFXfont:
    def __init__(self, bitmap, glyph, first, last, yAdvance):
        self.bitmap = bitmap
        self.glyph = glyph
        self.first = first
        self.last = last
        self.yAdvance = yAdvance



class ILI9341:

    def __init__(self, RS, WR, RD, CS, RST, FIRST, r):
        self.RS = RS
        self.WR = WR
        self.RD = RD
        self.CS = CS
        self.RST = RST
        #self.FIRST = RST
        self.paral_sm = rp2.StateMachine (0, paral_prog, freq=20000000, out_base=Pin(FIRST))
        self.paral_sm.active(1)
        self._init_width = 320
        self._init_height = 240
        self.width = 320
        self.height = 240
        self.rotation = r
        self.CS.init(self.CS.OUT, value=1)
        self.RD.init(self.RD.OUT, value=1)
        self.WR.init(self.WR.OUT, value=1)
        self.CS(1)
        self.RD(1)
        self.WR(1)
        self.reset()
        self.CS(0)
        self.init()
        self._scroll = 0
        self._buf = bytearray(_CHUNK * 2)
        self._colormap = bytearray(b'\x00\x00\xFF\xFF') #default white foregraound, black background
        self._x = 0
        self._y = 0
        self.scrolling = False
        
    def swap(self,a, b):
        temp = b
        b = a
        a = temp
        return a, b

    def set_color(self,fg,bg):
        self._colormap[0] = bg>>8
        self._colormap[1] = bg & 255
        self._colormap[2] = fg>>8
        self._colormap[3] = fg & 255

    def set_pos(self,x,y):
        self._x = x
        self._y = y

    def reset_scroll(self):
        self.scrolling = False
        self._scroll = 0
        self.scroll(0)

    def set_font(self, font):
        self._font = font
        

        
    def ILI9341_WriteData(self, data):
        self.RS(1)
        self.paral_sm.put(data)   #tft_write_bus(data>>8,data&0x00ff)
        self.WR(0)
        self.WR(1)

    def ILI9341_WriteCommand(self, command):
        self.RS(0)
        self.paral_sm.put(command)   #tft_write_bus(data>>8,data&0x00ff)
        self.WR(0)
        self.WR(1)
        
    def SSD1289_Write_Com_Data(self,com1,dat1):

        self.ILI9341_WriteCommand(com1)
        self.ILI9341_WriteData(dat1)

        
    def ILI9341_SetAddressWindow(self,x1, y1, x2, y2):
        #self.swap(x1,y1)
        #self.swap(x2,y2)
        self.SSD1289_Write_Com_Data(0x0044,(y2<<8)+y1)
        self.SSD1289_Write_Com_Data(0x0045, x1)
        self.SSD1289_Write_Com_Data(0x0046, x2)
        self.SSD1289_Write_Com_Data(0x004E, y1)
        self.SSD1289_Write_Com_Data(0x004F, x1)
        self.ILI9341_WriteCommand(0x0022)
        

        

    def init(self):
        self.SSD1289_Write_Com_Data(0x0000,0x0001)
        time.sleep_ms(1)    
        self.SSD1289_Write_Com_Data(0x0003,0xA8A4)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x000C,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x000D,0x080C)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x000E,0x2B00)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x001E,0x00B0)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0001,0x293F)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0002,0x0600)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0010,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0011,0x6078)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0005,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0006,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0016,0xEF1C)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0017,0x0003)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0007,0x0233)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x000B,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x000F,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0041,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0042,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0048,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0049,0x013F)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x004A,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x004B,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0044,0xEF00)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0045,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0046,0x013F)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0030,0x0707)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0031,0x0204)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0032,0x0204)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0033,0x0502)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0034,0x0507)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0035,0x0204)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0036,0x0204)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0037,0x0502)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x003A,0x0302)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x003B,0x0302)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0023,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0024,0x0000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x0025,0x8000)
        time.sleep_ms(1)
        self.SSD1289_Write_Com_Data(0x004f,0)
        self.SSD1289_Write_Com_Data(0x004e,0)
        self.ILI9341_WriteCommand(0x0022)

    def reset(self):
        self.RST(0)
        time.sleep_ms(50)
        self.RST(1)
        time.sleep_ms(50)

    def ILI9341_FillRectangle(self,x, y, w, h, color): 
       self.ILI9341_SetAddressWindow(x, y, x+w-1, y+h-1)
       for i in range(h):
          for i in range(w):
              self.ILI9341_WriteData(color)
            
    def ILI9341_FillScreen(self,color):
          self.ILI9341_FillRectangle(0, 0, self.width, self.height, color)
          
          
    def ILI9341_DrawPixel(self, x, y, color):
          #self.CS(0)
          self.swap(x,y)
          self.SSD1289_Write_Com_Data(0x004E, y)
          self.SSD1289_Write_Com_Data(0x004F, x)
          self.SSD1289_Write_Com_Data(0x0022, color)
          #self.CS(1)
          
    def printchar(self,letter,xpos,ypos,size,color):
        origin = xpos
        charval = ord(letter)
        #print(charval)
        index = charval-32 #start code, 32 or space
        #print(index)
        character = cmap[index] #this is our char...
        rows = [character[i:i+5] for i in range(0,len(character),5)]
        #print(rows)
        for row in rows:
        #print(row)
            for bit in row:
                #print(bit)
                if bit == '1':
                    self.ILI9341_DrawPixel(xpos,ypos,color)
                    if size==2:
                        self.ILI9341_DrawPixel(xpos,ypos+1,color)
                        self.ILI9341_DrawPixel(xpos+1,ypos,color)
                        self.ILI9341_DrawPixel(xpos+1,ypos+1,color)
                xpos+=size
            xpos=origin
            ypos+=size
    
    def delchar(self,xpos,ypos,size):
        if size == 1:
            charwidth = 5
            charheight = 9
        if size == 2:
            charwidth = 10
            charheight = 18
        self.ILI9341_FillScreen(xpos,ypos,charwidth,charheight,color565(255, 255, 255)) #xywh



    def printstring(self,string,xpos,ypos,size,color):
        if size == 2:
            spacing = 14
        else:
            spacing = 8
        for i in string:
            self.printchar(i,xpos,ypos,size,color)
            xpos+=spacing


    def drawChar(self, x, y, ch, color):
        Barray = self._gfxBitmap
        Garray = self._gfxGlyph
        Goff = int((ord(ch) - self._gfxOrdFirstCh) * self._gfxGlylen)
        (bo,w,h,xa,xo,yo) = struct.unpack_from('iiiiii', Garray, Goff)
        
        bits = 0
        bit = 0
        #_orient = self.display.getOrientation()
        #self.display.setOrientation(_orient+2)
        y = self.display._maxY - y - 1      
        yy=0
        while yy<h: #for yy in range(h):
            xx=0
            while xx<w:
                if(not(bit & 7)):
                    bits = Barray[bo]
                    bo+=1
                bit+=1
                if(bits & 0x80):
                    x1 = x+xx+xo
                    x1=self.display._maxX - x1
                    self.ILI9341_DrawPixel(x1, y+yy+yo, color)
                bits <<= 1
                xx+=1
            yy+=1
        #self.display.setOrientation(_orient)
#        return xa
        return w
    
    def text(self, x, y, s, color):
        currx = x
        k = 0
        while k < len(s):
            currx += self.drawChar(currx, y, s[k], color) + 1
            k+=1
        return currx

