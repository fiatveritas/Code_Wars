import string
def encryptor(key, message):
    #Program me!
    if len(message) == 0:
        return message
    else: 
        n = 0
        new_string = ''
        letter_pos = None
        while n < len(message) :
            if message[n].isupper:
            	letter_pos = string.ascii_uppercase.index(message[n])
            	letter_pos += key
            	new_string.append(string.ascii_uppercase[letter_pos])
            elif message[n].islower:
            	letter_pos = string.ascii_lowercase.index(message[n])
            	letter_pos += key
            	new_string.append(string.ascii_lowercase[letter_pos])
            	print(message[n])
            else:
            	new_string.append(message[n])
            	print(message[n])
            n += 1
        return new_string
    #print(message)
    #print(new_string)
    #return new_string

#print(encryptor(13, ''))
print(encryptor(13, 'Caesar Cipher')) #'Pnrfne Pvcure'
#print(encryptor(-5, 'Hello World!')) #'Czggj Rjmgy!'
#print(encryptor(27, 'Whoopi Goldberg') #'Xippqj Hpmecfsh'
#print(encryptor(39, "T")) #'G
#print('ABV'.isupper())
