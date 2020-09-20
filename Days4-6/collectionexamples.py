from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

user = ('bob', 'coder')

User = namedtuple('User', 'name role')

user = User(name='chris', role='coder')

print(user.name)
print(user.role)

