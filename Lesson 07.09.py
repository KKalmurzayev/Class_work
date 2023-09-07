class MyIterator:
    def __init__(self, value):
        self.value = value
        self.current = 0

    def __str__(self):
        return "My name is Iterator"

    def __iter__(self):
        print("iteration\n")
        return self
    
    def __next__(self):
        print("next\n")
        if self.current < self.value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(5)
for num in my_iter:
    print(num)