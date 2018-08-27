# Instead of moving a distribution, move (and modify) it using a convolution.
# 06_b_convolve_distribution
# Claus Brenner, 26 NOV 2012
from pylab import plot, show, ylim
from distribution import *

def move(distribution, delta):
    """Returns a Distribution that has been moved (x-axis) by the amount of
       delta."""
    return Distribution(distribution.offset + delta, distribution.values)

def convolve(a, b):
#    print(a.values)
#    print(b.values)
    distributions = []
    new_offset = a.offset + b.offset -1
    for a_val in a.values:
        val = []
        for b_val in b.values:
            val.append(a_val*b_val)
        new_offset = new_offset + 1
        distributions.append(Distribution(new_offset,val))
    c = Distribution.sum(distributions)


    """Convolve distribution a and b and return the resulting new distribution."""

    # --->>> Put your code here.
    
    return c  # Replace this by your own result.


if __name__ == '__main__':
    arena = (0,100)

    # Move 3 times by 20.
    moves = [20] * 50

    # Start with a known position: probability 1.0 at position 10.
    position = Distribution.unit_pulse(10)
    plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
         linestyle='steps')

    # Now move and plot.
    for m in moves:
        move_distribution = Distribution.triangle(m, 2)
        position = convolve(position, move_distribution)
        plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
             linestyle='steps')

    ylim(0.0, 1.1)
    show()
