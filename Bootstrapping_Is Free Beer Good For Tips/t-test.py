import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

fig = plt.figure()
ax = fig.add_subplot(111)

m = np.mean(tips)
mu = 20
s = np.std(tips, ddof=1)
N = len(tips)
t = (m - mu)/(s/math.sqrt(N))

p = (1 - stats.t.cdf(t, N-1))
two_p = 2 * p

print "t is %f" % t
print "one-sided p-value is %f" % p
print "two-sided p-value is %f" % two_p
print "p-value (from t-test) = %f, Reject H0" % two_p