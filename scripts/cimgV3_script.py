import struct

with open("/path/outputt.bin", "rb") as file:
        raw_memory = file.read()

#raw_memory = b"\x1b[38;2;255;255;255m.\x1b[0m"  #temp value to dump the memory
pixel_data = b""
pixel_count = 0

for i in range(0, len(raw_memory), 24):
        chunk = raw_memory[i : i + 24]

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

directive_code = 60539
directive_code_bytes = directive_code.to_bytes(2, "little")
data = directive_code_bytes + pixel_data

for w in range(1, 256):
        if pixel_count % w == 0:
                h = pixel_count // w
                if h <= 255:
                        width = w
                        height = h
                        break

magic_word = b"cIMG"
version = 3
remaining_directives = 1
header = struct.pack("<4shBBi", magic_word, version, width, height, remaining_directives)

with open("7DC.cimg", "wb") as f :
        f.write(header + data)
