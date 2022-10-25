'''Linked Lists weren't defined in python a few years ago. Neither was the keyword 'class'. Here is an simple implementation
to refresh what these look like- in python of course! 

Kite has better automatic documentation. This is just a test to see @how docstrings are parsed today.

:pos:int pos is used to denote the index of the node that tail's next pointer is connected to. pos is not passed as a parameter
:val: data at that particular index

'''
# Definition for singly-linked list in the linked list cycle problem at leetcode.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node:
    # we pass in a data point or element to be stored by a node
    # default for data is set to None
    # 'tail' should have next as None
    def __init__(self, data = None):
        # self.val = data # watch 'val' per leetcode
        self.data = data # watch 'val' per leetcode
        self.next = None # pointer to next node
        # print(f'created main node self.next: {self.next}')
# wrapper over the nodes, user only interacts with this and not the node class
class linked_list:
    def __init__(self):
        # head has no data and is not indexable
        self.head = Node()
        print(f'created linked list with a head')
    def append(self, data):
        new_node = Node(data)
        cur = self.head # start at left most point in list
        # iterate over the list and find None- the last node in the list, in which to add to
        while cur.next != None:
            # just traverse the list
            cur = cur.next
        # here means we got to the last one
        # add it
        cur.next = new_node
    # length only needs the instance of the class
    def length(self):
        # point to cur
        cur = self.head
        total = 0 # how many have we seen
        # iterate over nodes, incrementing, and traversing
        while cur.next != None:
            total += 1
            cur = cur.next
        # got to end return total elements in list
        return total
    
    def display_all(self):
        # what data does it have?
        eles = []
        cur_node = self.head
        # print(dir(cur_node))
        # print(f'cur_node.next: {cur_node.next}')
        # traverse
        while cur_node.next != None:
            # set the cur to next
            cur_node = cur_node.next
            # add the elements  watch .val vs .data 
            # eles.append(cur_node.val)
        # print("past while") this indent will not give all data in the loop, just the last one
            eles.append(cur_node.data)
        print(f'eles: {eles}')
    
    def print_reversed(node):
        '''recursive call for last print first'''
        if node.next == None: return
        print_reversed(node.next)
        print(f'val:{node.val}')
        # else: no else on recursion, just call it

    def get(self, index):
        '''extract data at specific index we need the head & a way to know which index we're at
        :index: int: the position of the node is zero based
        '''
        if index >= self.length(): # check bounds
            print("ERROR: get element indexout of bounds")
            return None # no crash
        cur_idx = 0 # start at zero
        cur_node = self.head # start at beginning
        while True: # loop to the one in question
            cur_node = cur_node.next #forward one
            if cur_idx == index:# found one in question
                return cur_node.data
            # otherwise increment the cur_idx
            cur_idx += 1 
    def erase(self, index):
        cur_idx = 0
        cur_node = self.head
        # prev_node = None
        if index >= self.length(): # bounds
            print("ERROR: erase out of bounds")
            return # None do nothing instead
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index: # we found prev
                prev_node.next = cur_node# does nothing this is the same setup
                prev_node.next = cur_node.next
                break
            cur_idx += 1
# test funcitonality of add and length
a_list = linked_list()
print("created linked_list()")
#a_list.display_all()# error if no add?
a_list.append(34)
a_list.append(23)
a_list.append(76)
a_list.append(27)
# a_list.display_all()
# a_list.get(3)# out of bounds might need to do more than return None and print
# a_list.get(2) #76
# a_list.erase(2) #index zero based is 76
a_list.erase(3)
a_list.display_all()


