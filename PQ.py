
# -------------------------------------------------------
#  ICC-211 DATA STRUCTURE & CLASSIC ALGORITHMS
#  LAB #2 - Priority Queue
#
#  Name  : Ruddy Gabriel Gomez Tejada
#  ID    : 1014-3471
#  Email : rggt0001@ce.pucmm.edu.do
#  Date  : 8/12/2022
# -------------------------------------------------------

class PriorityQueue:

    # Class constructor
    def __init__(self):
        # Members of
        self.heap = []
        self.data_dict = {}
        # Additional code 
        self.size = 0

    def insert_or_update(self, priority, data):
        newData = (priority,data)
        if self.heap:
            if data in self.data_dict:
                #si el dato a insertar ya esta en el heap
                oldPriority = self.heap[self.data_dict[data]] #prioridad del dato que ya estaba insertado
                if oldPriority[0]>priority:
                    #si la prioridad nueva del dato es menor a la antigua entonces actualizalo
                    self.heap[self.data_dict[data]] = newData
                else:
                    return
            else:
                #si no esta en el heap entronces agregalo
                self.heap.append(newData)
                self.size+=1
                self.data_dict[data] = self.size-1
            self.shiftUp(self.data_dict[data]) #empieza a mover el dato si es menor prioridad en el heap
        else:
            #si el heap esta vacio inserta el primer valor
            self.heap.append(newData)
            self.size+=1
            self.data_dict[data] = self.size-1
        
        return
    def swap(self,finalIndex, firstIndex):
        self.heap[finalIndex], self.heap[firstIndex] = self.heap[firstIndex], self.heap[finalIndex]
        self.data_dict[self.heap[firstIndex][1]] = firstIndex
        self.data_dict[self.heap[finalIndex][1]] = finalIndex
            
        
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self,index):
        return 2*index + 1
    def getRightChildIndex(self,index):
        return 2*index + 2
    
    def parent(self,index):
        return self.heap[self.getParentIndex(index)]
    def leftChild(self,index):
        return self.heap[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.heap[self.getRightChildIndex(index)]
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)< self.size

    def shiftUp(self,index):
        if index >= 0:
            actualPriority = self.heap[index][0] #tomamos la prioridad del valor que comparamos
            if self.hasParent(index):
                #si tiene padre comparamos con la prioridad del padre
                fatherPriority = self.heap[self.getParentIndex(index)][0]
                if fatherPriority>actualPriority:
                    #si la actual es menor a la de su padre entonces intercambiamos
                    self.swap(index,self.getParentIndex(index))
                    #seguimos subiendo para encontrar otro mas
                    self.shiftUp(self.getParentIndex(index))
                    #revisamos tambien con el que se cambio los hijos que tenga si es mayor o menor prioridad que ellos
    def shiftDown(self,index):
        if index>=0:
            actualPriority = self.heap[index][0]
            self.data_dict[self.heap[index][1]] = index
            if self.hasLeftChild(index) and self.hasRightChild(index):
                leftChild = self.getLeftChildIndex(index)
                rightChild = self.getRightChildIndex(index)
                if self.heap[leftChild][0] < self.heap[rightChild][0] and self.heap[leftChild][0] < actualPriority:
                    self.swap(leftChild,index)
                    self.shiftDown(leftChild)
                else:
                    if self.heap[rightChild][0] < actualPriority:
                        self.swap(rightChild,index)
                        self.shiftDown(rightChild)
            elif self.hasLeftChild(index):
                leftChild = self.getLeftChildIndex(index)
                if self.heap[leftChild][0] < actualPriority:
                    self.swap(leftChild,index)
                    self.shiftDown(leftChild)
            elif self.hasRightChild(index):
                rightChild = self.getRightChildIndex(index)
                if self.heap[rightChild][0] < actualPriority:
                    self.swap(rightChild,index)
                    self.shiftDown(rightChild)



    def __str__(self,index,data, priority):
        pass 
    """print("Agregado {} en la posicion {} con la prioridad {}".   format(data,index,priority))
        print(self.heap)
        print(self.data_dict)"""
        
        



    # Extract element with lowest priority value
    # Return the element as tuple (priority, data)
    def extract(self):
        if self.heap:
            if self.size == 1:
                minTerm = self.heap.pop()
                self.size-=1
                return minTerm
            else:
                self.passToLast()
                minTerm = self.heap.pop()
                self.size-=1
                self.data_dict.pop(minTerm[1])
                if self.size>0:
                    self.shiftDown(0)
                return minTerm
        return
            

    def passToLast(self):
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1],self.heap[0]
    # Return the element with lowest priority
    # as a tuple (priority, data)
    # DO NOT REMOVE from queue
    def peek(self):
        pass

    # Return number of elements in the queue
    def __len__(self):
        pass

    # Return True if queue is empty, False otherwise
    def is_empty(self):
        # Return queue is empty
        pass

pq = PriorityQueue()
pq.insert_or_update(1,'1')
pq.insert_or_update(4,'4')
pq.insert_or_update(2,'2')
pq.insert_or_update(3,'3')
pq.insert_or_update(6,'6')
pq.insert_or_update(5,'5')
print(pq.heap)
pq.extract()
pq.insert_or_update(2,'1')
pq.extract()
pq.extract()
pq.extract()
pq.extract()
pq.extract()
print(pq.extract())
print(pq.extract())
print(pq.heap)
print(pq.data_dict)

