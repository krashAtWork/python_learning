from collections import deque

class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, ele):
        self.queue.append(ele)
        #print(self.queue)

    def pop(self):
        # check the length if 0 give none, if 1 give 1 , if 2 give 0, if 3 give 0
        length = len(self.queue)
        ##print(length)
        if(length == 0):
            return None
        else:
            return self.queue[0]

flower = Queue()
flower.push("flower")
flower.push("of")
flower.push("evil")
print(flower.pop())



river = deque();
river.append("river")
river.append("runs")
river.append("through")
river.append("it")
print(river.popleft())
