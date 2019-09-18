import scipy.stats as s
import matplotlib.pyplot as plt
import numpy as np

wei = s.weibull_min(2, 0, 2) # shape, loc, scale - creates weibull object
sample = wei.rvs(1000)
shape, loc, scale = s.weibull_min.fit(sample, floc=0)

x = np.linspace(np.min(sample), np.max(sample))
dx = x[1]-x[0]
deriv = np.diff(wei.cdf(x))/dx
plt.hist(sample, density=True, fc="none", ec="grey", label="frequency")
plt.plot(x, wei.cdf(x), label="cdf")
plt.plot(x, wei.pdf(x), label="pdf")
plt.plot(x[1:]-dx/2, deriv, label="derivative")
plt.legend(loc=1)
plt.show()