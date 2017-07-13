# Mini Des algorith with mode of operation cbc
# python version 3.3.0
# referances
# http://stackoverflow.com/
# https://www.cs.uri.edu/cryptography/dessimplified.htm
# skeleton ModesOfOperation.py
# coded by student Name: Prachi Goel
# student ID: 1001234789

import sys
import datetime


class MiniDes:
    def __init__(self):
        print("        'Mini DES Ecryption with mode OFB'      ")
        print(' Coded by: \n student Name: Prachi Goel \n student ID: 1001234789')

    # Taking the input from the users
    def user_input(self):
    # taking user input for Student Name
        ciphertext = input("'Please enter the 11 block ciphertext to be decrypted: ")
    # check for the length: student name to be equal to 10, if less than 10 exit the program
        if len(ciphertext) != 132:
            print("'The ciphertext entered is not correct: expected 132 characters got less/more'")
            sys.exit()
        elif len(ciphertext)==132:
            try:
                int(ciphertext,2)
            except ValueError:
                print("'Entered input is not binary'")
                sys.exit()
        else:
            print ("input accepted")
        return ciphertext

    def IV(self):
        self.iv=input("Please enter 2 alphabets for initialisation vector example 'ac' etc: ")
        if len(self.iv)!=2:
            print("The value of initialization vactor is not valid expected 2 letters got less/more ")
            sys.exit()
        return self.iv

    def letters_to_binary(self, alphabets):
        # letter conversion to 6 bit
        name_binary = ""
        for i in range(0, len(alphabets)):
            name_binary += format((ord(alphabets[i]) - ord('a') + 1), '06b')
        return name_binary


    def date_of_birth(self):
        dob = input("'Please enter the date of birth in YYYY.MM.dd': ")
        date_format = '%Y.%m.%d'
        try:
            date_input = datetime.datetime.strptime(dob, date_format)
            time_tuple = date_input.timetuple()
            return (time_tuple.tm_yday)
        except ValueError:
            print('date of birth is not valid')
            sys.exit()

    def date_to_binary(self, Jdate):
        date_binary = ""
        date_binary = bin(Jdate)[2:].zfill(9)
        return date_binary

#Dividing the message into blocks
    def dividing_ciphertext_to_block(self, message):
        n = 12
        block = [message[i:i + n] for i in range(0, len(message), n)]
        return block

#taking the value of L0 for the block
    def encryp_step1_L0(self, blocki):
        L0 = (blocki[:6])
        print('L: ',L0)
        return L0

#taking the value of R0 for the block
    def encryp_step1_R0(self, blocks):
        R0= (blocks[6:])
        print('R: ',R0)
        return R0

#key for round 1
    def key_round1(self, binary_date):
        key1 = binary_date[0:8]
        return key1

#key for round 2
    def key_round2(self, binary_date):
        key2 = binary_date[1:9]
        return key2


#Expansion of R0
    def R0_expansion(self, R0):
        eR0 = ""
        eR0 += R0[0]
        eR0 += R0[1]
        eR0 += R0[3]
        eR0 += R0[2]
        eR0 += R0[3]
        eR0 += R0[2]
        eR0 += R0[4]
        eR0 += R0[5]
        print('E(R):',eR0)
        return (eR0)

# Xoring the key with R0
    def XOR_R0_Key(self, R0, key):
        FRK = int(R0, 2) ^ int(key, 2)
        # padding values for func
        func = format(FRK, '08b')
        print ('Result of R0 XOR KEY1: ',func)
        return func

#getting the values from S boxes
    def Checking_Sbox(self, func):
# intialising the Sbox1.
        s1_row0 = ['101', '010', '001', '110', '011', '100', '111', '000']
        s1_row1 = ['001', '011', '110', '010', '000', '111', '101', '011']

        # Getting the value from Sbox1
        S1 = func[:4]
        if S1[0] == '0':
            b = int(S1[1] + S1[2] + S1[3], 2)
            S1_value = s1_row0[b]
        else:
            b = int(S1[1] + S1[2] + S1[3], 2)
            S1_value = s1_row1[b]

