import matplotlib.pyplot as plt
import numpy as np

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7]

fig = plt.hist(tips, bins = 5, normed = 1)
plt.xlabel("Tip %")
plt.ylabel("Density")
plt.suptitle("Sample Tips after Free Beer")
plt.text(18.5, 0.30, '$Sample Mean = %2.3f$' % np.mean(tips))
plt.show()
