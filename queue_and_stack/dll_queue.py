import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def enqueue(self, value):
    self.storage.append(value)
    self.size = len(self.storage)
    # pass
  
  def dequeue(self):
    if len(self.storage) > 0:
      self.size = len(self.storage)- 1
      return self.storage.pop(0)
    #pass

  def len(self):
    return self.size
    # pass
