import numpy as np
import matplotlib.pyplot as plt
import math


def binomial_func(trials, P_success=1/4, P_fail=3/4):
    res = np.zeros((trials + 1))
    for successes in range(trials + 1):
        res[successes] = math.comb(trials, successes) * (P_success ** successes) * (P_fail ** (trials - successes))
    return res



plt.plot(binomial_func(90))
plt.plot(binomial_func(100))
plt.plot(binomial_func(110))
plt.legend(['90 trials plot', '100 trials plot', '110 trials plot'])
plt.title('Binomial distribution with P(success)=1/4')
plt.show()