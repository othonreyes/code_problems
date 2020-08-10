from collections import Counter
from queue import PriorityQueue

if __name__ == '__main__':
    # option 1 but primitive
    counter = Counter()
    name = 'Othon Reyes Sanchez'
    for i in name:
        counter[i] += 1
    print(f"Words ", counter)

    # option 2: from an iterable
    counter2 = Counter(name)
    print(f"Words2 ", counter2)

    queue = PriorityQueue()

    def sequencer():
        for i in reversed(range(1,10)):
            yield i

    for i in sequencer():
        print(f"Pushing {i}")
        queue.put(i)

    while not queue.empty():
        print(f"Poping {queue.get()}")
