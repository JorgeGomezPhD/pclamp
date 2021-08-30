# imports libraries to be used
import matplotlib.pyplot as plt
from set_file_name import abf

# Imports file you want to visualize
abf = abf

# defines function to use in other file
def multiple_trace():
    trace1 = int(input("Enter trace 1: "))
    trace2 = int(input("Enter trace 2: "))

    for i in [trace1, trace2]:
        abf.setSweep(i)
        plt.plot(abf.sweepX, abf.sweepY, alpha=.5, label="sweep %d" % (i))
        plt.xlim(0, 1)
    plt.savefig(f"210824/21824000_sweep{i}.pdf")
    plt.legend()
    plt.show()

multiple_trace