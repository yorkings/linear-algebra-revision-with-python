import numpy as np

v = np.array([3, 4])
magnitude = np.linalg.norm(v)

#derived fom my understanding
magnitude1=np.sqrt(np.sum(v**2))
print(magnitude1)

