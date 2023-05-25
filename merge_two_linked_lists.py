#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    list3 = SinglyLinkedList()
    list1 = []
    list2 = []
    while head1:
        list1.append(head1.data)
        head1 = head1.next

    while head2:
        list2.append(head2.data)
        head2 = head2.next

    l3 = sorted(list1+list2)

    print(l3)

    [list3.insert_node(i) for i in l3]
      
    return list3.head

    

if __name__ == '__main__':
    fptr = open("output", 'w')

    
    llist1_count = int(3)

    llist1 = SinglyLinkedList()

    for _ in [1, 2, 3]:
        llist1.insert_node(_)

    llist2 = SinglyLinkedList()

    for _ in [3, 4]:
        llist2.insert_node(_)

    llist3 = mergeLists(llist1.head, llist2.head)

    print_singly_linked_list(llist3, ' ', fptr)
    fptr.write('\n')

fptr.close()
