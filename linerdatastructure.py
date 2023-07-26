# QUESTION 9
def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(char, operand1, operand2)
            stack.append(result)
    return stack.pop()

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Example usage
expression = input("Enter postfix expression: ")
result = evaluate_postfix(expression)
print("Result: ", result)



# # QUESTION 10


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "Queue is empty"
        elif len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue = Queue()

while True:
    choice = input("Enter 1 to enqueue, 2 to dequeue, and 3 to exit: ")
    if choice == "1":
        value = input("Enter a value to enqueue: ")
        queue.enqueue(value)
    elif choice == "2":
        value = queue.dequeue()
        print(f"Dequeued value: {value}")
    elif choice == "3":
        break
    else:
        print("Invalid choice")




