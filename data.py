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
bostoncollege3 = pd.Series({'James': 'A&S', 'Seong': 'CSOM', 'Andrew': 'CSOM', 'John': 'CSOM', 'Alice': 'A&S'})
print bostoncollege3


print bostoncollege3['James']
print '\n'
print bostoncollege3[['James','Seong','Andrew']]
print '\n'

print bostoncollege3[bostoncollege3 == 'A&S']

conditions = bostoncollege3 == 'CSOM'
print conditions
print '\n'
print bostoncollege3[conditions]


print '\n'

print 'James' in bostoncollege3
print 'james' in bostoncollege3

print '\n'
BCdata = pd.Series({'James': 100, 'Seong': 200, 'Andrew': 300, 'John': 400, 'Alice': 500})
print BCdata

print BCdata / 3
print np.square(BCdata)

