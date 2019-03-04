# generate random Gaussian values
from random import seed
from random import gauss
# seed random number generator
seed(1)
# generate some Gaussian values
for _ in range(10):
	value = gauss(0, 1)
	print(value)