#task1 
import numpy as np

v = np.arange(10, 50)
print(v)

#task 2
m = np.arange(9).reshape(3, 3)
print(m)

#tak3 
I = np.eye(3)
print(I)

#task4 
a = np.random.rand(3, 3, 3)
print(a)

#task5
A = np.random.rand(10, 10)
print("Min:", A.min())
print("Max:", A.max())
 
#task6 
v = np.random.rand(30)
print("Mean:", v.mean())


#task 7 
M = np.random.rand(5, 5)
norm = (M - M.mean()) / M.std()
print(norm)

#task 8  
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
C = A @ B
print(C)


#task 9 
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
print(A.dot(B))
 
#task 10 
M = np.random.rand(4, 4)
print(M.T)
 
#task 11 
M = np.random.rand(3, 3)
print(np.linalg.det(M))
 
#task 12 
A = np.random.rand (3, 4)
B = np.random.rand(4, 3)
C = A @ B 
print (C)

#task 13 
M = np.random.rand(3, 3)
v = np.random.rand(3, 1)
print(M @ v)
 
#task 14 
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)

x = np.linalg.solve(A, b)
print(x)
 
#task 15 
M = np.random.rand(5, 5)

print("Row sums:", M.sum(axis=1))
print("Column sums:", M.sum(axis=0))
