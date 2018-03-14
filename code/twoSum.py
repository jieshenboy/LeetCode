
#计算两个值，两个值的和等于target的位置
def twoSum(nums, target):
    i=0
    a=0

    for a in nums:
        i=i+1
        j = 0
        for b in nums:
            j=j+1
            if (i == j):
                break
            if (a == target - b):
                print(j,i)
                return [j-1 , i-1]



if __name__ == '__main__':
    twoSum([3, 2, 4], 6)
