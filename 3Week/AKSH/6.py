def f(**kwargs):
#    print(kwargs['name'], kwargs['lname'])
      for key in kwargs:
          print(key, kwargs[key])
f(name = 'Askar', lname = 'Akshabaev')