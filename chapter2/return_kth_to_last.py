class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next =None

    def __repr__(self):
        return "<Node: %s>" % self.data



class LinkedLists(object):

    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head

        while current is not None:
            print current,

            current = current.next



    def kth_to_last(self, k):

        current = self.head

        count = 0

        while current:
            count += 1
            current = current.next

        print count

        target = count - k

        counter_to_k = 1

        current = self.head
        while current:
            counter_to_k += 1
            if counter_to_k == target:
                return current
            else:
                current = current.next








ll = LinkedLists()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
ll.head = node1
