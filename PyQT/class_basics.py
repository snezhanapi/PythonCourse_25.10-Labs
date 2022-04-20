# # the base class
# class Parent:
#   def __init__(self,*args, **kwargs):
#     print(f'{self} constructor execute')
#     print(args) # (())
#     print(kwargs) # {a:3,b:4}

# # the derived class, which inherits from base class:
# class Child(Parent):
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)

# p1 = Parent(1,2,a=3,b=4)
# c = Child(5,6,c=7,d=8)


# pass function to methods
def onBtnLogInClick():
  print('btnLogIn was clicked')
  # return None

class Button:
  def connect(self, f, x):
    print(f)
    if x%2==0:
      f()


btnLogIn = Button()
btnLogIn.connect( onBtnLogInClick, 9 )
btnLogIn.connect( onBtnLogInClick, 8 )