import myqueue
import complab
import random

def simulation(num_seconds, pages_per_min) :
    lab_printer = complab.Printer(pages_per_min)
    print_queue = myqueue.Queue()
    waiting_times = []

    for second in xrange(num_seconds) :

        if new_print_task() :
            task = complab.Task(second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()) :
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(second))
            lab_printer.start_next(next_task)
        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print "Average Wait %6.2f secs %3d tasks remaining." %(average_wait, print_queue.size())

def new_print_task() :
    num = random.randrange(1, 181)
    if num == 180 :
        return True

for i in xrange(10) :
    simulation(3600, 5)
