#
# Author: Tom Pauwaert
# Date: 31 March 2015
# Description:
#     This python scripts implements a 2D and 1D peakfinder algorithm
#     based on the MIT OCW Course: Introductions to Algorithms
#     found on their OCW website (http://ocw.mit.edu/)
#

def peakfinder_1d(array):
    """ Find _a_ peak in an array. Where a peak is defined as any 
    value x, such that for surrounding values y and z the following
    holds:
    x >= y and x >= z
    For this definition, a peak _always_ exists in the array.

    @param: array - a non-empty array
    @exception: raised if the array is empty
    """
    if len(array) == 0:
        raise ValueError("Array argument should not be empty.")
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2: 
        return max(array)
    else:
        if (array[len(array)/2-1] >= array[len(array)/2]):
            return peakfinder_1d(array[:len(array)/2])
        elif (array[len(array)/2+1] >= array[len(array)/2]):
            return peakfinder_1d(array[max(len(array)-1, len(array)/2+1):])
        else:
            return array[len(array)/2]


def peakfinder_2d(array):
    """ Find _a_ peak in a 2D array. Where a peak is defined as any 
    value x, such that for surrounding values y and z on the same row
    and values u, v on the same column the following holds:
    x >= y and x >= z and x >= u and x >= v

    For this definition, a peak _always_ exists in the 2D array.

    @param: array - a non-empty array
    @exception: raised if the array is empty
    """
    rows = len(array)
    columns = len(array[0]) if type(array[0]) is list  else 0

    # This is a single list. Interpreted as a single column
    if columns ==  0:
        return max(array)

    # This is a list with list elements of length 1. So also a single column
    # but one that requires some preprocessing.
    elif columns == 1: 
        return max([x[0] for x in array])

    # special case for if there are only two rows.
    if rows == 1:
        return max(array[0])
    elif rows == 2:
        return max(array[0] + array[1])

    (row_max, index) = find_max_index(array[rows/2])

    # Determine whether to continue searching  in the upper half or in the 
    # lower half of the of the matrix.
    #
    if(array[rows/2-1][index] >= array[rows/2][index]):
        return peakfinder_2d(array[:rows/2-1])

    elif(array[rows/2+1][index] >= array[rows/2][index]):
        return peakfinder_2d(array[rows/2+1:])

    else:
        return array[rows/2][index]  # The current element is a peak.


def find_max_index(array):
    """ Takes a 1 dimensional array and find the maximum element in the
    array and returns the index and value of the first element in the array
    having this maximum value.
    """
    max_ = max(array)
    index = array.index(max_) 
    return (max_, index)

# TODO: Try matrices using numpy
# TODO: Try non-recursive versions of the algorithms - for large n.

if __name__ == "__main__":
    print "Provide an array to search: "
    result = peakfinder_1d(map(int,raw_input().strip().split()))
    print "Peak found for value: %s" % result
