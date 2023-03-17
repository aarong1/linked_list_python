#linked_list_in_python.py
#--------------------------


class node:
    '''Each node has two properties, its value and a pointer that indicates the node that follows
'''
    def __init__(self, value):
        self.value = value
        self.next = None


class ll:
    '''The list has three properties, the head, the tail and the list size
'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
    while node is not None:
        yield node
        node = node.next

    
    def push(self,newVal):
        newNode = node(newVal)
        if self.head is None:

            print('self.head is None type')

            self.head = newNode
            self.tail = self.head


            # print(newNode.value)
            # print(self.head)

        else:

            print('self head is not None type')

        self.length += 1

    def head_value(self):
        print(self.head.value)


newL = ll()

newL.push(5)



