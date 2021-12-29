from linkedlist import LinkedList
from node import Node

# Stack follows the Last In First Out principle
class Stack(object):

    # constructor for stack class
    # initializing both the LinkedList and top in 
    # the __init__ function
    def __init__(self):
        self.__linkedList = LinkedList()
        self.__top = None

    # push item onto stack and update the top
    # index is 1 because it will always refer to the top of stack
    def push(self, x):
        self.__top = self.__linkedList.add(1, x)

    # pops item from top of stack and update the top
    # code goes here (should return item from top of stack or 
    # None if stack is empty)
    # index is 1 because it will always refer to the top of stack
    def pop(self):
        popped, current = self.__linkedList.remove(1)
        self.__top = current 
        return popped
        
    # returns Boolean of whether stack is currently empty
    # if top is None it's True
    def isEmpty(self):
        if self.__top == None:
            return True
        else: 
            return False

    # returns Boolean of whether stack is currently full
    # if top is None it's False
    def isFull(self):
        if self.__top == None:
            return False
        else: 
            return True

    # clears the stack
    # reinitialize the Linkedlist and top
    def clear(self):
        self.__linkedList = LinkedList()
        self.__top = None

    # looks at the top item of the stack without removing it
    # returns the top value instead for comparison
    def peek(self):
        if self.__top == None:
            return None

        return self.__top.get_curr()