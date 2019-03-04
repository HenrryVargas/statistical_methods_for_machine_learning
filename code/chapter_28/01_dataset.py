# generate data samples
from numpy.random import seed
from numpy.random import rand
# seed the random number generator
seed(1)
# generate two sets of univariate observations
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
# summarize
print('data1: min=%.3f max=%.3f' % (min(data1), max(data1)))
print('data2: min=%.3f max=%.3f' % (min(data2), max(data2)))