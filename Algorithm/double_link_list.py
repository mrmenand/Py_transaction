class DoubleNode(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkList(object):

    def  __init__(self,node = None):
        self._head = node

    def  is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur  = self._head
        cnt = 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        return  cnt

    def travel(self):
        """遍历列表"""
        cur = self._head
        while cur is not None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self,item):
        """头插法"""
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self,item):
        """尾插法"""
        node = DoubleNode(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def insert(self,pos,item):
        """指定位置插入"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self._head
            cnt = 0
            while cnt < pos:
                cnt += 1
                cur = cur.next
            #退出循环 指向pos
            node = DoubleNode(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def  remove(self,item):
        """删除节点"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                #头节点
                if cur == self._head:
                    self._head = cur.next
                    #判断链表只有一个节点
                    if  cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next




    def  search(self,item):
        """查找节点是否存在"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    dll = DoubleLinkList()
    dll.add(2)
    dll.add(3)
    dll.append(1)

    print(dll.is_empty())
    print(dll.length())
    print(dll.travel())  

    dll.insert(2, 6)
    dll.insert(3, 66)
    dll.insert(3, 666)

    print(dll.travel())
    # print(dll.length())
    print(dll.search(6))

    dll.remove(66)
    print(dll.travel())

