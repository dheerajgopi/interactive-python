import myqueue

def hot_potato(players, count) :
    queue = myqueue.Queue()

    for player in players :
        queue.enqueue(player)

    while queue.size() > 1 :
        for i in xrange(count) :
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()

print hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)
