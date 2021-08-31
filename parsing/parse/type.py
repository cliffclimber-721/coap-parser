from parse import *
pkt = bin_packet[3:4]

#class type():
#    def type_0(self):
#        if pkt == 0:
#            print("0, CONfirmable")

#   def type_1(self):
#       if pkt == 1:
#            print("1, NON-confirmable")

#    def type_2(self):
#        if pkt == 2:
#            print("2, ACKnowledgement")

#    def type_3(self):
#        if pkt == 3:
#            print("3, ReSeT")
def type(num_t):
    type_num = {"0" : "CONfirmable", "1" : "NON-confirmable", "2" : "ACKnowledgement", "3" : "ReSeT"}.get(num_t, "Another type")
    print(f"{type_num}")