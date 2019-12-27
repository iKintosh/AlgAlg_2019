from itertools import product

import numpy as np


class MultiPolus:
    def __init__(self, n):
        self.n = n
        self.num_of_gate = n
        self.num_of_outputs = 0
        self.inputs = self._create_input(self.n)
        self.outputs = ''
        self.gates = ''
        self.truth_table = np.zeros((2 ** (2 ** n), 2 ** n), dtype=np.int8)
        self.truth_table_set = set()

        self.truth_table[0: self.n] = self.inputs.astype(np.bool)
        self.add_inputs_to_truth_table_set()

    def __str__(self):
        return self.gates + self.outputs

    def _create_input(self, n):
        lst = []
        for i in range(n):
            lst.append([0, 1])
        return np.array(list(product(*lst))).T

    def add_inputs_to_truth_table_set(self):
        for i in self.inputs:
            self.truth_table_set.add(tuple(i))

    def get_negative(self):
        for i in range(self.num_of_gate):
            candidate = ~self.truth_table[i].astype(np.int8) + 2
            if tuple(candidate) not in self.truth_table_set:
                self.truth_table_set.add(tuple(candidate))
                self.truth_table[self.num_of_gate] = candidate
                self.gates += f'GATE {self.num_of_gate} NOT {i}\n'
                self.outputs += f'OUTPUT {self.num_of_outputs} {self.num_of_gate}\n'

                self.num_of_gate += 1
                self.num_of_outputs += 1

    def get_and(self):
        for size in range(self.n):
            len_gate = self.num_of_gate
            for i in range(len_gate):
                for j in range(len_gate):
                    candidate = self.truth_table[i] & self.truth_table[j]
                    if tuple(candidate) not in self.truth_table_set:
                        self.truth_table_set.add(tuple(candidate))
                        self.truth_table[self.num_of_gate] = candidate
                        self.gates += f'GATE {self.num_of_gate} AND {i} {j}\n'
                        self.outputs += f'OUTPUT {self.num_of_outputs} {self.num_of_gate}\n'

                        self.num_of_gate += 1
                        self.num_of_outputs += 1

    def get_or(self):
        for size in range(int(self.n / 2) + 1):
            len_gate = self.num_of_gate
            for i in range(len_gate):
                for j in range(len_gate):
                    candidate = self.truth_table[i] | self.truth_table[j]
                    if tuple(candidate) not in self.truth_table_set:
                        self.truth_table_set.add(tuple(candidate))
                        self.truth_table[self.num_of_gate] = candidate
                        self.gates += f'GATE {self.num_of_gate} OR {i} {j}\n'
                        self.outputs += f'OUTPUT {self.num_of_outputs} {self.num_of_gate}\n'

                        self.num_of_gate += 1
                        self.num_of_outputs += 1
                        if self.num_of_outputs == (2 ** (2 ** self.n) - self.n):
                            break


if __name__ == '__main__':
    bit_number = int(input())
    p = MultiPolus(bit_number)
    p.get_negative()
    p.get_and()
    p.get_or()
    print(p)
