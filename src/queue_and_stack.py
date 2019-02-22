'''
Created on Feb 19, 2019

@author: Rusty
'''
from random import randint, shuffle

class LLNode:
    """ Singly link list node implementation """
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_


class LLStack:
    """ Link list node stack implementation """
    def __init__(self):
        self.top = None

    def push(self, item):
        """ Push item onto stack """
        self.top = LLNode(item, self.top)

    def pop(self):
        """ Pop item from top of stack """
        item = self.top.item
        self.top = self.top.next
        return item

    def empty(self):
        """ Return if no more items in stack """
        return self.top is None


class ArrayStack:
    """ Array stack implementation """
    def __init__(self):
        self.items = []

    def push(self, item):
        """ Push item onto stack """
        self.items.append(item)

    def pop(self):
        """ Pop item from top of stack """
        return self.items.pop()

    def empty(self):
        """ Return if no more items in stack """
        return not self.items

    def peek(self):
        """ Return value at top of stack without altering stack state"""
        return self.items[-1]


class QueueWithStacks:
    """ Array stack implementation """
    def __init__(self):
        self.inbox = ArrayStack()
        self.outbox = ArrayStack()

    def enqueue(self, item):
        """ Push item onto stack """
        self.inbox.push(item)

    def dequeue(self):
        """ Pop item from top of stack """
        if self.outbox.empty():
            while not self.inbox.empty():
                self.outbox.push(self.inbox.pop())

        return self.outbox.pop()

    def empty(self):
        """ Return if no more items in stack """
        return self.inbox.empty() and self.outbox.empty()

class StackWithMax(ArrayStack):
    """ Stack class with max function to return the current max """
    def __init__(self):
        super().__init__()
        self.max_stack = ArrayStack()

    def max(self):
        """ Return maximum value in the stack """
        return self.max_stack.peek()

    def push(self, item):
        """ Push item onto stack """
        super().push(item)
        if self.max_stack.empty() or item > self.max():
            self.max_stack.push(item)
        else:
            self.max_stack.push(self.max())

    def pop(self):
        """ Pop item from top of stack """
        self.max_stack.pop()
        return super().pop()


class DLLNode:
    """ Doubly link list node implementation """
    def __init__(self, item, prev, next_):
        self.item = item
        self.prev = prev
        self.next = next_


class LLDeque:
    """ Container class that allows adding and removing from the front or back """
    def __init__(self):
        self.front = None
        self.back = None

    def __iter__(self):
        current_node = self.front
        while current_node:
            yield current_node.item
            current_node = current_node.prev

    def empty(self):
        """ If no items in container """
        return self.front is None

    def add_front(self, item):
        """ Add item to front of container """
        if self.front:
            self.front = DLLNode(item, self.front, None)
            self.front.prev.next = self.front
        else:
            self.front = DLLNode(item, None, None)
            self.back = self.front

    def add_back(self, item):
        """ Add item to back of container """
        if self.back:
            self.back = DLLNode(item, None, self.back)
            self.back.next.prev = self.back
        else:
            self.add_front(item)

    def remove_front(self):
        """ Remove item from front of container """
        item = self.front.item
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.prev

        return item

    def remove_back(self):
        """ Remove item from back of container """
        if self.front == self.back:
            return self.remove_front()

        item = self.back.item
        self.back = self.back.next
        return item


class RandomizedQueue:
    """ Queue that returns an element at a random position """
    def __init__(self):
        self.items = []

    def __iter__(self):
        order_indices = range(len(self.items))
        shuffle(order_indices)

        for index in order_indices:
            yield self.items[index]

    def enqueue(self, item):
        """ Add an item to the queue """
        self.items.append(item)

    def dequeue(self):
        """ Remove an item from queue at a random position """
        index = randint(0, len(self.items) - 1)

        # if random index is end of list, just pop
        if index == len(self.items) - 1:
            return self.items.pop()

        # swap place of end of list with random index
        item = self.items[index]
        self.items[index] = self.items.pop()
        return item

    def empty(self):
        """ Return if no more items in stack """
        return not self.items


if __name__ == '__main__':
    print('Hello')
