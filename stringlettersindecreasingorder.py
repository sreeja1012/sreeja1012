# import library
import numpy as np
def prCharWithFreq(str) :
     
    # Size of the 'str'
    n = len(str)
     
    # Initialize all elements of freq[] to 0
    freq = np.zeros(26, dtype = np.int)
    for i in range(0, n) :
        freq[ord(str[i]) - ord('a')] += 1
                 
    # Traverse 'str' from left to right
    for i in range(0, n) :
        if (freq[ord(str[i])- ord('a')] != 0) :
            print (str[i], freq[ord(str[i]) - ord('a')],
                                            end = " 
           freq[ord(str[i]) - ord('a')] = 0
if __name__ == "__main__" :
     
    str = "mississippi";
    prCharWithFreq(str)
