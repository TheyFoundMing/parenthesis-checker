from stack import Stack

class StackParenthesesChecker(object):
    # constructor for StackParenthesesChecker class
    # initializing the stack in the __init__ function
    def __init__(self):
        self.__stack = Stack()

    # Check if string s has balanced parenthesis
    def isBalanced(self, s):
        # for efficiency, the stack is cleared when user wants
        # to start the program again anytime
        self.__stack.clear()

        counter = 0;

        # pushing each character into the stack
        for ch in s:
            if ch == "(" or ch == ")":
                self.__stack.push(ch)
            else: 
                return "Invalid"
                
        # a counter is used to keep track of whether the string
        # is balanced or not
        while self.__stack.isFull():
            current = self.__stack.pop()
            if current.get_curr() == ")":
                counter += 1
            else:
                # if there is an open parenthesis without any
                # prior closing parenthesis we can assume it's 
                # unbalanced
                if counter == 0:
                    return False
                counter -= 1

        # balanced strings should have a count of 0 
        if counter == 0:
            return True
        else: 
            return False