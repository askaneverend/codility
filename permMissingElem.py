# you can use print for debugging purposes, e.g.
# print "this is a debug message"

'''
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''



def solution(A):
    # write your code in Python 2.7
    tmp = [0] * (len(A) + 2)  #add 2 because we have to give space for N + 1, and the start number is from 1, so number 0 also take one place
    for i in A:
    	tmp[i] = 1
    print tmp
    for j in xrange(1, len(tmp)):
    	if tmp[j] == 0 :
    		return j
