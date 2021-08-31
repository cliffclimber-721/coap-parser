global bin_packet
bin_packet = bin(int(packet, scale)).zfill(8)
class type_comp:
    global bin_packet
    global pkt
    pkt = int(bin_packet[3:4])

    def type_0(self):
        if pkt == 0:
            print("0, CONfirmable")

    def type_1(self):
        if pkt == 1:
            print("1, NON-confirmable")

    def type_2(self):
        if pkt == 2:
            print("2, ACKnowledgement")

    def type_3(self):
        if pkt == 3:
            print("3, ReSeT")

t=type_comp()

class coap():
    def __init__(self):
        packet = input(">>")
        print(packet)
        scale = 16
        global bin_packet
        bin_packet = bin(int(packet, scale)).zfill(8)

        print("Packet in hex :", packet)
        print("Result :", bin_packet)

    def version(self):
        print("Version :", bin_packet[2:3])

    def length(self):
        print("Token Length :", int(bin_packet[5:8]))

    def type(self):
        pkt = int(bin_packet[3:4])
        print('Type :', bin_packet[3:4], ', in decimal :', pkt)
        print(t.type_0())
        print(t.type_1())
        print(t.type_2())
        print(t.type_3())

    def mtd_code(self):
        print("Method Code :", bin_packet[10:17])
        method = ["0, EMPTY", "1, GET", "2, POST", "3, PUT", "4, DELETE"]
        mtd = int(bin_packet[10:17])

        if mtd == method[0]:
            print(method[0])
        elif mtd == method[1]:
            print(method[1])
        elif mtd == method[2]:
            print(method[2])
        elif mtd == method[3]:
            print(method[3])
        else:
            None

    def msg_id(self):
        print("Message ID :", bin_packet[18:])


c=coap()
c.version()
c.length()
c.type()
c.mtd_code()
c.msg_id()