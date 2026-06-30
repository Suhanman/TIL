my_foods=["apple","banana", "cherry"]

for food in my_foods:
    for food2 in my_foods:
        if food == food2:
            print(f"Skipping duplicate item:{food}")
            continue
        print(f"Cooking {food} with {food2}")
        
class CountTo:
    def __init__(self,max_value):
        self.max =max_value
    def __iter__(self):
        return CountToIterator(self.max)

class CountToIterator:
    def __init__(self,max_value):
        self.max = max_value
        self.current = 1
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current  +=1
            return val
        else:
            raise StopIteration
        
counter = CountTo(5)

for count in counter:
    for count2 in counter:
            print(f"Count: {count} and {count2}")
            
            
def count_up_to(limit):
    print("Generator function started....")
    n = 1
    
    while n <= limit :
        print(f"Yielding {n}")
        yield n
        print(f"Resumed after Yielding {n}")
        n += 1
        
    print("Generator function finished")

count_gen = count_up_to(3)
print(f"Returned object : {count_gen} of type {type(count_gen)}")

print("First call to next outside of for loop.")
next(count_gen)

print("Remaining output from for loop")
for number in count_gen:
    print(number)
