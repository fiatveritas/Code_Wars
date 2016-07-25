import re
import string
def pig_it(text):
    #your code here
    print(text)
    new_word = ''
    if len(text) == 0:
        return 'ay'
    elif len(text) == 1 and (text in string.ascii_lowercase or text in string.ascii_uppercase):
        new_word = text + 'ay'
        return new_word
    else:
        new_text = re.split('(\W+)', text)
        for word in new_text:
            #print('***' + word)
            if len(word) == 1 and (word not in string.ascii_uppercase or word not in string.ascii_lowercase):
                new_word += word
            else:
                #print('here')
                if word == ' ':
                    new_word += word
                elif len(word) > 1:
                    new_word += word[1:-1] + word[-1] + word[0] + 'ay'
        #new_word = new_word[:-1]
        print(new_word)
        return new_word