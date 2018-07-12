# use to encrypt a message
# parameters are:
#  the message to be encrypted
#  the bitmap file to use to hide the message
#  the name of the new file you want to produce
def encrypt_message(message, infilename, outfilename):
    # make the file handles using binary modes ("rb" and "wb")
    infilehandle = open(infilename, "rb")
    outfilehandle = open(outfilename, "wb")

    # get all the binary data into a list
    binarydata = bytearray(infilehandle.read())

    # skip over the header data and start with the 63rd byte
    changebyte = 63
    
    for letter in message:
        binarydata[changebyte] = ord(letter)
        changebyte += 16

    # write the encrypted data to the new file
    outfilehandle.write(binarydata)

    # close the files
    infilehandle.close()
    outfilehandle.close()

encrypt_message("Secret message", "bunny.bmp", "newbunny.bmp")

