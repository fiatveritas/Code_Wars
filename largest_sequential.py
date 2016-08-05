#!/usr/bin/python2.7
def next_bigger(n):
    print n
    number = [int(i) for i in str(n)]
    copy = number[:]
    index = len(copy) - 1
    list_num = []
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
                for digit in copy:
                    stringer += str(digit)
                list_num.append(int(stringer))
                index = 0
                continue
        index -= 1
    return min(list_num)

print next_bigger(12) #21
print next_bigger(513) #531
print next_bigger(2017) #2071
print next_bigger(414) #441
print next_bigger(144) #414
