# Statistical power

You were perhaps surprised by the ideas that were presented in the video and quiz that appeared prior to this one.  Instinctively we believe that the more data we collect the more evidence we have.  The answer to the previous exercise suggests that this is not the case, however.  To understand what is going on you need to think about the process that we go through when we perform a hypothesis test once more:

![](hypo-testing.001.jpeg)

The key point to recognise is that the distribution for the __test statistic__ when we have one data point is different from the distribution we have when we have ten data points.  The __critical region__ for a 5% significance level is thus "wider" in this second case.  In other words, the __significance level__ is the measure that we use to quantify the conditional probability for a type I error.  In the previous example, __the significance levels__ for the two tests are identical.  The evidence that a type I error has not occurred is thus the same in both cases.  The fact that we have more data points is irrelevant.

Why then should we repeat our experiments to get more data?  Why does this give us more certainty in our result?  

To answer these questions we need to consider the probability that a type II error occurs.  Remember a type II error occurs when the __null hypothesis__ is __not__ rejected even though the __alternative hypothesis__ is true.  The conditional probability for a type II error is one minus a quantity that is known as the __statistical power__.  This __statistical power__ is then defined as:

_statistical power = conditional probability of accepting the __alternative hypothesis__ given that the __alternative hypothesis__ is true._

To measure the statistical power we thus have to find the probability that a sample from a distribution with an expectation that is outside the __critical region__ falls inside the __critical region.__  

To understand this better let's consider how we might determine this quantity for the test that we performed in the first task.  In that task, we evaluated the sample mean of our data points  ![](https://render.githubusercontent.com/render/math?math=\mu_D).  We then demonstrated that ![](https://render.githubusercontent.com/render/math?math=\mu_D) is lower the upper bound for the __critical region__ and thus argued that the __null hypothesis__ should be rejected.

Lets now assume that the value of ![](https://render.githubusercontent.com/render/math?math=\mu_D) that we obtained is the true expectation of the normal distribution that was sampled.  In addition, let's assume that the standard deviation for the sampled distribution is two as was assumed under the null hypothesis in the first task.  If you remember from that task the null and alternative hypotheses in the first task were that the sampled distribution had expectation twenty and variance four and that the expectation was less than 20 respectively.  From this information, you could thus calculate the upper bound for the __critical region__, which we will call l.  Given the definition above the __statistical power__ is thus:

![](https://render.githubusercontent.com/render/math?math=B(\mu)=P(T\le\l|\mu_D=\mu)=P\left[\frac{1}{n}\sum_{i=1}^{n}X_i\le\mu_0+\frac{\sigma}{\sqrt{n}}\Phi^{-1}(0.05)\right])

In the final equality here we replace the test statistic with the sample mean calculated from n random variables.  The lower bound is then replaced by a formula that can be used to calculate this quantity.  In this expression, ![](https://render.githubusercontent.com/render/math?math=\mu_0) is the expectation that is assumed under the null hypothesis (in this case ![](https://render.githubusercontent.com/render/math?math=\mu_0=20)), ![](https://render.githubusercontent.com/render/math?math=\Phi^{-1}) is the inverse of the cumulative probability distribution function for the standard normal distribution.  

In the conditional probability on the left-hand side of the final equality of the expression above we have asserted that we are calculating this conditional probability given that the true expectation ![](https://render.githubusercontent.com/render/math?math=\mu_D) for the distribution is equal to the value of the sample mean that we used as the statistic when performing the hypothesis test.  The ![](https://render.githubusercontent.com/render/math?math=X_i) values that we are using in the calculation of T are a new set of samples this distribution.  We can thus continue the derivation above as follows:

![](https://render.githubusercontent.com/render/math?math=B(\mu)=P(T\le\l|\mu_D=\mu)=P\left[\frac{\frac{1}{n}\sum_{i=1}^{n}X_i-\mu}{\sigma/\sqrt{n}}\le\frac{\mu_0}{\sigma/\sqrt{n}}+\Phi^{-1}(0.05)-\frac{mu}{\sigma/\sqrt{n}}\right])

The central limit theorem tells us that the quantity on the right-hand side of the inequality in the probability above is a sample from a standard normal random variable.  We can thus write the following as our final expression for the statistical power of the test:

![](https://render.githubusercontent.com/render/math?math=B(\mu)=P(T\le\l|\mu_D=\mu)=\Phi\left[\frac{\mu_0}{\sigma/\sqrt{n}}+\Phi^{-1}(0.05)-\frac{\mu}{\sigma/\sqrt{n}}\right])

where ![](https://render.githubusercontent.com/render/math?math=\Phi) is the cumulative probability distribution function for the standard normal random variable.

__To complete this task you need to complete the function called `statisticalPower` in the cell on the left.__  This function takes four arguments:

1. `mu0` - the value of expectation that is assumed under the null hypothesis.
2. `sigma` - the standard deviation of the distribution
3. `mu` - the value for the sample mean that was obtained for the data.
4. `N` - the number of data points from which mu was calculated.

The function should use these four numbers and the theory described above to calculate the statistical power.  This quantity should then be returned.  If the task is completed correctly a graph showing the statistical power against the number of experiments performed will be shown for the test that was described in the first exercise.

   
