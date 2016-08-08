#!/usr/bin/python2.7
def next_bigger(n):
    print '*************', n
    number = [int(i) for i in str(n)]
    copy = number[:]
    index = len(copy) - 1
    while index >= 0:
        for i in range(len(copy) - 1, -1, -1):
            if index == i:
                continue
            elif copy[index] == copy[i]:
                continue
            elif copy[index] > copy[i]:
                digit_holder = None
                digit_holder = copy[index]
                copy[index] = copy[i]
                copy[i] = digit_holder
                stringer = ''
                holder = None
                if index < i:
                    holder = index
                else:
                    holder = i
                print holder
                another_copy = copy[holder+1:]
                another_copy.sort()
                for digit in copy[:holder+1]:
                    stringer += str(digit)
                for digit in another_copy:
                    stringer += str(digit)
                print '***', copy[:holder+1], '***', another_copy[holder:],
                return(int(stringer))
        index -= 1

print next_bigger(12) #21
print next_bigger(513) #531
print next_bigger(2017) #2071
print next_bigger(414) #441
print next_bigger(144) #414
#print next_bigger(1234567980)
