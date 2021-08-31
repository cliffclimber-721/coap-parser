packet = '0x48016da7'
scale = 16

print("Packet in hex :", packet)

bin_packet = bin(int(packet, scale)).zfill(8)
print("Result :",str(bin_packet))
print("Length :", len(str(bin_packet[2:])))
print('Version :', bin_packet[2:3])
print("Token Length :", bin_packet[5:8])

print('Type :', bin_packet[3:4],', in decimal :', int(bin_packet[3:4]))
pkt = int(bin_packet[3:4])
if pkt == 0:
    print(pkt, ", CONfirmable")
elif pkt == 1:
    print(pkt, ", NON-confirmable")
elif pkt == 2:
    print(pkt, ", ACKnowledgement")
elif pkt == 3:
    print(pkt, ", ReSeT")
else:
    print("Another Messages Types")

print("Method Code :", bin_packet[10:17])
mtd = int(bin_packet[10:17])

if mtd == 0:
    print(mtd, "EMPTY")
elif mtd == 1:
    print(mtd, ", GET")
elif mtd == 2:
    print(mtd, ", POST")
elif mtd == 3:
    print(mtd, ", PUT")
elif mtd == 4:
    print(mtd, ", DELETE")
else:
    print("Another Method Code")

print("Message ID :", bin_packet[18:])