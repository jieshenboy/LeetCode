def find_end_m():
    """
    这里的案例是找出关系网中谁是m结尾的人的例子
    用得到的有队列。：先入先出
    广度遍历，层层查找
    双边队列，deque()
    :O:V+E(V表示顶点(vertice)，E表示边数(Edge)
    :param person:
    :return: T or F
    """
    graph = {}
    graph["you"] = ["alice","bob","claire"]
    graph["alice"] = ["peggy"]
    graph["bob"] = ["anuj","peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"]=[]
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    from collections import deque
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()#提取一个人
        if (person not in searched):
            if person_is_seller(person):
                print("person "+ person + "is a mango seller!")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

if __name__ == "__main__":
    print(find_end_m())