# Towers of Hanoi
## Fast pseudorandom number generator

Samples are taken from an approximately normal distribution.

*Towers of Hanoi* is a [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling) algorithm for pseudorandom number generation--- inspired by the [Ziggurat algorithm](https://heliosphan.org/zigguratalgorithm/zigguratalgorithm.html).


## Example
The included example illustrates the advantages of *rejection sampling* over naive sampling methods. Namely, *rejection sampling* is an accelerated method for sampling random numbers from a bounded domain (e.g. $x \in [4, 5]$). [This method can be more efficient than naive sampling by approximately an order of magnitude.]

In the example included in this repository, samples are drawn from a standard normal distribution.

To run the example, `$ python3 RandomizedOptimizationTests.py`.
