queue = []

# append method to perform insertion at rear
def enqueue():
    element = input("Enter element to be inserted")
    queue.append(element)

def dequeue():
    if not queue:
        print("Queue is Empty")
    else:
        e = queue.pop(0)
        print("Poped element",e)

def display():
    print(queue)

while True:
    operation = int(input("Enter the operation 1.Insert 2.Delete 3.Display 4.Quit\n"))
    if operation==1:
        enqueue()

    elif operation == 2:
        dequeue()

    elif operation==3:
        display()
    else:
        print("Enter correct Operation")

