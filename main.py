"""
HOSSEIN JALILI
#HO3J
Convert numeric bases in Python
main.py
mehr 1400
ver 1.0
"""


################import###############
import numeric_bases as nb
import os

################lambda###############
clear=lambda : os.system("cls")

################main###############

clear()
while True:
    try:
        print("""
                 Convert numeric bases
        |*************************************|
        |   1 :  input Decimal to convert     |
        |   2 :  input Binary to convert      |
        |   3 :  input Octal to convert       |
        |   4 :  input Hexadecimal to convert |
        |   5 :  quit app                     |
        ***************************************
        """)
        i=int(input("Enter number of Convert numeric bases :\t"))
        if i ==1:
            nb._dec()
        elif i==2:
            nb._bin()
        elif i==3:
            nb._oct()
        elif i==4:
            nb._hex()
        elif i==5:
            break
        else :
            clear()
            print("wrong  number !!! " ,end="\n \n")
            print( end=" ")
            qq = input("Enter 'Q' to quit app \n or 'Enter' to continue : \t ").lower()
            if qq =="q" :
                break
            else :
                clear()
                continue
    except:
        clear()
        print("Enter number !")

        