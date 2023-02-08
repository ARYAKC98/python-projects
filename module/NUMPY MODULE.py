import numpy

a = numpy.arange(6)
a2 = a[numpy.newaxis,:]
print(a2.shape)