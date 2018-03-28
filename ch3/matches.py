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
        # print('symbol', symbol)
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
                print('bottom', symbol)
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

print(parChecker('{{([][])}()}'))