# intialising the Sbox2.
        s2_row0 = ['100', '000', '110', '101', '111', '001', '011', '010']
        s2_row1 = ['101', '011', '000', '111', '110', '010', '001', '100']

        # Getting the value from Sbox2
        S2 = func[4:]
        if S2[0] == '0':
            b = int(S2[1] + S2[2] + S2[3], 2)
            S2_value = s2_row0[b]
        else:
            b = int(S2[1] + S2[2] + S2[3], 2)
            S2_value = s2_row1[b]
# computing f(R0,K1)
        Value_after_Sbox = S1_value + S2_value
        print('Value after Sbox is: ',Value_after_Sbox)
        return Value_after_Sbox

# computing (f(R0,K1) XOR L0)
    def XOR_Sbox_L_to_find_R(self, Sbox, L0):
        R_value = int(Sbox, 2) ^ int(L0, 2)
        # encrypted block as R0L0-value
        Ri = format(R_value, '06b')
        print('New value of R: ',Ri,'\n')
        return Ri

    def plaintext_conversion(self,plaintext):
        y=6
        characters=[plaintext[i:i + y] for i in range(0, len(plaintext), y)]
        print ("the characters are: ", characters)
        return characters

    def original_message(self,characters):
        message = ""
        for i in range (0, len(characters)):
            decoded_literal=""
            equi_number=int(characters[i],2)
            if equi_number>0 and equi_number<27:
                decoded_literal=chr((equi_number-1)+ord('a'))
            elif equi_number>26 and equi_number<37:
                decoded_literal = chr((equi_number-27)+ord('0'))
            elif equi_number==37:
                decoded_literal=chr(equi_number+9)
            elif equi_number==38:
                decoded_literal=chr(equi_number-6)
            message+=decoded_literal
        return message

        # Xoring the IV with the block of plain text

    def XOR_IV_Block(self, iv, blocks):
        IV_XOR_Block = int(iv, 2) ^ int(blocks, 2)
        IV_XOR_Block_result = format(IV_XOR_Block, '012b')
        return IV_XOR_Block_result

def Decryption():
    decryption = MiniDes()
    ciphertext = decryption.user_input()
    Jdate = (decryption.date_of_birth())
    iv = decryption.IV()
    # binary conversion of string,number,date,dot and space
    binary_date = decryption.date_to_binary(Jdate)
    binary_iv= decryption.letters_to_binary(iv)
# Initialising the key
    key = []
    key.append(decryption.key_round1(binary_date))
    key.append(decryption.key_round2(binary_date))
# Stream of data to be decrypted
    blocks = decryption.dividing_ciphertext_to_block(ciphertext)
    print ("Message is divided into following blocks: \n", blocks)
    # dividing message into blocks
    plaintext = ""
    # initializing Oj with IV
    Oj = binary_iv
    for i in range(0, len(blocks)):
        print("Block is ", i + 1, ": '", blocks[i])
        print("Oj for block ", i + 1, ": '", Oj)
        # Oj=Ek(Ij)
        for j in range(0, len(key)):
            # 2 round encryption for each block of plaintext
            print('Key is: ', key[j])
            L = decryption.encryp_step1_L0(Oj)
            R = decryption.encryp_step1_R0(Oj)
            Expanded_R = decryption.R0_expansion(R)
            Func_R_K = decryption.XOR_R0_Key(Expanded_R, key[j])
            Sbox = decryption.Checking_Sbox(Func_R_K)
            decrypted_message_Ri = decryption.XOR_Sbox_L_to_find_R(Sbox, L)
            print("new value of L is ", R)
            Result_Round = (R + decrypted_message_Ri)
            Oj = Result_Round
        Oj = (decrypted_message_Ri + R)

        # Cj=Pj XOR Oj

        Decrypted_Block = decryption.XOR_IV_Block(blocks[i], Oj)
        print("'Decryption of block ",i+1," at the end of 2 round of decryption given by RiLi: '", Decrypted_Block, '\n\n\n')
        plaintext+=Decrypted_Block
    print('Plaintext: ', plaintext, '\n')
    characters = decryption.plaintext_conversion(plaintext)
    decipher_message= decryption.original_message(characters)
    print("original message was: ", decipher_message)