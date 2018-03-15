def binarySearch(list, item):
    low = 0
    high = len(list)-1#4


    while low < high:
        mid = (low+high)//2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    if low == high:
        return low
    return None

if __name__ == "__main__":
    binarySearch([1,3,5,7,9],9)