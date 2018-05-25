#!/usr/bin/python
from collections import defaultdict

# 16 color
color = {
  '\n':'\x1b[0m',
  'y': '\x1b[43m',
  'b': '\x1b[43m',
  'd': '\x1b[40m',
  'g': '\x1b[42m',
  ' ': '\x1b[0m',
  'x': '\x1b[47m',
}

# 16M color
color = {
  '\n':'\x1b[0m',
  'y': '\x1b[48;2;229;198;45m',
  'b': '\x1b[48;2;128;74;2m',
  'd': '\x1b[48;2;57;33;5m',
  'g': '\x1b[48;2;75;146;0m',
  ' ': '\x1b[48;2;25;23;16m',
  'x': '\x1b[47m',
}

char = defaultdict(lambda: ' ')
char['\n'] = '\n'

img = '''                                
                                
       xxx x xx xxx  x  x       
       x x x x   x  x x x       
       xx  x  x  x  x x x       
       x   x  x  x  x x x       
       x   x xx  x   x   x      
                                
                                
        gg g            g       
       ggggg            gg      
        gg              g       
        gg              g       
      yyyyyy    yy      g  yy   
    yyyyyybyyyyyyyyyyyyyyyybby  
yyyyyybbybbbbyyyyyyyyyyyyybbbyyy
yyyybbbbdddddybbbbybbbbbbbbbbbyy
bbbbbbddd    ddddbbddddddddddbbb
dddddd           dd         dddb
'''

print ''.join((color[this] if color[this] != color[prev] else '') + char[this] for this, prev in zip(img, '\n'+img))
