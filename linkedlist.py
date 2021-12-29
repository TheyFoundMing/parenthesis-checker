from node import Node

class LinkedList(object):

    # constructor for LinkedList class
    # initializing both the head and tail in the __init__ function
    def __init__(self):
        self.__head=None
        self.__tail=None

    # add item x to list at index i
    def add(self, i, x):
        current = Node()
        current.set_curr(x)

        # when head is empty, you can set the current node as
        # both head and tail
        if self.__head == None:
            self.__head = current
            self.__tail = current
            return current

        if i: # stacks
            # the current node replaces the tail
            current.set_prev(self.__tail)
            self.__tail.set_next(current)
            self.__tail = current
        else: # queues
            # the current node replaces the head 
            current.set_next(self.__head)
            self.__head.set_prev(current)
            self.__head = current

        return current

    # remove item at index i from the list
    # code goes here (should return item from list or None if item is not in the list)
    def remove(self, i):

        # if the list is empty, it will just return None for
        # both popped and current variables
        if self.__tail == None:
            return None, None

        if i: # stack
            # the self.__tail is now updated to the popped's
            # previous node
            popped = self.__tail    
            self.__tail = self.__tail.get_prev()

            # if the current tail is now None after popping, 
            # the 'current' node variable is returned as none
            if self.__tail == None:
                return popped, None
            
            # close off the current tail from the popped node
            self.__tail.set_next(None)
            return popped, self.__tail

        else:
            # the self.__head is now updated to the popped's
            # previous node
            popped = self.__head
            self.__head = self.__head.get_next()

            # if the current head is now None after popping,
            # the 'current' node variable is returned as none
            if self.__head == None:
                return popped, None
            
            # close of the current head from the popped node
            self.__head.set_prev(None)
            return popped, self.__head