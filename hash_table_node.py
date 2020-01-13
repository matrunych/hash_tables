import math


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, hash_type, values):
        if hash_type == 1:
            self.hash_table = ChainedHash(hash_type, values)

        elif hash_type == 2:
            self.hash_table = ChainedHashMultiply(hash_type, values)

        elif hash_type == 3:
            self.hash_table = OpenAdressHash(hash_type, values)

        elif hash_type == 4:
            self.hash_table = OpenAdressHashSquare(hash_type, values)

        else:
            self.hash_table = OpenAdressHashDouble(hash_type, values)

        for el in values:
            self.hash_table.insert(el)



    def get_collisions_amount(self):
        amount = 0
        for el in self.hash_table.h_table:
            if el == None:
                amount += 1
        return amount + len(self.hash_table.values) - self.hash_table.size

    def search(self, number):
        return self.hash_table.search(number)

    def find_sum(self, s):
        for x in range(s // 2 + 1):
            y = s - x
            if self.hash_table.search(x) and self.hash_table.search(y):
                if x + y == s:
                    return x, y


class DefaultHashTable:
    def __init__(self, hash_type, values):
        self.values = values

        def find_closest(number):
            prime_found = False

            for i in range(2, int(math.sqrt(number) + 2)):
                if number % i == 0:
                    break
                if i == int(math.sqrt(number) + 1):
                    prime_found = True
                    break

            if prime_found:
                # print(number)
                return number

            # number -= 1

            return number

        # print(len(values) * 3 - 1)
        self.size = find_closest(len(values) * 3 - 1)
        # print(self.size)



        self.hash_type = hash_type

        self.h_table = [None for el in range(self.size)]


class ChainedHash(DefaultHashTable):
    # def __init__(self, hash_type, values):
    #     super(ChainedHash, self).__init__(hash_type, values)

    def hash(self, key):
        return key % self.size

    def insert(self, value):
        cur_node = self.h_table[self.hash(value)]
        if cur_node:
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(value)
        else:
            self.h_table[self.hash(value)] = Node(value)

    def search(self, value):
        cur_node = self.h_table[self.hash(value)]
        if cur_node:
            while cur_node.next:
                if cur_node.value == value:
                    return True
                cur_node = cur_node.next
            if cur_node.value == value:
                return True
        return False


class ChainedHashMultiply(ChainedHash):
    # def __init__(self, hash_type, values):
    #     super(ChainedHashMultiply, self).__init__(hash_type, values)

    def hash(self, key):
        A = 0.6180339887 #(math.sqrt(5) - 1)/2
        return int(self.size * (key * A % 1))


class OpenAdressHash(DefaultHashTable):
    # def __init__(self, hash_type, values):
    #     super(OpenAdressHash, self).__init__(hash_type, values)

    def hash(self, key, i):
        return ((key % self.size) + i) % self.size

    def insert(self, value):
        i = 0
        index = self.hash(value, i)
        cur_node = self.h_table[index]
        if cur_node != None:
            while self.h_table[index + i] != None:
                i += 1
            self.h_table[index + i] = value
        else:
            self.h_table[index] = value

    def search(self, value):
        i = 0
        index = self.hash(value, i)
        cur_node = self.h_table[index]
        if cur_node != None:
            while self.h_table[(index + i) % self.size] != value:
                if self.h_table[(index + i) % self.size] == None:
                    return False
                i += 1
            return True
        else:
            return False



class OpenAdressHashSquare(OpenAdressHash):
    # def __init__(self, hash_type, values):
    #     super(OpenAdressHashSquare, self).__init__(hash_type, values)

    def hash(self, key, i):
        return ((key % self.size) + i * 2 + i ** 2 * 3) % self.size


class OpenAdressHashDouble(OpenAdressHash):
    # def __init__(self, hash_type, values):
    #     super(OpenAdressHashDouble, self).__init__(hash_type, values)

    def hash(self, key, i):
        A = 0.6180339887
        return (key % self.size + i + (int(self.size * (key * A % 1)))) % self.size

import random


a = list(range(1, 101))
random.shuffle(a)
h = HashTable(1, a)
print(h.find_sum(5))
