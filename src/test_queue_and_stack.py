'''
Created on Feb 19, 2019

@author: Rusty
'''

import unittest

import queue_and_stack


class CommonTests:
    """ Common tests for all stack implementations """
    
    def test_empty_is_empty(self):
        """ Stack should start out emtpy """
        self.assertTrue(self.stack.empty())

    def test_push(self):
        """ Push should make stack not empty """
        self.stack.push('a')
        self.assertFalse(self.stack.empty())

    def test_single_pop(self):
        """ A push followed by pop should return original item """
        self.stack.push('a')
        self.assertEqual(self.stack.pop(), 'a')

    def test_reverse_order_pop(self):
        """ Two pushes should reverse order when popped """
        self.stack.push('a')
        self.stack.push('b')
        self.assertEqual(self.stack.pop(), 'b')
        self.assertEqual(self.stack.pop(), 'a')

    def _test_strings(self, stack1, stack2, reference):
        """ Push a string unto one stack, then pop to another.  
            When popped again, we should have the original string """
        [stack1.push(x) for x in reference]

        while not stack1.empty():
            stack2.push(stack1.pop())

        test = []
        while not stack2.empty():
            test.append(stack2.pop())
        
        if isinstance(reference, str):
            return ''.join(test)
        else:
            return test

class StackLLTestCase(unittest.TestCase, CommonTests):
    """ Tests for stacks """
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.stack = queue_and_stack.LLStack()
    
    def test_pop_empty(self):
        """ popping an empty linked list give a none type error """
        with self.assertRaises(AttributeError):
            self.stack.pop()

    def test_strings(self):
        """ Try different sequence of characters with the stack """
        self._test_strings(queue_and_stack.LLStack(), queue_and_stack.LLStack(), 
                   'this is a long string!! msjhdtaisdhja  askjdlsjdklasjl END')
        self._test_strings(queue_and_stack.LLStack(), queue_and_stack.LLStack(), 
                           '12345')
        self._test_strings(queue_and_stack.LLStack(), queue_and_stack.LLStack(), '')

class StackArrayTestCase(unittest.TestCase, CommonTests):
    """ Tests for stacks """
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.stack = queue_and_stack.ArrayStack()
        
    def test_pop_empty(self):
        """ popping an empty array gives an index error """
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_strings(self):
        """ Try different sequence of characters with the stack """
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                   'this is a long string!! msjhdtaisdhja  askjdlsjdklasjl END')
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                           '12345')
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                           '')


class StackWithMaxTestCase(unittest.TestCase, CommonTests):
    """ Tests for stacks """
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.stack = queue_and_stack.StackWithMax()

    def test_pop_empty(self):
        """ popping an empty array gives an index error """
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_ints(self):
        """ Try different sequence of characters with the stack """
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                   range(20))
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                           [1,99,5,108,22,87,-22])
        self._test_strings(queue_and_stack.ArrayStack(), queue_and_stack.ArrayStack(), 
                           [1])

    def test_single_max(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.max())

    def test_multiple_max(self):
        pushes = [1, -1, -100, 100, 5, 1234, 666]
        maxes = [1, 1, 1, 100, 100, 1234, 1234]
        
        for item, max in zip(pushes, maxes):
            self.stack.push(item)
            self.assertEqual(max, self.stack.max())
        
        while not self.stack.empty():
            self.assertEqual(maxes[-1], self.stack.max())
            self.stack.pop()
            maxes.pop()

class QueueTestCase(unittest.TestCase):
    """ Tests for queues """
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.queue = queue_and_stack.QueueWithStacks()
  
    def test_empty_is_empty(self):
        """ Queue should start out emtpy """
        self.assertTrue(self.queue.empty())

    def test_enqueue(self):
        """ Enqueue should make queue not empty """
        self.queue.enqueue('a')
        self.assertFalse(self.queue.empty())

    def test_single_dequeue(self):
        """ An enqueue followed by a dequeue should return original item """
        self.queue.enqueue('a')
        self.assertEqual(self.queue.dequeue(), 'a')

    def test_in_order_dequeue(self):
        """ Two enqueues should return items in original order """
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.assertEqual(self.queue.dequeue(), 'a')
        self.assertEqual(self.queue.dequeue(), 'b')

    def test_dequeue_empty(self):
        """ popping an empty queue gives an index error """
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_strings(self):
        """ Try different sequence of characters with the queues.
            Results should be returned back in order """
        def _test(queue, reference):
            [queue.enqueue(x) for x in reference]
            test = []
            while not queue.empty():
                test.append(queue.dequeue())
            
            self.assertEqual(reference, ''.join(reference))
            
        _test(queue_and_stack.QueueWithStacks(), 
              'test long string !!!! askdmaksdklasdja    k !!!!')
        _test(queue_and_stack.QueueWithStacks(), 
              '')

if __name__ == '__main__':
    unittest.main()
