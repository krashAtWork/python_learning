class Maxheap:
    def __init__(self, items = [] ):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) -1)

    def push(self, ele):
        self.heap.append(ele)
        self.__floatUp(len(self.heap) -1)

    def peek(self)
        if self.heap[1]:
            return self.heap[1]
        else
            return False

    def pop(self):
        if len(self.heap) > 2 :
            # do al ot stuff
            self.__swap(1, len(self.heap) -1 )
            max = self.heap.pop[1]
            self.__bubbleDown(1)
        elif(len(self.heap) == 2):
            max = self.heap.pop[1]
        else:
            max = False
        return max

  def __swap(self, i , j ):
      self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def __s
