import string
def encryptor(key, message):
    #Program me!
    if message == '':
        return ''
    else: 
        new_string = ''
        for i in message:
            if i in string.ascii_lowercase:
                number = string.ascii_lowercase.index(i)
                if key > 0:
                    number += key
                    if number > 25:
                        number %= 25
                        number -= 1
                    new_string += string.ascii_lowercase[number]
                else:
                    number += key
                    if number < -26:
                        number %= 26 
                    new_string += string.ascii_lowercase[number]
            elif i in string.ascii_uppercase:
                number = string.ascii_uppercase.index(i)
                if key > 0:
                    number += key
                    if number > 25:
                        number %= 25
                        number -= 1
                    new_string += string.ascii_uppercase[number]
                else:
                    number += key
                    if number < -26:
                        number %= 26
                    new_string += string.ascii_uppercase[number]
            else:
                new_string += i
    #print(message)
    #print(new_string)
    return new_string

print(encryptor(13, ''))
print(encryptor(13, 'Caesar Cipher')) #'Pnrfne Pvcure'
print(encryptor(-5, 'Hello World!')) #'Czggj Rjmgy!'
print(encryptor(27, 'Whoopi Goldberg') #'Xippqj Hpmecfsh'
#print(encryptor(39, "T")) #'G'