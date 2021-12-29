from stack import Stack
from stack_checker import StackParenthesesChecker
from queue_checker import QueueParenthesesChecker

def main():
    # checkers are set up here
    # stacks, queues and linkedlists are initialized inside
    # their respective classes when needed instead
    checker1 = StackParenthesesChecker()
    checker2 = QueueParenthesesChecker()

    userString = ""
    
    # a loop to ask input via console for new string to check with both checkers
    while True:
        userString = input("Enter string: ")

        stack_balanced = checker1.isBalanced(userString)
        queue_balanced = checker2.isBalanced(userString)

        if stack_balanced == "Invalid" and queue_balanced == "Invalid":
            print("Invalid string")
        elif stack_balanced and queue_balanced:
            print("The input string '%s' has balanced parentheses." % userString)
        else:
            print("The input string '%s' does not have balanced parentheses." % userString)

        # the stacks and queues will clear when checker.isBalanced() is called
        response = input("Try again? (y/n) ")
        if response[0] == "y":
            continue
        elif response[0] == "n":
            break
        else:
            break

if __name__ == "__main__":
    main()
