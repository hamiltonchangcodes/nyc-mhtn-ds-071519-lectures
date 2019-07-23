#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math #importing math module to do square roots
class Calc:
    def __init__(self, data):
        self.data = data
        self.update_stats()
#         self.length = len(data)  HERE WE ARE REFACTORING. WE BUILD THIS ORIGINALLY TO DO THE MATH
#         self.mean = self.__calc_mean()  BUT WE HAVE NOW INSTEAD TOLD THE PROGRAM TO GO LOOK AT THE MATH
#         self.median = self.__calc_med()  WE WOULD HAVE DONE ANYWAYS WHEN WE RUN THE UPDATE_STATS FUNCTION
#         self.variance = self.__calc_var()
#         self.standev = self.__calc_standev()
    
    def __calc_mean(self): #THE __ IN FRONT ALLOWS US TO HIDE THE FUNCTION AND REFER TO MEAN ITSELF INSTEAD OF CALC_MEAN
        return round(sum(self.data) / len(self.data), 2)
    
    def __calc_med(self):
        mid = len(self.data)/2
        if len(self.data)%2 == 0:  #THE %2 DIVIDES SOMETHING BY TWO TO FIND A REMINDER, IF WE SET IT ==0 TO TEST IF IT IS EVEN OR ODD
            return (self.data[int(mid + .5)] + self.data[int(mid - .5)])/2
        else: return self.data[int(mid - .5)]
        
    def __calc_var(self):
        sum = 0
        for i in self.data:
            sum += (i - self.mean)**2
        return round(sum / (len(self.data)-1), 2)
    
    def __calc_standev(self):
        return round(math.sqrt(self.variance), 2)
    
    def add_data(self, data):
        # add new data and sort it
        self.data.extend(data)
        self.data.sort()
        # re-run all stats calcs on new data
        self.update_stats()
# THIS WAS BUILT TO REMOVE A SPECIFIC ITEM, AND NOT BASED ON ITS POSITION IN THE LIST    
    def remove_data(self, item):
        self.data.remove(item)
        self.update_stats()
    
    def update_stats(self):
        # assumes data has been set or re-set
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_med()
        self.variance = self.__calc_var()
        self.standev = self.__calc_standev()


# In[ ]:




