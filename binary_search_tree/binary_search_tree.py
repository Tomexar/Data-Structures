import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True
    elif target < self.value:
      if self.left:
        return self.left.contains(target)
      else:
        return False
    elif target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    temp = self
    while temp.right is not None:
      temp = temp.right
    return temp.value

  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)