def encode(cypher, shift):
    change = list(cypher)
   #print(change)
    coded = []
    for letter in change:
       if letter.isupper() == True:
           if ord(letter) + shift > 90:
               letter = chr(64 + (ord(letter) + shift - 90)) 
               #print('1')
           else:
               letter = chr(ord(letter) + shift)
               #print('2')
       else:
           if ord(letter) + shift > 122:
               letter = chr(96 + (ord(letter) + shift - 122))
               #print('3') 
           else:
               letter = chr(ord(letter) + shift)
               #print('4')
               #print(letter)
       coded.append(letter)
    return("".join(coded) + " with a shift of " + str(shift) + " :ENCODED")

def decode(cypher, shift):
    change = list(cypher)
    #print(change)
    coded = []
    for letter in change:
       if letter.isupper() == True:
           if ord(letter) - shift < 65:
               letter = chr(90 - (65 - ord(letter - shift))) 
               #print('1')
           else:
               letter = chr(ord(letter) - shift)
               #print('2')
       else:
           if ord(letter) + shift > 122:
               letter = chr(122 - (96 - ord(letter - shift))) 
               #print('3') 
           else:
               letter = chr(ord(letter) - shift)
               #print('4')
               #print(letter)
       coded.append(letter)
    return("".join(coded) + " with a shift of " + str(shift) + " :DECODED")

print(encode("Hello", 5))
print(decode("Mjqqt", 5))