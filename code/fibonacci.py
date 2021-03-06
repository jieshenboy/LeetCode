class Fibonacci(object):
    """
    返回一个斐波那契数列
    """
    def __init__(self):
        self.fList = [0,1] #设置初始列表
        self.main()

    def main(self):
        listLen = input("请输入fibonacci数列的长度（3-50）：")
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print("得到的fibonacci数列为：\n %s" %self.fList)

    def checkLen(self, lenth):
        lenList = map(str, range(3,51))
        if lenth in lenList:
            print("长度符合标准，可以运行")
        else:
            print("不符合长度")
            exit()

if __name__ == "__main__":
    f = Fibonacci()
