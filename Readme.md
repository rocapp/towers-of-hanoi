# Towers of Hanoi

A [rejection sampling](https://en.wikipedia.org/wiki/Rejection_sampling) implementation inspired by the [Ziggurat algorithm](https://heliosphan.org/zigguratalgorithm/zigguratalgorithm.html).

The included example illustrates the advantages of rejection sampling over naive sampling methods. Namely, rejection sampling can accelerate sampling from a specified bounded domain (e.g. $x \in [4, 5]$) by approximately an order of magnitude. In this example, samples are drawn from a normal distribution.