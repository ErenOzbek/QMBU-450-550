import linear
import unittest

class linear_Test(unittest.TestCase):

    def sigma_test(self):
    	if type(sigmasq) is float:
    		pass
    	else:
    		raise TypeError("SigmaSq should be a scalar value, check your code for any typos")


    def string_test(self):
        if type(x) == str or type(y) == str:
            raise TypeError("You can not enter a string for linear regression")
    
    def data_match(self):
        if x.shape[0] != x.shape[1]:
            raise ValueError('You should have equal amount of data for both variables') 

    
if __name__ == '__main__':
  unittest.main()

