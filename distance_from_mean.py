import numpy as np 
def distances_from_average(test_list):
    """This function computes the distance away from the average"""
    deviations = []
    mean = np.mean(test_list)
    for number in test_list:
    	deviations.append(round(mean - number, 2))
    return deviations


print distances_from_average([55, 95, 62, 36, 48]) # [4.2, -35.8, -2.8, 23.2, 11.2]
print distances_from_average([1, 1, 1, 1, 1]) # [0, 0, 0, 0, 0]
print distances_from_average([1, -1, 1, -1, 1, -1]) # [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
print distances_from_average([1, -1, 1, -1, 1]) # [-0.8, 1.2, -0.8, 1.2, -0.8])
print distances_from_average([2, -2]) # [-2.0, 2.0])
print distances_from_average([1]) # [0])
print distances_from_average([123, -65, 32432, -353, -534]) # [6197.6, 6385.6, -26111.4, 6673.6, 6854.6])
print distances_from_average(xrange(101)) # range(50,-51,-1))
print distances_from_average(xrange(1001)) # range(500,-501,-1))
#print distances_from_average(xrange(1000001)) # range(500000,-500001,-1))