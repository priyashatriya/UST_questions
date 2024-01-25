from collections import deque
# Maximum length of the queue
MAX_LENGTH = 5


def circular_queue():
    try:
        #print('You are in circular queue function')
# Create a circular queue using a dictionary
        queue = deque(maxlen=MAX_LENGTH)
# Add elements to the queue
        queue.append(1)
        queue.append(2)
        queue.append(3)
        queue.append(4)
        queue.append(5)
# Queue is full, add a new element
        queue.append(6)
# Print the queue
        print(queue)
    except Exception as e:
        print('Error executing circular queue')
        raise

def main():
    try:
        circular_queue()
    except Exception as e:
        print('error in execution')
        raise

if __name__=='__main__':
    main()