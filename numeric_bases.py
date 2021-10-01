
"""
HOSSEIN JALILI
#HO3J
Convert numeric bases in Python
numeric_bases.py
mehr 1400
ver 1.0
"""

################import###############
import os

################operation###############
clear=lambda : os.system("cls")


def _dec():
    clear()
    try:
        num=int(input("enter number as 10_base :\t"))
        print( "your 'dec' number  : \t\t",(num))
        print("_____________________________________")
        print(num, "----> in Binary : \t\t", str(bin(num)).lstrip('0b'))
        print(num, "----> in Octal : \t\t", str(oct(num)).lstrip('0o'))
        print(num, "----> in decimal : \t\t", str(num))
        print(num, "----> in Hexadecimal : \t", str(hex(num)).lstrip('0x'))
        print("_____________________________________")
        print()
    except:
        print( " enter true value !!! ")

    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()
 

def _bin():
    clear()
    try:
        num=int(input("enter number as 2_base :\t"))
        number=int(str(num), 2)
        print( "your 'bin' number  : \t\t",(num))
        print("_____________________________________")
        print(num, "----> in Binary : \t\t", str(bin(number)).lstrip('0b'))
        print(num, "----> in Octal : \t\t", str(oct(number)).lstrip('0o'))
        print(num, "----> in decimal : \t", str(number))
        print(num, "----> in Hexadecimal : \t", str(hex(number)).lstrip('0x'))
        print("_____________________________________")    
        print()
    except:
        print( " enter true value !!! ")
    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()
 

def _oct():
    clear()
    try:
        num=int(input("enter number as 8_base :\t"))
        number=int(str(num), 8)
        print( "your 'oct' number  : \t\t",(num))
        print("_____________________________________")
        print(num, "----> in Binary : \t\t", str(bin(number)).lstrip('0b'))
        print(num, "----> in Octal : \t\t", str(oct(number)).lstrip('0o'))
        print(num, "----> in decimal : \t\t", str(number))
        print(num, "----> in Hexadecimal : \t", str(hex(number)).lstrip('0x'))
        print("_____________________________________")    
        print()
    except:
        print( " enter true value !!! ")
    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()
 

def _hex():
    clear()
    try:
        num=input("enter number as 16_base :\t")
        number=int(str(num), 16)
        print( "your 'hex' number  : \t\t",(num))
        print("_____________________________________")
        print(num, "----> in Binary : \t\t", str(bin(number)).lstrip('0b'))
        print(num, "----> in Octal : \t\t", str(oct(number)).lstrip('0o'))
        print(num, "----> in decimal : \t\t", str(number))
        print(num, "----> in Hexadecimal : \t", str(hex(number)).lstrip('0x'))
        print("_____________________________________")    
        print()
    except:
        print( " enter true value !!! ")
    ex = input("\nInput Enter to back to menu \nInput 'any key' then Enter to 'clear' and back to menu \n")
    if not ex =="" : 
        clear()
 



