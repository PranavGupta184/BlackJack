def encode(msg, shf):
    msg1=""
    for i in msg:
        if i == " ":
            msg1+=" "
        else:
            msg1+=chr(ord(i)+shf)
    return msg1
def decode(msg,shf):
    d_msg=""
    for y in msg:
        if y ==" ":
            d_msg+=" "
        else:
            d_msg+=chr(ord(y)-shf)
    return d_msg
def choice():
    logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
    print(logo)
    inp3='y'
    while inp3=='y':
        inp=input("Type 'encode' to encrypt, 'decode' to decrypt.")
        inp=inp.lower()
        if inp=='encode':
            message=input("Type the message to be encoded - ")
            shift=int(input("Enter the shift number - "))
            shift=shift%26
            encoded_message= encode(message, shift)
            print(f"Here's the encoded message, {encoded_message}")
            inp3=input("Do you wish to enter again? (Y - Yes/N - No)")
            inp3=inp3.lower()
        elif inp=='decode':
            message=input("Type the encoded message - ")
            shift=int(input("Type the shift number - "))
            shift=shift%26
            decoded_message = decode(message, shift)
            print(f"Here's the decoded message, {decoded_message}")
            inp3=input("Do you wish to enter again? (Y - Yes/N - No)")
            inp3=inp3.lower()
        else:
            print("Wrong Input")
            inp3=input("Do you wish to enter again? (Y - Yes/N - No)")
            inp3=inp3.lower()
choice()
