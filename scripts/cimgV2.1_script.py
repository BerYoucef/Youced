import struct
magic_word = b"cIMG"
version = 0x02
width = 0x02
height = 0x02

header = struct.pack("<4shbb", magic_word, version, width, height)
"""
r1 = 49
g1 = 196
b1 = 198
a1 = b"c"
r2 = 92
g2 = 167
b2 = 123
a2 = b"I"
r3 = 89
g3 = 7
b3 = 16
a3 = b"M"
r4 = 244
g4 = 63
b4 = 16
a4 = b"G"

d1 = struct.pack("BBB1s", r1,g1,b1,a1)
d2 = struct.pack("BBB1s", r2,g2,b2,a2)
d3 = struct.pack("BBB1s", r3,g3,b3,a3)
d4 = struct.pack("BBB1s", r4,g4,b4,a4)
"""


data = b""
pixels = [(49,196,198,ord('c')), (92,167,123,ord('I')),(89,7,16,ord('M')),(244,63,16,ord('G'))]

for r,g,b,char in pixels:
        data += struct.pack("BBBB", r,g,b,char)


with open("6dC.cimg", "wb") as file:
        file.write(header + data)


