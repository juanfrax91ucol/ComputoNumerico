#
# Distribucion  Binomial
#Juan Francico Arreola Hernández.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
a = np.random.binomial(n = 5, p = 0.7, size = 20)
print(a)
sns.distplot(a, hist=True, kde=False)
plt.ylabel('Muestras')
plt.xlabel('Intervalos (1-5)')
plt.show()