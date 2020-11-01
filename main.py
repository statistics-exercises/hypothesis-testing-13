import matplotlib.pyplot as plt 
import scipy.stats
import numpy as np

def statisticalPower( mu0, sigma, mu, N ) :
  # Your code to compute the statistical power goes here
  
  return

# You don't need to modify the code from here

# we are assuming through that the result obtained for the sample 
# mean is the same as the result that was obtained in the first 
# exercise.  What we will thus calculate is the statistical power
# if that result had been obtained with different sample sizes.
sample = 16.704 
# This is the part for generating the power versus the number
# of experiments for the hypothesis test in the first task 
xvals, yvals = np.zeros(10), np.zeros(10)
for i in range(10) : 
  xvals[i] = i+1 
  yvals[i] = statisticalPower( 20, 2, sample, i+1 )
  
plt.plot( xvals, yvals, "ko")
plt.savefig( "power.png" )
