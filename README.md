# Linked list implementation in python

Implement a linked list in python from scratch (not to be compared to, or compete with collections.deque!)

A linked list class is instantiated using ll(<value>)
  
Underneath the call the node class is used to construct the node list and hold information to the pointers to the neightbour nodes.
  
Current implementation of the singly linked list means only information on the _next_ node is kept. Not the previous node as per doubly linked lists.
  
```
#Instantiate a new class  
newL = ll()

#push values to the head
>>> newL.push(1)
>>> newL.push(2)
>>> newL.push(5)
  
 #the pretty print function shows a graphical visual of the linked list 
>>> newL
1 -> 2 -> 5 -> None
  
  #the class is iterable!
>>> for i,j in enumerate(newL):
...     print(i);print(j)
  
0
1
1
2
2

```

## Resources

### Linked Lists

https://realpython.com/linked-lists-python/#using-advanced-linked-lists

https://www.geeksforgeeks.org/data-structures/linked-list/

### Python Classes

### NoneType in Python

https://realpython.com/null-in-python/

### Data Structures in Python

https://www.freecodecamp.org/news/data-structures-in-javascript-with-examples/

<h2 style="align:center" > Diagram of the *pop()* method adding a node to the head of the list and reassigning the tail of the head node </h2>

<br>

<br>

<p align="center">
<img style = 'display: block;margin-left: 200rem;margin-right: auto;width:40%' src = 'https://github.com/aarong1/linked_list_python/blob/main/linked_list.png'> </img>
</p>
