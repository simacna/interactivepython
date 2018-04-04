# *args  = accepts 0 or more arguments

def takes_any_args(*args):
  #args will be a tupule - immutable list
  print("Type of args: " + str(type(args)))
  print("Value of args: " + str(args))

# takes_any_args((5,4,3,2,1), ["list"])

#arg unpacking

def normal_function(a,b,c):
  print("a:{} b: {} c:{}".format(a,b,c))

numbers = {"a": 7, "b":5, "c": 3}
# normal_function(**numbers)

def max_even(*args):
  biggest = -1000
  for idx in args:
    if idx > biggest and (idx % 2 == 0):
      biggest = idx

  return biggest
# print(max_even(2, 3, 9, 11, 7, 8, 13, 21))


