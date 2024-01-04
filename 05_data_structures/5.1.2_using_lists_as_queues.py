from collections import deque

### 5.1.2. Using Lists as Queues

# Reference: https://docs.python.org/3.12/tutorial/datastructures.html#using-lists-as-queues

"""
It is also possible to use a list as a queue, where the first element added is the first element retrieved ("first-in, first-out");
however, lists are not efficient for this purpose.
While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow
(because all of the other elemenbts have to be shifted by one).

To implement a queue, use collections.dequeue which was designed to have fast appends and pops from both ends.
For example:
"""

queue = deque(["Eric", "John", "Michael"])
print("queue:", queue)

queue.append("Graham")
print("queue:", queue)

print("queue.popleft():", queue.popleft()) # Eric
print("queue:", queue)

print("queue.popleft():", queue.popleft()) # John
print("queue:", queue)
