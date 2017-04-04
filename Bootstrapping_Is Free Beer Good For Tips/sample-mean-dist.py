import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

fig = plt.figure()
ax = fig.add_subplot(111)

plt.axis([18.0, 22.0, 0.0, 1.6])
x = np.arange(18.0, 22.0, 0.001)
y = stats.norm.pdf(x, 20, np.std(tips, ddof=1)/math.sqrt(len(tips)))

plt.plot(x, y, color = 'red')
plt.xlabel("Average tip %")
plt.ylabel("Density")
plt.suptitle("$Tips control (H0) sample mean density N(20, s^2/n)")
plt.text(np.mean(tips), 0.09, '$Sample Mean = %2.3f$' % np.mean(tips))
plt.plot(np.mean(tips), 0, 'd')

plt.show()