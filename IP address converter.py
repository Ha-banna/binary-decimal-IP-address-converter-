#! python3
from sys import *

def decimal_convert(part):
    total = int(part)
    end = list('00000000')
    string =""
    if total - 128 >= 0:
        del end[0]
        end.insert(0,'1')
        total = total - 128
    if total - 64 >= 0:
        del end[1]
        end.insert(1,'1')
        total = total - 64
    if total - 32 >= 0:
        del end[2]
        end.insert(2,'1')
        total = total - 32
    if total - 16 >= 0:
        del end[3]
        end.insert(3,'1')
        total = total - 16
    if total - 8 >= 0:
        del end[4]
        end.insert(4,'1')
        total = total - 8
    if total - 4 >= 0:
        del end[5]
        end.insert(5,'1')
        total = total - 4
    if total - 2 >= 0:
        del end[6]
        end.insert(6,'1')
        total = total - 2
    if total - 1 >= 0:
        del end[7]
        end.insert(7,'1')
        total = total - 1

    for i in range(len(end)):
        string = string + end[i]
    return string

def binary_convert(part):
    total = 0
    if part[0] == '1':
        total += 128
    if part[1] == '1':
        total += 64
    if part[2] == '1':
        total += 32
    if part[3] == '1':
        total += 16
    if part[4] == '1':
        total += 8
    if part[5] == '1':
        total += 4
    if part[6] == '1':
        total += 2
    if part[7] == '1':
        total += 1
    return total

dob = input("Is your current IP address in binary or decimal form\n")
ldob = dob.lower()
ip = str(input("please type IP address here:\n"))

#binary to decimal
if ldob == "binary":
    binary = ip.split(".")
    if len(binary) == 4:
        for i in range(len(binary)):
            if len(binary[i]) == 8:
                continue
            else:
                print("there was an error, please check the IP address you entered and run again")
                exit()
        p1 = binary_convert(binary[0])
        p2 = binary_convert(binary[1])
        p3 = binary_convert(binary[2])
        p4 = binary_convert(binary[3])
        print('binary to decimal conversion: '+str(p1)+'.'+str(p2)+'.'+str(p3)+'.'+str(p4))
    else:
        print("there was an error, please check the IP address you entered and run again")
        exit()

#decimal to binary      
elif ldob == "decimal":
    decimal = ip.split(".")
    if len(decimal) == 4:
        for i in range(len(decimal)):
            if int(decimal[i]) <= 255:
                continue
            else:
                print("there was an error, please check the IP address you entered and run again")
                exit()
        p1 = decimal_convert(decimal[0])
        p2 = decimal_convert(decimal[1])
        p3 = decimal_convert(decimal[2])
        p4 = decimal_convert(decimal[3])
        print('decimal to binary conversion: '+str(p1)+'.'+str(p2)+'.'+str(p3)+'.'+str(p4))
    else:
        print("there was an error, please check the IP address you entered and run again")
        exit()
else:
    print("type in binary or decimal")
