import numpy as np
#Date and time in Numpy
#we can get the date in a numpy array in a particular format i.e year-month-day by using numpy.datetime64() method.
date = np.array(np.datetime64('2019-08-26'))
print(date)
d1 = np.array(['2007-07-13', '2006-01-13', '2010-08-13'], dtype='datetime64')
print(d1)
d2= np.array(['2001-01-01T12:00', '2002-02-03T13:56:03.172'], dtype='datetime64')
print(d2)

d3=np.arange('2005-02', '2005-03', dtype='datetime64[D]')  # add all dates of a month
print(d3)

#The arguments for timedelta64 are a number, to represent the number of units, and a date/time unit, such as (D)ay, (M)onth, (Y)ear, (h)ours, (m)inutes, or (s)econds.
d4=np.timedelta64(1, 'D')
print(d4)

d5=np.datetime64('2009-01-01') - np.datetime64('2008-01-01')
print(d5)

d6=np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')
print(d6)

d7 = np.timedelta64(1,'W') % np.timedelta64(10,'D')
print(d7)

#The timedelta64 data type also accepts the string “NAT” in place of the number for a “Not A Time” value.
d8=np.datetime64('nat') - np.datetime64('2009-01-01')
print(d8)