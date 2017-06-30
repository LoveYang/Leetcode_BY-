# -*- coding: utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n= x^y
        count=0
        while n>>1:
            if n%2:
                count+=1
            n=n>>1
        return count
        
