def quicksort(array):
    """
    分而治之的策略，
    1，基准条件尽可能简单
    2，不断将问题分解（或者说缩小规模），直到符合基线条件。
    1，当len(arrap)小于2的时候，即只可能是0或者1的时候
    2,将问题分解
    算法的不足：
    但是该算法有个问题，如果本来就是有序的数组，那么他就重复性的计算了一次，那么相当于浪费时间。
    且，该算法始终保持左边的数组空的，导致栈特别长。
    :param array:
    :return:
    """
    if len(array) < 2:

        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        qreater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(qreater)

if __name__ == "__main__":
    print(quicksort([10,8,156,7,10]))
