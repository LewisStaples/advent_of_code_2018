# Demonstrating error when using numpy Array in heapq 

# Discovery: if you are using heapq's heappush and heappop (as a priority queue) and the items are a list with an integer followed by an Numpy array, you will get a ValueError if heappop needs to consult the Numpy array as a tie-breaker.

import heapq
import numpy as np

pq = []
heapq.heappush(pq, [77, np.array([1,2])])
heapq.heappush(pq, [5, np.array([2,3])])
heapq.heappush(pq, [42, np.array([3,4])])

heapq.heappush(pq, [42, np.array([4,5])])# Uncommenting triggers the below error !!!
# ERROR:  ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

while len(pq) > 0:
    print(heapq.heappop(pq))

