from random import choice


class RandomizedSet:
    """
    All function works in average O(1) complexity
    """

    def __init__(self):
        self.val = []
        self.val_dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.val_dict:
            self.val_dict[val] = len(self.val)
            self.val.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_dict:
            last_val = self.val[-1]
            self.val_dict[last_val] = self.val_dict[val]
            self.val[self.val_dict[val]] = last_val
            self.val.pop()
            del self.val_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.val)


obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.remove(2)
