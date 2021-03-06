# OddOccurrencesInArray

<a href="https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/">原文</a>


A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.</br>

For example, in array A such that:</br>
```
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
```
  
the elements at indexes 0 and 2 have value 9,</br>
the elements at indexes 1 and 3 have value 3,</br>
the elements at indexes 4 and 6 have value 9,</br>
the element at index 5 has value 7 and is unpaired.</br>
Write a function:</br>

```
class Solution { public int solution(int[] A); }
```

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.</br>

For example, given array A such that:</br>
```
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
```  

the function should return 7, as explained in the example above.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an odd integer within the range [1..1,000,000];</li></br>
    <li>each element of array A is an integer within the range [1..1,000,000,000];</li></br>
    <li>all but one of the values in A occur an even number of times.</li></br>
</ul>



分析:ex:5 ^5 =0 ,利用xor取得非成對的數字

```python
def solutionByXOR(A):
    result = 0
    for number in A:
        result ^= number
    return result
```