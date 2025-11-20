#task 1 
import numpy as np

# Function converting F → C
def f_to_c(F):
    return (F - 32) * 5/9

temps_f = np.array([32, 68, 100, 212, 77])

# Vectorize the function so it works on arrays
vf_to_c = np.vectorize(f_to_c)

temps_c = vf_to_c(temps_f)
print("Celsius:", temps_c)

#task 2
# Custom power function
def power(x, p):
    return x ** p

nums = np.array([2, 3, 4, 5])
pows = np.array([1, 2, 3, 4])

vpower = np.vectorize(power)

result = vpower(nums, pows)
print(result)

#task 3 
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)

#task 4 
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b = np.array([12, -5, 15])

currents = np.linalg.solve(A, b)
print("Currents (I1, I2, I3):", currents)

#Image Manipulation Using NumPy + PIL
#import modules 
from PIL import Image
import numpy as np
 
# load 
img = Image.open("images/birds.jpg")
arr = np.array(img)

# bonus 

#flip image 
def flip_image(arr):
    flipped_h = arr[:, ::-1]      # left–right
    flipped_v = arr[::-1, :]      # up–down
    return flipped_h, flipped_v


#add noise 
def add_noise(arr, amount=30):
    noise = np.random.randint(-amount, amount, arr.shape)
    noisy = arr + noise
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)


#Apply a rectangular mask
def apply_mask(arr, size=100):
    masked = arr.copy()
    
    h, w = arr.shape[0], arr.shape[1]
    x1 = h//2 - size//2
    x2 = h//2 + size//2
    y1 = w//2 - size//2
    y2 = w//2 + size//2
    
    masked[x1:x2, y1:y2] = 0
    return masked

