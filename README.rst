Type corrector
==============

This project has merged with typesys and will no longer be maintained.
Typesys can be found `here <https://github.com/fredgj/typesys>`_.

Intro
-----

Type corrector is a module that contains the decorator type_corrector.
This decorator lets the user specify what types the 
arguments to a function should have. It's not 100% safe to use as it
might result in a ValueError or TypeError if the user is not careful enough.
The motivation behing this module was to find a way that makes it easier
for the programmer to see what types the arguments should be, and at 
the same time allow some margin of error.
I'm not sure whether this is a good idea or not, or if it's a good approach. It was
mostly developed for fun while playing around with decorators.


Installation
------------

pip install typecorrector


Usage
-----

First import type_corrector from the typecorrector module:

.. code:: python

    from typecorrector import type_corrector

Then you can decorate your functions with type_corrector

.. code:: python

    @type_corrector(int, int)
    def add(x,y):
        return x+y

    
    @type_corrector(float, float)
    def div(x,y):
        return x/y
       

A call to add(1,'2') will cast '2' to an int, since that is what we
specified as the type of the second paramater in the decorator.
We can also call div as div('10', '3'), and div will return 3.3333333333333335
as expected.

This decorator also works with \*args and \*\*kwargs

.. code:: python

    @type_corrector(int)
    def mult(*numbers):
        result = 1
        for num in numbers:
            result *= num
        return result


    @type_corrector(int)
    def kw_mult(**kwargs):
        first = kwargs.get('first')
        second = kwargs.get('second')
        third = kwargs.get('third')
        return first * second * third


This allows us to call the functions like this:

- mult('2', '3', '4') 
- kw_mult(first='2', second='3', third='4')

When looking at the function definitions of add, mult and kw_mult we can easily
see that the arguments are supposed to be integers.
By decorating the functions like this it should be a clear
hint what types we want the parameters to be passed in as, even though it 
allows some margin of error.


Known issues
------------

- When calling help on a decorated function the parameters are not shown
  correctly, instead it will just say <function name>(\*args, \*\*kwargs).
  Thanks to the functools.wraps decorator the docstring of a wrapped function
  will still be shown correctly.
- When using the inspect module to get the argument specification with
  inspect.getargspec or getting the source code from inspect.getsourcelines
  it will fail and show the wrapped function instead.


Bugs, problems and new features
-------------------------------

If you find any bugs, have any problems, or maybe you just want to request a 
new feature, then use the `issue tracker
<https://github.com/fredgj/typecorrector/issues>`_.

