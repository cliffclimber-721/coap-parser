from parse import *
import parse as p
from parse.type import pkt
from parse.mtd import mtd


class coap_parsing():
    def length(self):
        print("Token Length :", bin_packet[5:8])

    def version(self):
        print("Version :", bin_packet[2:3])

    def type(self):
        print('Type :', bin_packet[3:4], ', in decimal :', pkt)
        p.type()

    def mtd_code(self):
        print("Method Code :", bin_packet[10:17])
        p.method_code()

    def msg_id(self):
        print("Message ID :", bin_packet[18:])

c = coap_parsing()

c.length()
c.version()
c.type()
c.mtd_code()
c.msg_id()