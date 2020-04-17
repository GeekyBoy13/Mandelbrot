import time
import itertools
import matplotlib.pyplot as plt 

#Function to determine whether an integer is even or odd.
def evorod(start):
	if start % 2 == 0:
		return True
	return False
	
# run runforfun() with a starting number, 
# and it will apply the Collatz Conjecture to see how many iterations it takes before it goes to 1.
def runforfun(start):
	copy = start
	count = 0
	print('Starting...')
	time.sleep(2)
	while start != 1:
		if evorod(start):
			start /= 2
			count += 1
			print(int(start))
			time.sleep(0.3)
		elif not evorod(start):
			start = 3 * start + 1
			count += 1
			print(int(start))
			time.sleep(0.3)
	print(f'The number {copy} went through {count} iterations.')
    
# The same thing as runforfun, but without the printing all the iterations;
# just returns the number and how many iterations it took.	
def run(start):
	copy = start
	count = 0
	while start != 1:
		if evorod(start):
			start /= 2
			count += 1
		elif not evorod(start):
			start = 3 * start + 1
			count += 1
	return copy, count
  
# Takes the square of a complex number x + yi.  
def complex(x,y):
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
  while count < 9:
    a=x
    b=y
    x = complex(a,b)[0] + c
    y = complex(a,b)[1] + d
    count += 1
  if (x)**2 + (y)**2 <= 5:
    return True
  return False

# Calculates all of the points that are in the Mandelbrot Set, 
# seperates them into real and imaginary parts and returns both parts.
def calculate():
  a=[]
  b=[]
  for x,y in itertools.product(range(-200, 51), range(-120, 121)):
    if run2(x/100,y/100):
      a.append(x/100)
      b.append(y/100)
  return a,b
      
# Graphs the Mandelbrot Set  
plt.style.use('bmh')
a, b = calculate()
plt.scatter(a, b, color='red', marker='o', s=0.1)
plt.ylim(-1.2, 1.2)
plt.xlim(-2, 0.5)
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Mandelbrot Set')
plt.show()

# Graphs the Collatz Conjecture
x=[i for i in range(1,100001)]
y=[run(i)[1] for i in range(1,100001)]
plt.style.use('bmh')
plt.scatter(x,y, color='red', marker='o', s=0.7)
plt.xlim(0,100000)
plt.ylim(0, 300)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Collatz Conjecture')
plt.show()
