#housing.data was obtained from http://archive.ics.uci.edu/ml/machine-learning-databases/housing/

import matplotlib.pyplot as pl

MEDV = []
TAX = []
PTRATIO = []
LSTAT = []

housingData = open('housing.data', "r")

#saving relevant values from each line using the lists initialized above.
for line in housingData:
	value = line.split()
	MEDV.append(value[13])
	TAX.append(value[9])
	PTRATIO.append(value[10])
	LSTAT.append(value[12])

ylabel = 'Median value of owner-occupied\nhomes in $1000\'s'

xlabels = ['full-value property-tax rate per $10,000',
           'pupil-teacher ratio by town',
           '% lower status of the population']

titles = ['tax rate vs.\nmedian house value',
          'pupil-teacher ratio vs.\nmedian house value',
          'lower status of the population\nvs. median house value']

xdata = [TAX, PTRATIO, LSTAT]
ydata = MEDV

for i in range(3):
        pl.subplot(2,2,i+1)
        pl.scatter(xdata[i], ydata)
        pl.title(titles[i])
        pl.xlabel(xlabels[i])
        pl.ylabel(ylabel)
        pl.grid()

# To make everything fit nicely with no overlaps.
pl.tight_layout()
pl.show()

