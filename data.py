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


print '\n'
test1 = BCdata[['James', 'Seong', 'Andrew']]
print test1

print '\n'

test2 = BCdata[['James', 'Alice']]
print test2

result = test1 + test2
print BCdata.notnull()
print '\n'
print result
print '\n'
print result.notnull()

#Notice that because Seong, Andrew, and Alice were not found in both Series, they were returned with NULL/NaN values.
#NULL checking can be performed with usnull and notnull


#DATA FRAME---------------------------------------------------------------------------------------------------------------

nbadata = {'year': [2010,2011,2012,2013,2014,2015],
	   'team': ['Los Angeles Lakers', 'Dallas Mavericks', 'Miami Heat', 'Miami heat', 'San Antonio Spurs', 'Golden State Warriors'],
	   'wins': [57, 57, 46, 66, 62, 67],
	   'losses': [25, 25, 20, 16, 20, 15]}

nba = pd.DataFrame(nbadata, columns=['year', 'team', 'wins', 'losses'])
print nba


