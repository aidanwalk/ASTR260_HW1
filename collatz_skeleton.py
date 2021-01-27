import numpy as np

def number_of_steps_to_one(number):
    """Function which determines how many steps
    it takes for a number to reach 1 in the Collatz
    sequence
    input: number (a positive integer)
    output: steps 
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    if not number>1:
        raise ValueError("number must be larger than one")
    #Fill this in with an algorithm that calculates
    #the number of steps needed to reach one
    steps = 0
    while number > 1 :
        if number%2 == 0 : #number is even
            number = number/2
        else :
            number = 3*number + 1
        steps += 1
    
    return steps

if __name__ == "__main__":
    max_number_to_check = 10**5
    numbers_to_check = np.arange(2, max_number_to_check+1)
    #Fill this section in 
    #write a for loop that iterates from 1 -> max_number to check
    #and calculates the number of steps to get to 1
    #data = np.zeros((max_number_to_check - 1), int) #max_number_to_check-1 bc we start calculating at 2
    data = []
    for x in numbers_to_check:
        x = x.item() #convert from np.int32 into int
        numberOfSteps = number_of_steps_to_one(x)
        ##data[x-2,0] = x #x-2 bc we start checking at 2, this assigns 2 to test[0,0]
        #data[x-2] = numberOfSteps
        data.append((x, number_of_steps_to_one(x)))
    np.savetxt('collatz_output.txt', data, fmt='%i', delimiter=',', header='L(n)')