import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    inputfile = 'collatz_output.txt'
    #data = np.genfromtxt(open('collatz_output.txt'), dtype=np.int, skip_header=1)
    data = np.loadtxt('collatz_output.txt', delimiter=',', skiprows = 1)
    
    plt.scatter(data[:,0], data[:,1], marker='.', c='black', s=1)
    plt.title("Collatz Conjecture n(1, 10000)")
    plt.xlabel("n")
    plt.ylabel("L(n)")

    plt.show()


