alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text,shift_amount,typrOfencryption):
    outputText=""

    if typrOfencryption == 'decode':
        shift_amount *= -1

    for x in original_text:
        if x not in alphabet:
            outputText +=x
        elif x in alphabet:
            shifted_position=alphabet.index(x)+shift_amount
            shifted_position %= len(alphabet)
            outputText+=alphabet[shifted_position]
    print(outputText)
    
should_continue= True

while should_continue:
    direction=input("Type 'encode' to encrypt, type 'deecode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    restart=input("Type 'yes' if you want to go. Otherwise 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Ok Bye")



















# def encrypt(message,shiftNum):
#     encodedMessage=""
#     for x in message:
#         shifted_position=alphabet.index(x)+shiftNum
#         shifted_position %= len(alphabet)
#         encodedMessage+=alphabet[shifted_position]
#     print(encodedMessage)
# def dencrypt(message,shiftNum):
#     decodedMessage=""
#     for x in message:
#         shifted_position=alphabet.index(x)-shiftNum
#         shifted_position %= len(alphabet)
#         decodedMessage+=alphabet[shifted_position]
#     print(decodedMessage)

# def caesar(original_text,shift_amount,typeOfEncryption):
#     if(typeOfEncryption=='encode'):
#         encrypt(original_text,shift_amount)
#     elif(typeOfEncryption=='decode'):
#         dencrypt(original_text,shift_amount)