# -*- coding: utf-8 -*-
"""Building Block of Neural Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NJpZddCVobUX_N3HyQ75dnV8qtsaEsmd

**Scaler (0D Tensors)**
"""

import numpy as np
x = np.array(12)
x

x.ndim

"""**Vectors (1D Tensors)**"""

x = np.array([12,3,6,14])
x

x.ndim



"""**Metrices(2D Tensors)**"""

x = np.array([[5,78,2,34,0],
              [6,79,3,35,1],
              [7,80,4,36,2]])
x

x.ndim

"""# **Tensors Operation**

*1.0 Element-wise operations*
"""

def naive_relu(x):
  assert len(x.shape) == 2

  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i,j] = max(x[i,j], 0)

  return x

"""*1.1 Addition*"""

def naive_add(x,y):
  assert len(x.shape) == 2
  assert x.shape == y.shape
  
  x= x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i, j] += y[i,j]

  return x

"""*2.0 Broadcasting*"""

def naive_add_matrix_and_vector(x,y):
  assert len(x.shape) == 2
  assert len(y.shape) == 1
  assert x.shape[1] == y.shape[0]

  x = x.copy()
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      x[i,j] += y[i]
  return x

"""*3.0 Tensor Dot*"""

def naive_vector_dot(x,y):
  assert len(x.shape) == 1
  assert len(y.shape) == 1
  assert x.shape[0] == y.shape[0]

  z=0
  for i in range(x.shape[0]):
    z += x[i] * y[i]
    return z

"""*Between a matrix and a vector*"""

def naive_matrix_vector_dot(x, y):
  assert len(x.shape) == 2
  assert len(y.shape) == 1
  assert x.shape[1] == y.shape[0]

  z= np.zeroes(x.shape[0])
  for i in range(x.shape[0]):
    for j in range(x.shape[1]):
      z[i] +=  x[i,j] *  y[j]

  return z