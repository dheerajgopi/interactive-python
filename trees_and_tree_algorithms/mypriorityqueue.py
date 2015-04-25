class BinaryHeap :
    def __init__(self) :
        self.heap_list = [0]
        self.current_size = 0

    def __str__(self) :
        return str(self.heap_list)

    def insert(self, item) :
        self.heap_list.append(item)
        self.current_size += 1
        self.perc_up()

    def perc_up(self) :
        done = False
        child = self.current_size
        parent = self.current_size / 2
        while not done :
            if self.heap_list[child] < self.heap_list[parent] :
                self.heap_list[child], self.heap_list[parent] = \
                    self.heap_list[parent], self.heap_list[child]
                child = parent  #comparing next parent child pair
                parent = child / 2
        
            else :
                done = True

    def del_min(self) :
        min_val = self.heap_list[1] #replacing root with largest term and percolating it down
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return min_val

    def perc_down(self, i) :
        i = 1 #present root value
        while (i * 2) <= self.current_size :
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc] :
                self.heap_list[i], self.heap_list[mc] = \
                   self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i) :
        if ((i * 2) + 1) > self.current_size :
            return i * 2
        else :
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1] :
                return i * 2
            else :
                return (i * 2) + 1

    def build_heap(self, alist) :
        self.current_size = len(alist)
        i = len(alist) / 2
        self.heap_list = [0] + alist[:]
        while i > 0 :
            self.perc_down(i)
            print self.heap_list
            i -= 1

bh = BinaryHeap()
bh.build_heap([1,5,2,7,3])
print bh
