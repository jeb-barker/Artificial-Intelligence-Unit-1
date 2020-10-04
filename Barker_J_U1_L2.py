# Name: Jeb Barker
# Date: Sep. 28, 2020

import random


# print all items in one line with a tab or 3 to 4 spaces.
def display(array):
    [print(str(item) + "\t") for item in array]


# sort the array by using heapsort algorithm.
# use swap and heapDown
def sort(array):
    pass


# swap two items at position a and b in array
# array is a list, a and b are integers
def swap(array, a, b):
    pass


# heap down from k to size
def heapDown(array, k, size):
    left, right = 2 * k, 2 * k + 1
    pass


# check all items in array.
# Returns True if all items are in ascending order.
def isSorted(array):
    return True if sorted(array) == array else False


# use round(random.unifrom(from, to), 2) to assign new values in each cell
def createRandom(array):
    return [round(random.unifrom(), 2)]


# Make the given array as a max heap. Use heapDown.
def makeHeap(array, size):
    pass


def main():
    array = [0.0] * 101
    createRandom(array)
    display(array)
    makeHeap(array, len(array) - 1)
    display(array)
    sort(array)
    display(array)
    print(isSorted(array))


if __name__ == '__main__':
    main()

''' Sample output

15.36   38.17   58.13   59.72   84.46   6.77   72.38   92.32   48.53   46.59   12.68   15.6   36.55   55.51   68.78   91.3   96.35   53.01   62.4   4.12   53.27   36.61   87.25   98.7   58.46   7.19   36.51   31.73   61.75   43.94   76.1   7.55   46.47   14.9   75.97   4.39   96.78   32.97   3.86   55.28   40.99   76.06   33.9   17.0   82.2   30.35   49.85   54.93   78.24   19.22   98.36   20.73   55.19   17.98   61.77   3.77   17.16   29.2   64.7   49.35   13.44   97.75   21.87   55.29   77.09   70.75   31.78   90.42   86.74   26.31   92.45   7.44   97.05   42.43   22.97   92.51   39.43   38.58   15.27   57.41   78.49   55.65   89.27   84.8   75.52   65.33   58.08   3.86   32.1   90.31   91.24   32.41   65.28   19.51   84.68   69.37   5.51   68.73   12.86   21.51   
98.7   97.05   98.36   96.78   91.24   78.24   97.75   96.35   92.51   89.27   90.31   69.37   61.77   64.7   76.1   91.3   92.45   59.72   62.4   78.49   84.8   84.46   87.25   68.73   58.46   55.19   36.55   31.73   61.75   49.35   72.38   77.09   70.75   90.42   92.32   53.01   48.53   39.43   38.58   57.41   55.65   76.06   65.33   32.1   82.2   65.28   84.68   58.13   15.6   21.51   6.77   20.73   7.19   17.98   36.51   3.77   17.16   29.2   55.51   43.94   13.44   68.78   21.87   55.29   7.55   46.47   31.78   14.9   86.74   26.31   75.97   7.44   4.39   42.43   22.97   32.97   38.17   3.86   15.27   46.59   55.28   4.12   40.99   53.27   75.52   33.9   58.08   3.86   17.0   36.61   12.68   32.41   30.35   19.51   49.85   54.93   5.51   15.36   12.86   19.22   
3.77   3.86   3.86   4.12   4.39   5.51   6.77   7.19   7.44   7.55   12.68   12.86   13.44   14.9   15.27   15.36   15.6   17.0   17.16   17.98   19.22   19.51   20.73   21.51   21.87   22.97   26.31   29.2   30.35   31.73   31.78   32.1   32.41   32.97   33.9   36.51   36.55   36.61   38.17   38.58   39.43   40.99   42.43   43.94   46.47   46.59   48.53   49.35   49.85   53.01   53.27   54.93   55.19   55.28   55.29   55.51   55.65   57.41   58.08   58.13   58.46   59.72   61.75   61.77   62.4   64.7   65.28   65.33   68.73   68.78   69.37   70.75   72.38   75.52   75.97   76.06   76.1   77.09   78.24   78.49   82.2   84.46   84.68   84.8   86.74   87.25   89.27   90.31   90.42   91.24   91.3   92.32   92.45   92.51   96.35   96.78   97.05   97.75   98.36   98.7   
True

'''