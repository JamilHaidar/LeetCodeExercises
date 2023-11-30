class Node():
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None

class FrontMiddleBackQueue:

    def __init__(self):
        self.current_size = 0
        self.start = None
        self.end = None
        self.middle = None

    def insert_one_element(self,val: int) -> None:
        new_node = Node(val)
        self.start = new_node
        self.end = new_node
        self.middle = new_node
        self.current_size += 1

    def pushFront(self, val: int) -> None:
        if not self.current_size: return self.insert_one_element(val)
        new_node = Node(val)
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node
        if self.current_size%2==1:self.middle = self.middle.prev
        self.current_size += 1

    def pushMiddle(self, val: int) -> None:
        if not self.current_size: return self.insert_one_element(val)
        new_node = Node(val)
        if self.current_size==1:
            new_node.next = self.middle
            self.middle.prev = new_node
            self.middle = new_node
            self.start = new_node
        else:
            if self.current_size%2==1:
                new_node.next = self.middle
                new_node.prev = self.middle.prev
                self.middle.prev.next = new_node
                self.middle.prev = new_node
                self.middle = new_node
            else:
                new_node.next = self.middle.next
                new_node.prev = self.middle
                self.middle.next = new_node
                new_node.next.prev = new_node
                self.middle = new_node
        self.current_size += 1

    def pushBack(self, val: int) -> None:
        if not self.current_size: return self.insert_one_element(val)
        new_node = Node(val)
        self.end.next = new_node
        self.end.next.prev = self.end
        self.end = self.end.next
        if self.current_size%2==0:self.middle = self.middle.next
        self.current_size += 1
    
    def popFront(self) -> int:
        if not self.current_size:return -1
        val = self.start.val
        if self.current_size == 1:
            self.start = self.end = self.middle = None
        else:
            if self.current_size%2==0:self.middle = self.middle.next
            self.start = self.start.next
            self.start.prev = None
        self.current_size -= 1
        return val

    def popMiddle(self) -> int:
        if not self.current_size:return -1
        val = self.middle.val
        if self.current_size == 1:
            self.start = self.end = self.middle = None
        elif self.current_size == 2:
            self.end = self.start = self.middle = self.start.next
            self.start.prev = None
        else:
            self.middle.next.prev = self.middle.prev
            self.middle.prev.next = self.middle.next
            if self.current_size%2==0:
                self.middle = self.middle.next
            else:
                self.middle = self.middle.prev
        self.current_size -= 1
        return val
    def popBack(self) -> int:
        if not self.current_size:return -1
        val = self.end.val
        if self.current_size == 1:
            self.start = self.end = self.middle = None
        else:
            self.end = self.end.prev
            self.end.next = None
            if self.current_size%2==1:self.middle = self.middle.prev
        self.current_size -=1
        return val

def traverse_queue(root):
    while root:
        print(root.val,root.prev.val if root.prev else None,root.next.val if root.next else None)
        root = root.next

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
q = FrontMiddleBackQueue()
q.pushFront(1)   # [1]
q.pushBack(2)    # [1, 2]
q.pushMiddle(3)  # [1, 3, 2]
q.pushMiddle(4)  # [1, 4, 3, 2]
q.popFront()     # return 1 -> [4, 3, 2]
q.popMiddle()    # return 3 -> [4, 2]
q.popMiddle()    # return 4 -> [2]
q.popBack()      # return 2 -> []
q.popFront()     # return -1 -> [] (The queue is empty)