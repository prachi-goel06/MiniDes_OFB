import subprocess
import EncryptionMiniDesOFB
import DescryptionMiniDesOFB
import os
import sys

def hangon():
    YN=input("Do you want to continue Y/N: ")
    if YN=='Y' or YN=='y':
        option()
    elif YN=='N' or YN=='n':
        sys.exit()
    else:
        print("Invalid command")

def option():
    Option= input("Please choose between Encryption/Decrypyion \n Enter E for Encryption or D for Decyption: ")
    if Option=='E':
        EncryptionMiniDesOFB.Encryption()
        hangon()
    elif Option=='D':
        DescryptionMiniDesOFB.Decryption()
        hangon()
    else:
        print("User entered invalid input")

if __name__ == '__main__':
    print("        'Mini DES Ecryption'      ")
    print(' Coded by: \n student Name: Prachi Goel \n student ID: 1001234789')
    option()
