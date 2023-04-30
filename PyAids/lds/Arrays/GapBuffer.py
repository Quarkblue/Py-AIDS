class GBuffer:
    
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.bufferStr = ""
        
    def toString(self):
        for i in self.buffer:
            if i != None:
                self.bufferStr += i
                
        return self.bufferStr
        
    def __str__(self):
        return str(self.buffer)
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        return self.buffer[index]
    
    
    def insert(self, value, index: int = None):
        if index == None:
            index = self.getGapIndex()
            
        if(index >= self.size or index < 0 ):
            raise IndexError("Index out of range")
        
        elif(self.getGapSize() == 0):
            self.growGap(index)
            self.insert(value, index)
        
        elif(self.buffer[index] != None):
            self.reduceGap(self.getGapSize())
            self.growGap(index)
            self.insert(value, index)
            
        elif(len(value) > self.getGapSize()):
            self.growGap(index)
            self.insert(value, index)
            
        elif(self.buffer[:index].count(None) > 0 and self.buffer[index:].count(None) > 0 and index != 0):
            index = self.getGapIndex()
            self.insert(value, index)
        else:
            for i in range(len(value)):
                self.buffer[index] = value[i]
                index += 1
    
    
    def reduceGap(self, size):
        self.buffer = self.buffer[:self.getGapIndex()] + self.buffer[self.getGapIndex()+size:]
    
    def reposeGap(self, index):
        if(index >= self.size or index < 0 ):
            raise IndexError("Index out of range")
        else:
            gapSize = self.getGapSize()
            self.reduceGap(gapSize)
            self.growGap(index, gapSize)
            
    
    def getGapSize(self):
        return self.buffer.count(None)
        
    def getGapIndex(self):
        return self.buffer.index(None)
    
    
    def growGap(self, index, size: int = None):
        if(size == None):
            size = self.size
        self.buffer = self.buffer[:index] + [None]*size + self.buffer[index:]
        
        
    def move_gap(self, distance: int):
        if isinstance(distance, int):
            if distance > 0 and distance < len(self.buffer[self.getGapIndex() + self.getGapSize() + 1:]):
                self.reposeGap(self.getGapIndex() + distance)
            elif distance < 0 and distance < len(self.buffer[:self.getGapIndex()]):
                distance = abs(distance)
                self.reposeGap(self.getGapIndex() - distance)
            else:
                raise ValueError("Distance out of range")
        
    def get_text(self):
        res = ""
        for i in range(len(self.buffer)):
            if self.buffer[i] == None:
                res += " "
            else:
                res += self.buffer[i]
        
        return res
    