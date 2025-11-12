import numpy as np

A = np.array([[1, 2],
              [3, 4]])

A_inv = np.linalg.inv(A)
print(A_inv)

print("identity  matrix")
print(A.dot(A_inv))  # Should give identity matrix
