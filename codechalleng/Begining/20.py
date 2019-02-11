import math
from collections import deque


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    queue = deque([])
    mean = []
    for element in sequence:
        queue.append(element)
        mean.append(round(sum(queue)/len(queue),2))
    return mean


mean = running_mean([2, 6, 10, 8, 11, 10])
print(mean)
