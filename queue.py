from linkedlist import LinkedList

class Queue(object):
    # constructor for Queue class
    # initializing both the LinkedList, front and rear 
    # the __init__ function
    def __init__(self):
        self.__linkedList = LinkedList()
        self.__front = None
        self.__rear = None

    # adds item to front of queue
    # rear typically remains the same after the first one
    # head will be the x value as a node
    # index is 0 because we'll always add it from the front
    def enqueue(self, x):
        current = self.__linkedList.add(0, x)

        # if the queue is empty, we can set the rear to currents
        if self.isEmpty():
            self.__front = current
            self.__rear = current
        else: 
            self.__front = current

    # removes item from rear of queue
    # code goes here (should return item from end of queue or None if queue is empty)
    # index is 0 because we'll always remove it from the front
    def dequeue(self):
        dequeued, front = self.__linkedList.remove(0)
        self.__front = front

        return dequeued
    
    # returns Boolean of whether queue is currently empty
    # if front is None it's True
    def isEmpty(self):
        if self.__front == None:
            return True
        else:
            return False

    # returns Boolean of whether queue is currently full
    # if front is None it's False
    def isFull(self):
        if self.__front == None:
            return False
        else:
            return True

    # clears the queue
    # reinitialize the Linkedlist, front and rear
    def clear(self):
        self.__linkedList = LinkedList()
        self.__front = None
        self.__rear = None

    # looks at the item at the end of the queue without removing it
    # returns the front value instead for comparison
    def poll(self):
        if self.__rear == None:
            return None

        return self.__rear.get_curr()
