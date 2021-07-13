import numpy as np

#encodes text array containing categorical labels into numeric labels
#x is the list of categorical labels that you wish to encode into numerical categorical data

def encode(x):
    uniqueClasses = set(x)

    encodedArray = np.array(x)
    for count, word in enumerate(uniqueClasses):
        indices = [i for i, y in enumerate(x) if y == word]
        encodedArray[indices] = count
    
    return encodedArray
