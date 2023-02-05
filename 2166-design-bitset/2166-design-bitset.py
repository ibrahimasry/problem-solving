class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.zeros = set(list(range(size)))
        self.ones = set()
    def fix(self, idx: int) -> None:
        ones,zeros = self.ones,self.zeros
        if idx in self.zeros:
            zeros.remove(idx)
            ones.add(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.ones:
            self.ones.remove(idx)
            self.zeros.add(idx)

        

    def flip(self) -> None:
        self.ones,self.zeros = self.zeros,self.ones
        

    def all(self) -> bool:
        return len(self.zeros) == 0
        

    def one(self) -> bool:
        return len(self.ones) > 0
        

    def count(self) -> int:
        return len(self.ones)
        

    def toString(self) -> str:
        arr = ["0"] * self.size
        for idx in self.ones:
            arr[idx] = "1"
        return ''.join(arr)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()