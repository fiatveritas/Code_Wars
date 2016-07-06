import string
def encryptor(key, message):
    #Program me!
    if len(message) == 0:
        return message
    else: 
        n = 0
        new_string = ''
        pos_letter = None
        while( n < len(message)):
            letter_pos = ord(message[n])
            if letter_pos >= 65 and letter_pos <= 90:
            	letter_pos += key
            	while(not(letter_pos >= 65 and letter_pos <= 90)):
            		letter_pos %= 26
                print(unichr(letter_pos))
            n += 1
        return new_string
    #print(message)
    #print(new_string)
    #return new_string

#print(encryptor(13, ''))
#print(encryptor(13, 'Caesar Cipher')) #'Pnrfne Pvcure'
print(encryptor(-5, 'Hello World!')) #'Czggj Rjmgy!'
#print(encryptor(27, 'Whoopi Goldberg') #'Xippqj Hpmecfsh'
#print(encryptor(39, "T")) #'G
#print('ABV'.isupper())
