import struct 

magic_number = b"cIMG"  # 4 bytes
version = 2   # 2 bytes
width  = 41   # 2 bytes
height = 22   # 2 bytes

header = struct.pack("<4shhh",magic_number, 
  version, width, height)


ascii_size = (width * height)
Full_data_size = (width * height * 4)

r = 140
g = 29
b = 64
asciii= 38

# datas = [r, g , b , asciii]

datas = struct.pack("BBBB", r, g, b, asciii)
# d = [datas[i: i + 4] for i in range(0, Full_data_size, 4)]
data = datas * ascii_size

Final_data = header + data


with open("File_name", "wb") as file: 
  file.write(Final_data)

  
"""
d = []
i = 0 
while (i < ascii_size):
    d.append(datas)
    i += 1
print(d)
"""
"""
temp_list = []
k = 0
for i in data:
  for k in range(4):
    temp_list.append(i[k])
""" 

