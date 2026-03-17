import struct

def solve():
    print("[*] Reading target.bin...")
    try:
        with open("target.bin", "rb") as f:
            raw_data = f.read()
    except FileNotFoundError:
        print("[-] ERROR: target.bin not found! Please dump it using GDB.")
        return

    num_pixels = len(raw_data) // 24
    print(f"[*] Total pixels detected: {num_pixels}")

    # Calculate length and width automatically based on the number of pixels
    valid_dims = []
    for w in range(1, 256):
        if num_pixels % w == 0:
            h = num_pixels // w
            if h <= 255:
                width = w
                height = h
                break
   
    print(f"[*] Dimensions: Width={width}, Height={height}")

    pixels = []
    for i in range(num_pixels):
        chunk = raw_data[i*24 : (i+1)*24]
        r = int(chunk[7:10])
        g = int(chunk[11:14])
        b = int(chunk[15:18])
        char = chunk[19:20]
        pixels.append({'r': r, 'g': g, 'b': b, 'char': char})

    print("[*] Compressing data using directive 59586...")
    directives_data = b''
    num_directives = 0

    # Compression algorithm: Combines adjacent (non-empty) pixels into a single line
    for y in range(height):
        x = 0
        while x < width:
            idx = y * width + x
            if pixels[idx]['char'] != b' ':
                start_x = x
                block = []
                # Continue reading until you find a blank space or the line ends.
                while x < width and pixels[y * width + x]['char'] != b' ':
                    block.append(pixels[y * width + x])
                    x += 1
                
                # Call Directive 59586 for this group
                w_rect = x - start_x  # width  of rectangle
                h_rect = 1            # height of rectangle
                
                dir_code = struct.pack('<H', 59586)
                coords = struct.pack('<BBBB', start_x, y, w_rect, h_rect)
                pix_data = b''.join([struct.pack('<BBBB', p['r'], p['g'], p['b'], ord(p['char'])) for p in block])
                
                directives_data += dir_code + coords + pix_data
                num_directives += 1
            else:
                x += 1

    # Main Header
    header = struct.pack('<4shbbI', b'cIMG', 3, width, height, num_directives)
    Final_Data = header + directives_data

    # Saving File
    with open("solution.cimg", "wb") as f:
        f.write(Final_Data)

    print(f"[+] Generated 'solution.cimg'")
    print(f"[+] Number of Directives used: {num_directives}")
    print(f"[+] Final File Size: {len(Final_Data)} bytes ")

    if len(Final_Data) > 1340:
        print("[-] WARNING: Size is still above 1340!")
    else:
        print("[*] Done!")

if __name__ == "__main__":
    solve()
