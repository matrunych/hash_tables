import math


class HashTable:
    def __init__(self, hash_type, values):
        self.values = values
        self.type = type
        if hash_type == 1:
            self.hash_table = ChainedHashDivision(values)

        elif hash_type == 2:
            self.hash_table = ChainedHashMultiply(values)

        elif hash_type == 3:
            self.hash_table = OpenAdressHash(values)

        elif hash_type == 4:
            self.hash_table = OpenAdressHashSquare(values)

        else:
            self.hash_table = OpenAdressHashDouble(values)

        for el in range(len(values)):
            self.hash_table.insert(el)
        print(self.values[2])

    def get_collisions_amount(self):
        return self.hash_table.collisions

    def search(self, number):
        return self.hash_table.search(number)

    def find_sum(self, s):
        for x in range(1, len(self.values)):
            if self.hash_table.search(s - x):
                return x, s - x
        return None


class ChainedHashDivision:
    def __init__(self, values):
        self.values = values

        self.h_table = [[] for i in range(len(values))] if math.log(len(values), 2) != int(math.log(len(values), 2)) \
            else [[] for i in range(len(values) + 1)]

        self.size = len(self.h_table)

        self.collisions = 0

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        if self.h_table[index] != None or self.h_table[index] != False:
            self.collisions += 1
        self.h_table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        if key in self.h_table[index]:
            return True
        return False


class ChainedHashMultiply(ChainedHashDivision):
    def hash(self, key):
        A = (math.sqrt(5) - 1) / 2
        return int(self.size * (key * A % 1))


class OpenAdressHash:
    def __init__(self, values):
        self.values = values
        self.collisions = 0
        self.h_table = [[] * int(len(values) * 1.2)]
        self.size = len(self.h_table)

        self.h_table = [None for i in range(len(values) * 3)] if math.log(len(values) * 3, 2) != int(
            math.log(len(values) * 3, 2)) \
            else [None for i in range(len(values) * 3 - 1)]  # size

        self.size = len(self.h_table)

    def hash(self, key, i):
        return ((key % self.size) + i) % self.size

    def insert(self, key):
        ind = self.hash(key, 0)
        for i in range(self.size):
            next_ind = (ind + i) % self.size
            if self.h_table[next_ind] is None or self.h_table[(ind + i) % self.size] is False:
                self.h_table[next_ind] = key
                break
            else:
                self.collisions += 1

    def search(self, key):
        index = self.hash(key, 0)
        for i in range(self.size):
            if self.h_table[(index + i) % self.size] == key:
                return True
            else:
                return False


class OpenAdressHashSquare(OpenAdressHash):
    def hash(self, key, i):
        return ((key % self.size) + i * 2 + i ** 2 * 3) % self.size


class OpenAdressHashDouble(OpenAdressHash):
    def hash2(self, k):
        return 5 - (k % 5)

    def hash(self, key, i):
        hash2 = self.hash2(key)
        return (key % self.size + i * hash2) % self.size


if __name__ == "__main__":
    import random

    # sequence = [i for i in range(100)]
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    # for i in range(100):
    # values.append(random.choice(sequence))
    a = list(range(2, 101))
    random.shuffle(a)
    h = HashTable(1, a)
    print(h.find_sum(5))
    # t = HashTable(1, values)
    #
    # print(t.search(3))
    # print(t.find_sum(7))
    #
    # print(t.get_collisions_amount())
