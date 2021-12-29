class Node():
    # constructor for Node class
    # current, next and previous values are initialized
    # in the __init__ function
    def __init__(self):
        self.__curr = None
        self.__prev = None
        self.__next = None

    # all the setters and getters are self-explanatory

    def set_curr(self, curr):
        self.__curr = curr

    def set_prev(self, prev):
        self.__prev = prev

    def set_next(self, nxt):
        self.__next = nxt

    def get_curr(self):
        return self.__curr

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next
