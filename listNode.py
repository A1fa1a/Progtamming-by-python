#!/bin/python

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedListError(Exception):
  pass

class IndexError(LinkedListError):
  pass

class ElementNotFoundError(LinkedListError):
  pass

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.nodes_count = 0

  def append(self, value):
    new_node = Node(value)

    if not self.head:
      self.head = new_node
    else:
      self.tail.next = new_node

    self.tail = new_node
    self.nodes_count += 1

  def print_nodes(self):
    current_nodes = self.head

    while current_nodes:
      print(current_nodes.value, end=" -> ")
      current_nodes = current_nodes.next

    print("None")

  def get_element(self, index):
    target = self.head

    if index < 0:
      index += self.nodes_count

    if index >= self.nodes_count or index < 0:
      if index < 0:
        index -= self.nodes_count
      raise IndexError(f"'{index}' is out of range")

    for _ in range(index):
      target = target.next

    return target

  def get_index(self, element):
    target = self.head
    index = 0

    while target:
      if target.value == element:
        return index
      target = target.next
      index += 1

    raise ElementNotFoundError(f"'{element}' is not found")

  def remove(self, element):
    previous = None
    current = self.head

    while current and current.value != element:
      previous = current
      current = current.next

    if not current:
      raise ElementNotFoundError(f"'{element}' is not found")

    if previous:
      previous.next = current.next
    else:
      self.head = current.next

    if current == self.tail:
      self.tail = previous

    self.nodes_count -= 1

linked_list = LinkedList()
linked_list.append(4)
linked_list.append(1)
linked_list.append(2)
linked_list.append(7)
linked_list.append(9)
linked_list.append(22)

linked_list.remove(9)
linked_list.print_nodes()
