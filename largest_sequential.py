#!/usr/bin/python2.7
def next_bigger(n):
    print '*************', n
    number = [int(i) for i in str(n)]
    copy = number[:]
    index = len(copy) - 1
    stringer = ''
    while index >= 0:
        if copy[index - 1] < copy[index]:
            place_holder = index - 1
            antecedent_copy = copy[:place_holder + 1]
            after_copy = copy[place_holder + 1:]
            modified_copy = after_copy[:]
            #print antecedent_copy, after_copy
            modified_copy = after_copy[:]
            after_copy.sort()
            for i in after_copy:
                if antecedent_copy[place_holder] < i:
                    holder = None
                    holder = antecedent_copy[place_holder]
                    antecedent_copy[place_holder] = i
                    modified_copy[modified_copy.index(i)] = holder
                    break
            modified_copy.sort()
            for i in antecedent_copy:
                stringer += str(i)
            for i in modified_copy:
                stringer += str(i)
            #print antecedent_copy, modified_copy
            #print place_holder
            break
        index -= 1
    return int(stringer)

print next_bigger(12) #21
print next_bigger(513) #531
print next_bigger(2017) #2071
print next_bigger(414) #441
print next_bigger(144) #414
print next_bigger(1234567980)
