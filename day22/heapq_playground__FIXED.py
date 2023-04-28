# Demonstrating fix to error when using numpy Array in heapq 

# Discovery (from before): if you are using heapq's heappush and heappop (as a priority queue) and the items are a list with an integer followed by an Numpy array, you will get a ValueError if heappop needs to consult the Numpy array as a tie-breaker ... and it can be fixed by adding a globally unique int

import heapq
import numpy as np
import uuid


pq = []
heapq.heappush(pq, [77, uuid.uuid4().int, np.array([1,2])])
heapq.heappush(pq, [5, uuid.uuid4().int, np.array([2,3])])
heapq.heappush(pq, [42, uuid.uuid4().int, np.array([3,4])])

heapq.heappush(pq, [42, uuid.uuid4().int, np.array([4,5])]) # Adding globally unique int fixes the error


while len(pq) > 0:
    print(heapq.heappop(pq))

