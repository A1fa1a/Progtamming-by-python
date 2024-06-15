#!/bin/python

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.nodesCount = 0

  def append(self, value):
    new_node = Node(value)

    if not self.head:
      self.head = new_node
    else:
      self.tail.next = new_node

    self.tail = new_node
    self.nodesCount += 1

  def print_nodes(self):
    current = self.head
    elements = []
    while current:
      elements.append(current.value)
      current = current.next

    print(elements)

  def get_element(self, index):
    if index < 0:
      index += self.nodesCount
    if index < 0 or index >= self.nodesCount:
      return "IndexError: index is out of range"

    current = self.head

    for _ in range(index):
      current = current.next

    return current.value

  def get_index(self, element):
    current = self.head
    index = 0

    while current:
      if current.value == element:
        return index

      current = current.next
      index += 1

    return f"'{element}' is not found"

  def remove(self, element):
    current = self.head
    prev = None

    while current and current.value != element:
      prev = current
      current = current.next

    if not current:
      return f"'{element}' is not found"

    if prev:
      prev.next = current.next
    else:
      self.head = current.next

    if current == self.tail:
      self.tail = prev

    self.nodesCount -= 1

linked_list = LinkedList()
#linked_list.append(4)
#linked_list.append(1)
#linked_list.append(2)
#linked_list.append(7)
#linked_list.append(9)
#linked_list.append(22)

linked_list.remove(7)
linked_list.print_nodes()  # [4, 1, 2, 9, 22]
