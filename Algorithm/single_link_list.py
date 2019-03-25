class SingleNode(object):
    """单链表的节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        cnt = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self._head
            cnt = 0
            while cnt < (pos-1):
                cnt += 1
                pre = pre.next
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())

    sll.append(1)
    sll.append(4)
    print(sll.is_empty())
    print(sll.length())

    sll.add(33)
    sll.append(45)
    print(sll.travel())

    sll.insert(3,66)
    print(sll.travel())
    print(sll.search(88))

    sll.remove(4)
    print(sll.travel())
