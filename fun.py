import itertools
import matplotlib.pyplot as plt 
  
# Takes the square of a complex number x + yi.  
def complexy(x,y):
  a=x
  b=y
  x=a**2 - b**2
  y=2 * a * b
  return x,y

# Determines whether the point x + yi is in the Mandelbrot Set
def run2(x,y):
  count = 0
  c=x
  d=y
  try:
    while count < 1000:
      a=x
      b=y
      x = complexy(a,b)[0] + c
      y = complexy(a,b)[1] + d
      count += 1
  except:
    return False
  return True


# Calculates all of the points that are in the Mandelbrot Set, 
# seperates them into real and imaginary parts and returns both parts.
def calculate():
  a=[]
  b=[]
  for x,y in itertools.product(range(-400, 102), range(-240, 242)):
    if run2(x/200,y/200):
      a.append(x/200)
      b.append(y/200)
  return a,b
      
# Graphs the Mandelbrot Set  
plt.style.use('bmh')
a, b = calculate()
plt.scatter(a, b, color='red', marker='o', s=0.1)
plt.ylim(-1.2, 1.2)
plt.xlim(-2.0, 0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Mandelbrot Set')
plt.show()
