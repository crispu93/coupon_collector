# The coupon collector problem
import sys
import random
import csv
import numpy as np
import matplotlib.pyplot as plt

def collect(n):
    ''' Select a random number
    between 1 and n (inclusive)'''
    return random.randint(0,n)


def coupon_collector(n, collected):
    ''' Returns the number of boxes needed
    to collect all coupons
    '''
    steps = 0
    while len(collected) != n:
        aux = collect(n)
        if aux not in collected: 
            collected.add(aux)
        steps += 1

    return steps

if __name__ == "__main__":
    #n = int(sys.argv[1])
    ''' For saving data
    with open('steps.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([20,50,100,500,1000,5000,10000,20000,50000])
        for i in range(100):
            row = []
            for n in [20,50,100,500,1000,5000,10000,20000,50000]:
                ### Set of coupons already collected
                collected = set()
                row.append(coupon_collector(n,collected))
                print(n,i)
                ##print(n, "coupons solved in", coupon_collector(n,collected), "steps" )            
            writer.writerow(row)
    '''
    times =20
    labels = np.array([100,200,300,500,800,1300,2100,3400,5500,8900,14400,23300,37700,61000])
    #labels = np.array([100,200,300,500,800,1300,2100,3400,5500,8900,14400,23300])
    #labels = np.array([20,50,100,500,1000])
    cols = []
    for n in labels:
        col = []
        for i in range(20):
            ### Set of coupons already collected
            collected = set()
            col.append(coupon_collector(n,collected))
            print(n,i)
        cols.append(col)
    data = np.array(cols)
    means = np.mean(data, axis = 1)
    stds = np.std(data, axis = 1)

    print(means)
    print(stds)
    fig = plt.figure()
    plt.errorbar(labels,means, yerr=stds, label='std')
    plt.title('Simulated 20 times')
    plt.xlabel('Number of coupons')
    plt.ylabel('Boxes')
    plt.grid(True)
    
    plt.show()