import struct
with open("challenges_files/output.bin", "rb") as file:
    raw_memory = file.read()


pixel_data = b""
pixel_count = 0
for i in range(0, len(raw_memory), 24):
    chunk = raw_memory[i: i+24]
    
    
    if len(chunk) < 24 or not chunk.startswith(b"\x1b[38;2;"):
        break
   
    try:    
        r = int(chunk[7:10])
        g = int(chunk[11:14])
        b = int(chunk[15:18])
        char = int(chunk[19])
    except Exception as e:
        break
    
    pixel_data += struct.pack("<BBBB", r, g, b, char)
    pixel_count += 1


for w in range(1,256):
    if pixel_count % w == 0 :
        h = pixel_count // w
        if h <= 255:
            width = w 
            height = h
            break 


magic_word = b"cIMG"
version = 0x02

header = struct.pack("<4shBB", magic_word, version, width, height)

with open("6DC.cimg", "wb") as f:
    f.write(header + pixel_data)

