import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

fig = plt.figure()
ax = fig.add_subplot(111)

TRIALS = 5000
n = len(tips)

X_ = []

for i in range(TRIALS):
    X = np.random.normal(20.0, np.std(tips, ddof=1), n)
    X_.append(np.mean(X))

greater = np.sum(X_ >= np.mean(tips))

print "observed mean = %f" % np.mean(tips)
print "num greater than mean(tips) = %d" % greater
print "p-value from bootstrapping (ratio of X_ >= mean(tips)) is %1.4f" % (2 * float(greater)/float(TRIALS))

