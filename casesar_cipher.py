import string
def encryptor(key, message):
    #Program me!
    if len(message) == 0:
        return message
    else: 
        n = 0
        new_string = ''
        lister = []
        upper = [i for i in string.ascii_uppercase]
        lower = [i for i in string.ascii_lowercase]
        letter_pos = None
        while n < len(message) :
            if message[n].isupper():
            	letter_pos = upper.index(message[n])
            	letter_pos += key
            	while letter_pos < 0 or letter_pos > 25:
            		letter_pos %= 26
            	lister.append(upper[letter_pos])
            elif message[n].islower():
            	letter_pos = lower.index(message[n])
            	letter_pos += key
            	while letter_pos < 0 or letter_pos > 25:
            		letter_pos %= 26
            	lister.append(lower[letter_pos])
            	print message[n]
            else:
            	lister.append(message[n])
            	print message[n]
            n += 1
        return new_string.join(lister)
    #print(message)
    #print(new_string)
    #return new_string

#print(encryptor(13, ''))
#print encryptor(13, 'Caesar Cipher') #'Pnrfne Pvcure'
#print(encryptor(-5, 'Hello World!')) #'Czggj Rjmgy!'
#print encryptor(27, 'Whoopi Goldberg') #'Xippqj Hpmecfsh'
#print(encryptor(39, "T")) #'G
#print('ABV'.isupper())
