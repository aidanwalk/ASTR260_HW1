import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    inputfile = 'collatz_output.txt'
    data = np.genfromtxt(open('collatz_output.txt'), dtype=np.int, 
                         skip_header=1)
    print(data)

    maxNumberChecked = len(data)+2
    numberChecked = np.arange(2, maxNumberChecked)
    
    plt.scatter(numberChecked, data, marker = ".", c='black', s=5)
    plt.title("Collatz n(1,10000)")
    plt.xlabel("n")
    plt.ylabel("L(n)")

    plt.show()


