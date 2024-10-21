def outer_function():
   x = 99
   def inner_function():
       print(x)
   return inner_function

yoyo = outer_function()


yoyo() 