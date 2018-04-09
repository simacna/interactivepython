class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def lists(self):
         return self.items

     def size(self):
         return len(self.items)

# {{([][])}()}

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        print('symbol', symbol)
        # print("symbol index", symbolString.index(symbol))
        if symbol in "([{":
            s.push(symbol)
        else:
            # print(s.lists())
            if s.isEmpty(): #don't understand purpose
                 balanced = False #how can index < len and not be empty
            else:
                top = s.pop()
                # print('top', top)
                # print('bottom', symbol)
                # how does symbol return end lists
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# print(parChecker('{{([][])}()}'))

#function object

def f(n): return n+2
#f is both a function and a variable and that variable is holding a function object (can store objects in variables)

# print(id(f)) -  everything has a number in python
g = f
# print(g(3))

nums = ['12', '7', '30', '14', '3']
#how can you find the element with biggest numeric value? 
#the max builtin does not help >> max(nums) => '7'

def max(items):
  biggest = items[0]
  for item in items[1:]:
    if int(item) > int(biggest):
      biggest = item
  return biggest
# print(max(nums))

#max by absolute value

def max_by_abs(items):
  biggest = items[0]
  for item in items[1:]:
    if abs(item) > abs(biggest):
      biggest = item
  return biggest

def get_gpa():
  return who["gpa"]

# sorted(students, key=get_gpa)

#max(), min() etc take key functions i.e. min(nums, key=int)

#the above functions are very similar, how do we resolve the dilema - one line of difference

"""
if int(item) > int(biggest):
if abs(item) > abs(biggest):
if item["gpa"] > biggest["gpa"]:
"""
