from queue import Queue

class QueueParenthesesChecker(object):
    # constructor for QueueParenthesesChecker class
    # initializing two Queue classes in the __init__ function 
    def __init__(self):
        self.__queue1 = Queue()
        self.__queue2 = Queue()
        
    # check if string s has balanced parenthesis
    def isBalanced(self, s):
        # for efficiency, both queues are cleared when user wants
        # to start the program again anytime
        self.__queue1.clear()
        self.__queue2.clear()

        # queue-ing each character into queue1
        for ch in s:
            if ch == "(" or ch == ")":
                self.__queue1.enqueue(ch)
            else: 
                return "Invalid"

        # queue2 is used as a separate array to hold all the ')'
        # and will be dequeued whenever a '(' appears
        while self.__queue1.isFull():
            popped = self.__queue1.dequeue()

            if popped.get_curr() == ")":
                self.__queue2.enqueue(popped.get_curr())

            # if queue1 was to run out of nodes, we can assume 
            # that the string is unbalanced
            else:
                if self.__queue2.isEmpty():
                    return False
                else: 
                    remove = self.__queue2.dequeue()

        # if both queues are empty, that means the string is 
        # therefore balanced
        if self.__queue1.isFull() or self.__queue2.isFull():
            return False
        else: 
            return True 
