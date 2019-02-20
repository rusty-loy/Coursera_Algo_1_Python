'''
Created on Feb 19, 2019

@author: Rusty
'''

class LLNode:
    """ Link list node implementation """
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


if __name__ == '__main__':
    print('Hello')
    