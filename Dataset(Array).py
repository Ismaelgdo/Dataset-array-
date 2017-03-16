#Ismael Garrido Dataset.py
#Creating a Class to compute simple operations on a dataset.

import math
class Dataset(object):
    '''Dataset is a collection of numbers from which simple
    descriptive statistics can be computed.'''

    def __init__(self):
        '''post: self is an empty Dataset'''
        self.nums = []
       

    def add(self, x):
        '''add x to the data set
        post: x is added to the data set'''
        return self.nums.append(x)

    def size(self):
        '''compute the lenght of the list
        pre: size of self >=0
        post: returns the lenght of the list'''
        return len(self.nums)

    def min(self):
        '''find the minimum
        pre: size of self >= 1
        post: returns smallest number in self'''
        if self.size() < 1:
            raise ValueError
        return min(self.nums)

    def max(self):
        '''find the maximum
        pre: size of self >= 1
        post: returns largest number in self'''
        if self.size() < 1:
            raise ValueError
        return max(self.nums)

    def average(self):
        '''calculate the mean
        pre: size of self >= 1
        post: returns the mean of the values in self'''
        if self.size() < 1:
            raise ValueError
        return sum(self.nums) / len(self.nums)

    def std_deviation(self):
        '''calculate the standard deviation
        pre: size of self >= 2
        post: returns the standard deviation of the values in self'''
        
        length = len(self.nums)
        if length < 2:
            raise ValueError("Minimun two values needed to compute standard deviation")

        m = sum(self.nums)*1.0 / len(self.nums)
        tot_sum = 0

        for i in range(length):
            tot_sum += (self.nums[i]-m)**2

        root = tot_sum*1.0/(length - 1)
        std_dev = math.sqrt(root)
        return round(std_dev, 4)

if __name__ == '__main__':
 
    while True:
        data = Dataset()
        print('This is program computes the min, max, mean and')
        print('standard deviation for a set of numbers.\n')
        while True:
            xStr = input('Enter a number (<Enter> to quit): ')
            if xStr == '':
                break
            try:
                x = float(xStr)
            except ValueError:
                print('Invalid Entry Ignored: Input was not a number')
                continue
            data.add(x)
        print('Summary of', data.size(), 'scores.')
        print('Min:', data.min())
        print('Max:', data.max())
        print('Mean:', data.average())
        print('Standard Deviation:', data.std_deviation())
        print()
        print()



                    

