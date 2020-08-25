# Towers of Hanoi

A [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling) implementation inspired by the [Ziggurat algorithm](https://heliosphan.org/zigguratalgorithm/zigguratalgorithm.html).

To run the example, `$ python3 RandomizedOptimizationTests.py`.

The included example illustrates the advantages of rejection sampling over naive sampling methods. Namely, rejection sampling is an accelerated method for sampling random numbers from a bounded domain (e.g. $x \in [4, 5]$). This method can be more efficient than naive sampling by approximately an order of magnitude. In this example, samples are drawn from a standard normal distribution.