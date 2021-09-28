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
    while count < 900:
      a=x
      b=y
      x = complexy(a,b)[0] + c
      y = complexy(a,b)[1] + d
      count += 1
  except:
    return False
  return True


# Calculates all of the points that are in the Mandelbrot Set, 
# and seperates them into real and imaginary parts and returns both parts.
def calculate():
  m = 200
  u = -1.2
  i = 1.2
  o = -2.4
  p = 0.5
  thingy = round((m**2 * ((i-u)*(p-o)))/100,0)
  a=[]
  b=[]
  counter=0
  for x,y in itertools.product(range(int(o*m), int(p*m)), range(int(u*m), int(i*m))):
    if run2(x/m,y/m):
      a.append(x/m)
      b.append(y/m)
    if round(counter/thingy, 0) != round((counter+1)/thingy, 0):
      print(round(counter/thingy, 0))
    counter += 1
  return a,b
      
# Graphs the Mandelbrot Set  
plt.style.use('bmh')
a, b = calculate()
plt.scatter(a, b, color='red', marker='o', s=0.1)
plt.ylim(-1.2, 1.2)
plt.xlim(-2.4, 0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Mandelbrot Set')
plt.show()
