import string
def encryptor(key, message):
    """This script takes a key and shifts each letter \
    in a message by the key. Positive key shifts letter \
    to the right. Negative number shifts to the left. \
    Shifts are based on alphabetical order."""
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
