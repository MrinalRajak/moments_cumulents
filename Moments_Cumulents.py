# Moments and cumulents

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

xs=np.linspace(-6,6,300)
xs2=np.linspace(stats.lognorm.ppf(0.01,0.7,loc=-0.1),stats.lognorm.ppf(0.99,.7,loc=-.1),150)
# Positively skewed Distribution
lognormal=stats.lognorm.pdf(xs2,0.7)
normal=stats.norm.pdf(xs)
plt.plot(xs2,lognormal,label='skew > 0')
# Negatively skewed Distribution
plt.plot(xs2,lognormal[::-1],label='skew < 0')
plt.legend()
plt.grid(True)
#plt.plot(xs,normal)
plt.show()
