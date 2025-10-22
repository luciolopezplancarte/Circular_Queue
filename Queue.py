"""
Lucio Plancarte
"""

class Queue:
    
    def __init__(self, capacity = 10):
        """
        Constructor for the class.
        It initializes the queue with a list of None elements.
        The capacity of the initial queue is provided by the user.
        It also initializes instance variabels for:
            the capacity of the array
            the size
            the initial front of the queue
            the ratio for the expand resize operation to 2
            the reduce threshold for the resize operation to 0.25
        PARAMETERS:
        -------------
        capacity : int. The initial capacity for the array
        """
        self._capacity = capacity
        self._size = 0
        self._queue = [None] * capacity
        self._front = 0
        self._expand_ratio = 2
        self._reduce_threshold = 0.25
        self._rear = capacity -1



    def __len__(self):
        """
        Method to return the length of the queue (the valid elements)
        """
        return self._size


    def __str__(self):
        """
        Method to show the content of the array
        (INCLUDE the None elements for visualization purposes)
        This method returns a String.
        """
        return "[" +",".join(str(item) for item in self._queue) +"]"
        

    def is_empty(self):
        """
        Method to check if the queue is empty
        The method returns True or False if queue is empty
        """
        return self._size == 0

    def peek(self):
        """
        Method to return the element at the FRONT of the queue
        The method returns None if the queue is empty
        This method does not remove the element from the queue
        """
        return self._queue[self._front]
    
    def set_front(self, front_id):
        """
        Method to set the new front of the queue
        PARAMETERS:
        -----------
        front_id : int. The index to be used as front of the circular queue
        """
        self._front = front_id

    def get_front(self):
        """
        Method to return the index where the front of the queue is at
        """
        return self._front

    def compute_front(self):
        """
        Method to compute the next front.
        This is useful if we are at the end of the queue and we want to add
        a new item.
        It USES the EQUATION discussed in class to get the value of the new front.
        It returns the new front.
        """


    def compute_next_available(self):
        """
        Method to compute the next available empty index to use to enqueue an item.
        It USES the EQUATION discussed in class to get the next index.
        It returns the next available index.
        """

    def dequeue(self):
        """
        Method to REMOVE and RETURN the logical front element from the queueue.
        If the queue is empty it prints a message "Empty"
        otherwise, it returns the element that is at the FRONT of the queue.
        The method computes the new front of the queue and sets the new front 
        accordingly using the methods for setting and computing the new front.

        The method needs to check if the size of the queue is at or below the shrink
        threshold based on the capacity and calls the resize operation passing the 
        new size rounded.
        Use the reduce threshold.
        It shows the message "Removing. New Front."
        It reduces the size of the queue/
        """

    def enqueue(self, item):
        """
        Method to add an item at the LOGICAL end of the queue.
        If the queue is full it needs to be resized by the expand ratio of its current
        capacity.
        The method needs to compute the next available index in the queue to be used for
        inserting the item.
        The method updates the size of the queue.
        It shows the message "Inserting at index: "
        PARAMETERS:
        -------------
        item : int. The item to add to the queue
        """

    def resize(self, new_cap):
        """
        Method to change the capacity of the queue.
        The method needs to MOVE the logical positions of the items in the old queue to
        their corresponding positions in the new queue.
        After moving the elements to their corresponding positions, it resets the front 
        and changes the capacity.
        It shows the message "Resizing..."
        PARAMETERS:
        ------------
        new_cap : int. The new capacity for the array
        """
