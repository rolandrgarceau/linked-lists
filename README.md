# linked-lists
A refresher on linked lists in Python. Linked Lists weren't defined in python some years ago when I started my journey in 2.7x. Neither was the keyword 'class'. Here is an simple implementation
to refresh what these look like- in python of course it's not! 

Linked lists data uses the concept of nodes. Nodes are allocated in memory at runtime. In python we can say the linked list node can be found at its next value (next value might be a pointer). We may need to know where the head is at to start this process, and a tail's next for a singly linked list in python will be `None`. There may be a previous pointer for doubly linked lists, but we are looking just at singly linked lists right now. 

This example was created as to prime for trying to solve [leetcode's linked list cycle](https://leetcode.com/problems/linked-list-cycle/). I don't think I would have thought of skipping nodes to see which one might repeat by checking if they equal themselves at some point. Go figure.

In python next is the pointer to the node or memory location of that node. The node itself knows how to get to the next node, so these might not be in contiguous memory locations.

We can think of an array like a linked list: it has indices into values of elements at a particular index. Array length is the amount of elements. 

Arrays memory location is known at compile time, not runtime, and is stored consecutively. We can use binary search on arrays or linear search, but a linked list only has linear search.

## linked_list.py

The node class is not accessed by user, the wrapper class is (linked_list). The initialization of linked_list creates a list of length zero, and it contains a head, but the head has no data, just reference to the first data node.

The append will create the first data element to the list.

## Gotchas

'node' object has no attribute 'next' if we initialize with 'init' and not __init__ .  Watch what you write! It will work and fail at runtime. 

### Adding recursive features

The .ipynb file has a print_reversed method. To write this function we need to know a few things about the nature of this linked list. First, when a node is created, it becomes the 'root' or 'head' node. What denotes this? The links are the self.next attributes in the linked list class
