primarymessage = input()  # Getting two lines - without and with space
modifiedmessage = input()

zerokeybyte = modifiedmessage[:2]  # Zerokeybyte is used to decrypt 'space' from second message
modifiedmessage = modifiedmessage[2:]
zerokeybyte = int(zerokeybyte, 16)

spacevalue = 0x20  # As we know 'space' position - we can get first key byte for further decrypting
key = zerokeybyte ^ spacevalue
answer = hex(key)[2:]

for i in range(0, int(len(modifiedmessage)/2)):  # Loop for getting next piece of key using previous one
    encrmsg = int(primarymessage[:2], 16)
    primarymessage = primarymessage[2:]
    decrmsg = key ^ encrmsg

    encrmsg = int(modifiedmessage[:2], 16)
    modifiedmessage = modifiedmessage[2:]

    key = decrmsg ^ encrmsg
    if len(hex(key)[2:]) == 1:
        answer = answer + '0' + hex(key)[2:]
    else:
        answer = answer + hex(key)[2:]

print(answer.upper())  # Formatting answer to upper key as it required for the task

