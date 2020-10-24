primarymessage = input()
modifiedmessage = input()

zerokeypoint = modifiedmessage[:2]
zerokeypoint = int(zerokeypoint, 16)

spacevalue = 0x20
key = zerokeypoint ^ spacevalue
modifiedmessage = modifiedmessage[2:]
answer = hex(key)[2:]

for i in range(0, int(len(modifiedmessage)/2)):
    msg = int(primarymessage[:2], 16)
    primarymessage = primarymessage[2:]
    primmsg = key ^ msg

    msg = int(modifiedmessage[:2], 16)
    modifiedmessage = modifiedmessage[2:]

    key = primmsg ^ msg
    if len(hex(key)[2:]) == 1:
        answer = answer + '0' + hex(key)[2:]
    else:
        answer = answer + hex(key)[2:]

print(answer.upper())
