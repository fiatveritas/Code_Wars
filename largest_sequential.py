#!/usr/bin/python2.7
import random
def arranged(n, copy):
    stringer = ''
    index = len(copy) - 1
    while index > -1:
        if copy[index - 1] < copy[index]:
            place_holder = index - 1
            antecedent_copy = copy[:place_holder + 1]
            after_copy = copy[place_holder + 1:]
            after_copy.sort()
            modified_copy = after_copy[:]
            print antecedent_copy, after_copy
            j = 0
            while j < len(after_copy):
                if antecedent_copy[place_holder] < after_copy[j]:
                    holder = None
                    holder = antecedent_copy[place_holder]
                    antecedent_copy[place_holder] = modified_copy[j]
                    modified_copy[j] = holder
                    break
                j += 1
            modified_copy.sort()
            #print place_holder
            break
        index -= 1
    for i in antecedent_copy:
        stringer += str(i)
    for i in modified_copy:
        stringer += str(i)
    stringer = int(stringer)
    print antecedent_copy, modified_copy
    return stringer
def next_bigger(n):
    print '*************', n
    if type(n) is not int:
        return -1
    number = [int(i) for i in str(n)]
    copy = number[:]
    index = len(copy) - 1
    while number[index - 1] > number[index]:
        #print index
        if index - 1 == 0:
            return -1
        index -= 1
    index = len(copy) - 1
    while index > -1 and number[0] == number[index]:
        if index == 0:
            return -1
        index -= 1
    return arranged(n, copy)

#for i in [random.randint(0, 20000) for j in range(0,200)]:
#    print i
#    print next_bigger(i)

print next_bigger(12) #21
print next_bigger(513) #531
print next_bigger(2017) #2071
print next_bigger(414) #441
print next_bigger(144) #414
print next_bigger(1234567980)
#print next_bigger(98765421)
#print next_bigger(1111)
#print next_bigger(3)
print next_bigger(7555)
#print next_bigger('')