class Node:
    """
    list 并不是传统意义上的列表，这也是append比insert操作效率高的原因所在。
    传统列表也叫做链表--通常是由一系列节点来实现的。每个节点都有指向下一节点的引用。

    """
    def __int__(self, value, naxt = None):
        self.value = value
        self.naxt = next


L = Node("a", Node("b", Node("c")))
L.naxt.value
