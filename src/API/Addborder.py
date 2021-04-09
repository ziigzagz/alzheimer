import numpy as np
m = [[1,2],[1,2]]
m = np.array(m)
print(m)
pm = np.pad(array=m, pad_width=1, mode='constant', constant_values=12)
for i in pm:
    print(i)