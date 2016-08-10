#!/usr/bin/python2.7
import random
def arranged(n, copy):
    """this function finds next largest integer"""

    stringer = ''
    index = len(copy) - 1
    while index > -1:
        if copy[index - 1] < copy[index]: #look for index where preceding digit is less than digit to the right
            place_holder = index - 1
            antecedent_copy = copy[:place_holder + 1]
            after_copy = copy[place_holder + 1:]
            after_copy.sort()
            modified_copy = after_copy[:]
            j = 0
            while j < len(after_copy): #switch the values of digits where the preceding digit is less than the one to the right
                if antecedent_copy[place_holder] < after_copy[j]:
                    holder = None
                    holder = antecedent_copy[place_holder]
                    antecedent_copy[place_holder] = modified_copy[j]
                    modified_copy[j] = holder
                    break
                j += 1
            modified_copy.sort()
            break
        index -= 1
    for i in antecedent_copy:
        stringer += str(i)
    for i in modified_copy:
        stringer += str(i)
    stringer = int(stringer)
    return stringer

def next_bigger(n):
    """this function finds the next largest integer based
    off digits on number 'n' passed into next_bigger()"""

    if type(n) is not int: #checks if correct input type givin
        return -1
    number = [int(i) for i in str(n)]
    if len(number) == 1: #checks if given number is one digit only
        return -1
    copy = number[:]
    index = len(copy) - 1
    while number[index - 1] >= number[index]: #checks if digits of given number are in monotonically decreasing order
        if index - 1 == 0:
            return -1
        index -= 1
    index = len(copy) - 1
    while index > -1 and number[0] == number[index]: #checks if all digits are the same
        if index == 0:
            return -1
        index -= 1
    return arranged(n, copy) #if none of the above, find next largest integer with arranged() function

#test cases, uncomment below to test
##############
#import random
#rand_list = []
#for i in range(0,200):
#    rand_list.append(random.randint(1,200000))
#for i in rand_list:
#    print 'random number generated', i, '\nnext number', next_bigger(i)