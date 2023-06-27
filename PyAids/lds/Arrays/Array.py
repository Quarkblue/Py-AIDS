# magic methods: __setitem__, __getitem__, __repr__, __len__, __iter__
# all magic methods not to be included in documentation

class Array:
    """
    Creates an array of a given size and type.
    """
    def __init__(self, size: int, aType: str):
        """
        Parameters
        ----------
        size: int
            size of array
        aType: str
            type of elements in array
        """
        self._size = size
        self._array = [None] * size
        self._type = aType
    
    def __setitem__(self, index: int, obj):
        if index < 0 or index >= self._size or index >= len(self._array):
            
            raise IndexError("Index out of range")
        elif not isinstance(obj, self._type):
            raise TypeError(f"Type Error: {self._type} expected, got {type(obj)}")
        else:
            self._array[index] = obj
    
    def __getitem__(self, index: int):
        if index < 0 or index >= self._size or index >= len(self._array):
            raise IndexError("Index out of range")
        else:
            return self._array[index]
        
    def __repr__(self):
        return str(self._array)
    
    def __len__(self):
        return len(self._array)
    
    def __iter__(self):
        return iter(self._array)
    
    def getType(self):
        """
        Returns the type of the array
        """
        return self._type
    
    def getSize(self):
        """
        Returns the size of the array
        """
        return self._size
    
    def toList(self):
        """
        Returns the array as a list
        """
        return self._array
    
    def join(self, sep: str = " "):
        """
        Returns the array as a string with the given separator
        ...or a space if no separator is given
        ----------
        Parameters
        ----------
        sep: str
            separator
        """
        joined = ""
        for i in range(len(self._array)):
            joined += str(self._array[i]) + sep
        
        if sep == " ":
            return joined.strip()
        else:
            return joined[:-len(sep)]
        
    def index(self, item):
        """
        Returns the index of the given item
        ----------
        Parameters
        ----------
        item: any
            item to find index of
        """
        return self._array.index(item)
    
    def reverse(self):
        """
        Returns a reversed array
        """
        return self._array.reverse()
    
    def sort(self, reverse: bool = False):
        """
        Returns a sorted array
        """
        return self._array.sort(reverse=reverse)
    
    
    def pop(self, index: int = None):
        """
        Removes and returns the last item in the array if no index is given
        ----------
        Parameters
        ----------
        index: int
            index of item to remove
        """
        if index is None:
            return self._array.pop()
        else:
            return self._array.pop(index)
        
        
    def push(self, item):
        """
        Addes an item to the end of the array
        ----------
        Parameters
        ----------
        item: any
            item to add to the array
        """
        self._array.append(item)
        
    def shift(self):
        """
        Returns and removes the first item in the array and decrements the size
        """
        return self._array.pop(0)
    
    def unshift(self, item):
        """
        Addes the item to the beginning of the array and increments the size
        """
        if(len(self._array) == self._size):
            self._size += 1
        self._array.insert(0, item)
        
        
        
        
    
    
        
        

