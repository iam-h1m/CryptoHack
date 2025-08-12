from Crypto.Util.number import long_to_bytes
#ciphertext from output file
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
#in the script provided n greater than pt because the exponent is only 1. This will not change
#pt as a result as it stays the same. This is dangerous as pt is less than n which now
#makes pt % n ineffective leaving pt unaltered so ct = pt^1 mod n = pt mod n = pt
print(long_to_bytes(ct))