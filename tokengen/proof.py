import pyscrypt
import binascii

hashed = pyscrypt.hash(password = str.encode("correct horse battery staple"),
                       salt = str.encode("seasalt"),
                       N = 1024,
                       r = 1,
                       p = 1,
                       dkLen = 16)
hexhash=binascii.hexlify(hashed).decode("utf-8")
print (hexhash)
print("The hash is: %d" % int(hexhash, 16))

#for()
