def findSmallest(arr):
    """
    to find samllest_index
    :param arr:
    :return: smallest_index
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """

    :param arr:
    :return:
    """
    newArr = []
    for i in range (len(arr)):
        smallest = findSmallest(arr)

        newArr.append(arr.pop(smallest))

    return newArr
if __name__ == '__main__':
    selectionSort([5, 3, 6, 2, 10])