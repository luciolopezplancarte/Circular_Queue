from Queue import Queue

if __name__ == "__main__":
    q = Queue(3)
    print(q) 
    print(f"Size: {len(q)}")
    print(f"Empty? {q.is_empty()}")
    front_e = q.dequeue()
    print(f"The element at the front was {front_e}")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Size: {len(q)}")
    print(q)
    q.enqueue(4) #Resizing
    print(f"Size: {len(q)}")
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(f"Size: {len(q)}")
    print(q)
    q.enqueue(8)
    print(f"Size: {len(q)}")
    print(q)
    q.enqueue(9)
    print(f"Size: {len(q)}")
    print(q)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(f"Size: {len(q)}")
    print(q)
    print(f"First element: {q.peek()}")

    
    
    

