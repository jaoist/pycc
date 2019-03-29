import pizza

pizza.make_pizza(16, 'sausage')
pizza.make_pizza(20, 'ham', 'pineapple')

# We can import specific functions from a module, and give functions and 
# modules aliases.

from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p

# Import all functions by using 'from <module> import *'
from pizza import *