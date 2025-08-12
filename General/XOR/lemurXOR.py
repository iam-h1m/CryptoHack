from PIL import Image
from pwn import *
#i load in the images. The bits of these images are xor'ed with each other to create the end result
pic1 = Image.open("lemur.png")
pic2 = Image.open("flag.png")

result_bytes = xor(pic1.tobytes(), pic2.tobytes())
result = Image.frombytes(pic2.mode, pic2.size, result_bytes)

result.save('xor_result.png')