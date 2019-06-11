class SingleNode(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self,):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        if self.is_empty():
            return 0
        cur = self._head
        cnt = 1
        # 尾节点指向None，当未到达尾部时
        while cur.next != self._head:
            cnt += 1
            cur = cur.next
        return cnt

    def travel(self):
        """遍历整个列表"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem,end =" ")
            cur = cur.next
        print(cur.elem,end=" ")

    def add(self,item):
        """头插法"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur =  self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = self._head

    def append(self,item):
        """尾插法"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0 :
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:
            pre = self._head
            cnt = 0
            while cnt < (pos-1):
                cnt +=1
                pre = pre.next
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                #判断头节点
                if cur == self._head:
                    #找尾
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    #中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem ==item:
            pre.next = cur.next

    def search(self,item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False


scll = SingleCycleLinkList()
scll.add(2)
scll.add(3)
scll.append(1)

print(scll.is_empty())
print(scll.length())
print(scll.travel()) # 会在

scll.insert(2,6)
scll.insert(3,66)
scll.insert(3,666)

print(scll.travel())
# print(scll.length())
print(scll.search(6))

scll.remove(66)
print(scll.travel())



