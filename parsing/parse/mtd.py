from parse import *

mtd = bin_packet[10:17]

#class method_code():
#    def mtd_0(self):
#        if mtd == 0:
#            print("0, EMPTY")

#    def mtd_1(self):
#        if mtd == 1:
#            print("1, GET")

#   def mtd_2(self):
#        if mtd == 2:
#            print("2, POST")

#    def mtd_3(self):
#        if mtd == 3:
#            print("3, PUT")

#    def mtd_4(self):
#        if mtd == 4:
#            print("4, DELETE")

def mtd_code(num_m):
    mtd_num = {"0" : "EMPTY", "1" : "GET", "2" : "POST", "3" : "PUT", "4" : "DELETE"}.get(num_m, "Another type")
    print(f"{mtd_num}")