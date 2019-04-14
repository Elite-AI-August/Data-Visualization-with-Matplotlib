import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

lena = mpimg.imread('google.png')
print("- Read google.png: \ndimension:")
print(lena.shape)
print

plt.imshow(lena)
plt.axis('off')
plt.show()