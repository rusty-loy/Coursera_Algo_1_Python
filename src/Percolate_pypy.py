'''
Created on Feb 4, 2019

@author: Rusty
'''
import random
import statistics
import math
from datetime import datetime

class QuickUnion:
    """ Supports union/connection of two nodes.  Quickly finds if two nodes are connected. """
    def __init__(self, size):
        """ Size is the number of nodes in the collection.  All nodes start off
            unconnected. """
        self._parents = list(range(size))
        self._weights = [1] * size

    def _get_root(self, index):
        """ Internal function to find the arbitrary root node of a node """
        parent_index = index
        while parent_index != self._parents[parent_index]:
            self._parents[parent_index] = self._parents[self._parents[parent_index]]
            parent_index = self._parents[parent_index]

        return parent_index

    def connected(self, node1, node2):
        """ Returns True if two nodes are connected (part of the same set) """
        return self._get_root(node1) == self._get_root(node2)

    def union(self, node1, node2):
        """ Connect two nodes.  All nodes that were previously union are maintained.
            This means all nodes that are connected to node1 are now connected to node2. """
        root1 = self._get_root(node1)
        root2 = self._get_root(node2)

        if root1 != root2:
            # Place smaller tree under the larger tree to keep trees balanced
            if self._weights[root1] < self._weights[root2]:
                self._parents[root1] = root2
                self._weights[root2] += self._weights[root1]
            else:
                self._parents[root2] = root1
                self._weights[root1] += self._weights[root2]

class Percolation:
    """ Grid that finds if there is a path from the top row to the bottom row """
    def __init__(self, grid_size):
        """ Grid size will be number of rows and columns.
            (grid = grid_size X grid_size)
            Grid starts in all closed state.
            """
        self.grid_size = grid_size
        # Additional nodes needed to represent top row and bottom row.
        # Top and bottom nodes decide if top row is connected to bottom row.
        self._nodes = QuickUnion((self.grid_size**2) + 2)
        self._top_index = self.grid_size ** 2
        self._bottom_index = self._top_index + 1

        # All nodes start in closed state
        self._open_nodes = [False] * (self.grid_size**2)

    def _get_grid_pos(self, row, col):
        """ Get internal grid index by zero indexed row and column.
            Row and column should be less that grid size"""
        return (row * self.grid_size) + col

    def open(self, row, col):
        """ Make grid passable at zero indexed row and column. """
        pos = self._get_grid_pos(row, col)
        if not self._open_nodes[pos]:
            self._open_nodes[pos] = True
            for neighbor_pos in [pos + 1, pos - 1, pos + self.grid_size, pos - self.grid_size]:
                if 0 <= neighbor_pos < self._top_index:
                    if self._open_nodes[neighbor_pos]:
                        self._nodes.union(neighbor_pos, pos)

            # Connect the top and bottom rows to their respective special node
            if row == 0:
                self._nodes.union(self._top_index, pos)
            if row == self.grid_size - 1:
                self._nodes.union(self._bottom_index, pos)

    def is_open(self, row, col):
        """ If the grid has been opened at position . """
        return self._open_nodes[self._get_grid_pos(row, col)]

    def number_open_sites(self):
        """ Number cells that have been opened """
        return self._open_nodes.count(True)

    def percolates(self):
        """ If the grid has a path from the top to the bottom. """
        return self._nodes.connected(self._top_index, self._bottom_index)

def run_percolation_samples(sample_size, grid_size):
    """ Perform multiple runs of percolation opening random cells.
        This allows us to approximate the average open cells when a grid
        first percoaltes """
    random_size = 1000000
    sizes = []

    def return_random_gen():
        return iter([random.choice(range(grid_size)) for _ in range(random_size * 2)])

    for _ in range(sample_size):
        perc = Percolation(grid_size)
        rand_num_gen = return_random_gen()

        counter = 0
        while not perc.percolates():
            counter += 1
            row, col = next(rand_num_gen), next(rand_num_gen)
            perc.open(row, col)

            if counter > (random_size - 10):
                counter = 0
                rand_num_gen = return_random_gen()

        sizes.append(perc.number_open_sites() / grid_size**2)

    mean = statistics.mean(sizes)
    stdev = statistics.stdev(sizes)
    confidence_unit = (1.96 * stdev) / math.sqrt(sample_size)
    confidence_95 = (mean - confidence_unit, mean + confidence_unit)
    print(mean)
    print(stdev)
    print(confidence_95)

if __name__ == '__main__':
    START = datetime.now()

    run_percolation_samples(2, 1000)
#     import cProfile
#     cProfile.run('run_percolation_samples(sample_size, grid_size)')

    print(datetime.now() - START)
