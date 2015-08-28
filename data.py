import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)

bostoncollege = pd.Series(["James", "Seong", "Andrew", "John", "Alice"])
print bostoncollege

bostoncollege2 = pd.Series(["James", "Seong", "Andrew", "John", "Alice"],
              index=['JA', 'S', 'AN', 'JO', 'AL'])
print bostoncollege2

#The Series constructor can convert a dictionary as well, using the keys of the dictionary as its index
bostoncollege3 = pd.Series({'James': 'A&S', 'Seong': 'CSOM', 'Andrew': 'CSOM', 'John': 'CSOM', 'Alice': 'CSOM'})
print bostoncollege3


