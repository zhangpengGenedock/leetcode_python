# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        orbin = '{0:032b}'.format(n)
        reversebin = orbin[::-1]
        return int(reversebin, 2)

    def reverseBits2(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits3(self,n ):
        rvalue = 0
        for i in range(0, 32):
            rvalue <<= 1
            rvalue += n & 1
            n >>= 1

        return rvalue

