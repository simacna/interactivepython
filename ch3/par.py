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
test = Stack()
test.push([1])
# print(test.size())

def par(pars):
    balanced = True
    s = Stack()
    index = 0

    while index < len(pars) and balanced:
        item = pars[index]
        if item == '(':
            s.push(item)
        else:
            s.pop()

        index = index + 1

    if s.isEmpty() and balanced:
        if (matches(pars)):
            return True
        else:
            return False
    else:
        return False

def matches(inp):
  first_half = len(inp)//2
  first_half_list = inp[0:first_half]
  second_half_list = inp[first_half:]
  weighted = True
  index = 0
  print('first half list', first_half_list)
  print('second half list', second_half_list)
  s = Stack()
  a = []
  for idx in range(second_half_list):
    a = s.pop

  # if (len(inp)%2 = 0):
  #   while index < len(inp):
  #     if (inp[index] and )
  if (first_half_list == second_half_list):
    return True
  else:
    return False
# print(matches([1,1,2,2]))
# print(matches('[()]'))
# print(matches('{{([][])}()}'))
# print(matches('[{()]'))
# print(matches('{{([][])}()}'))
# print(matches('[{()]'))

# print(par('((()))'))
# print(par('(()'))

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol == "(":
#             s.push(symbol)
#             # print('s.push')
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()

#         index = index + 1

#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False

# print(parChecker('((()))'))
# print(parChecker('(()'))

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
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
# print(parChecker('[{()]'))

# print(//2)

def numtobin(input):
  s = Stack()
  iterate = input
  print('outter it', iterate)
  while(iterate > 1):
  # if iterate > 1:
    # print('inner iterate', iterate)
    iterate = (input//2)
    print('inner iterate', iterate)
    s.push(iterate%2)
    # s.push(iterate)
  return s.lists()
# print(numtobin(42))
# print(2)

def divideBy2(decNumber):
    # remstack = Stack()
    final = []
    rev = []
    while decNumber > 0:
        rem = decNumber % 2
        final.append(rem)
        decNumber = decNumber // 2

    for x in final:
      rev.append(x)
    return final.reverse()

print(divideBy2(42))




