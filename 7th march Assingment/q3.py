# Q3. Measure the three measures of central tendency for the given height data:
import numpy as np
from scipy import stats
data=[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5] 
print("mean:",np.mean(data))
print("median:",np.median(data))
print("mode:",stats.mode(data))