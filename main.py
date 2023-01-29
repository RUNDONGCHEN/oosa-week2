#task1
import numpy as np
import matplotlib.pyplot as plt
data=np.random.random((10))

def datamin(datasource):
  min = datasource[0]
  for i in datasource:
    if min > i:
      min = i
  return min

def dataSorter(datasource):
  sort = []
  for i in datasource:
    a = datamin(datasource)
    sort.append(a)
    datasource = np.delete(datasource, np.where(datasource == a))
  return sort
#task2

x = list(np.arange(0,len(data)))
y = dataSorter(data)
#plt.plot(x,y)


#task3
def binarySearch(x,v):
  '''Binary search for v in x by looping'''

  # set first break point and ends
  start=0              # the start index
  end=len(x)           # the end index
  midP=(start+end)//2  # the mid point

  # a flag to let us know if the exact number has been found
  foundExact=False

  # loop over
  while((end-start)>1):
    if(x[midP]<v):   # answer is to the right
      start=midP
      midP=(start+end)//2
    elif(x[midP]>v):   # answer is to the left
      end=midP
      midP=(start+end)//2
    elif(x[midP]==v):  # found answer, unlikely
      foundExact=True  # have found exact answer
      break

  # if we have not found the exact answer, find the closest element
  if(foundExact==False):
    sep=np.abs(x[start:end]-v)  # use a slice to find the absolute distance
    midP=sep.argmin()+start     # set mid point as element with smallest distance

  return(midP)


if __name__=="__main__":
  plt.axvline(x = binarySearch(data,0.5), color = 'b', label = 'axvline - full height')
  plt.plot(x,y)
  plt.show()