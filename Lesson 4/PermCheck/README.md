# PermCheck


<a href="https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/">原文</a>

A non-empty array A consisting of N integers is given.</br>

A permutation is a sequence containing each element from 1 to N once, and only once.</br>

For example, array A such that:</br>
```
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
```
is a permutation, but array A such that:</br>
```
    A[0] = 4
    A[1] = 1
    A[2] = 3
```    
    
is not a permutation, because value 2 is missing.</br>

The goal is to check whether array A is a permutation.</br>

Write a function:</br>

class Solution { public int solution(int[] A); }</br>

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.</br>

For example, given array A such that:</br>
```
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
```
the function should return 1.</br>

Given array A such that:</br>
```
    A[0] = 4
    A[1] = 1
    A[2] = 3
```
the function should return 0.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an integer within the range [1..100,000];</li>
    <li>each element of array A is an integer within the range [1..1,000,000,000].</li>
</ul>



分析:排序並且一一比較,注意使用XOR或SUM會有問題 Ex A=[4,4,1,1] SUM(A)=SUM([4,1,2,3]),題目沒說給陣列裡的數字只會出現一次

C#
```csharp
using System;
class Solution {
  public int solution(int[] A)
	{
        Array.Sort(A);
        for (int i = 0; i < A.Length; i++)
        {
            if ((i + 1) != A[i])
                return 0;
        }
        return 1;
    }
	
}
```

python
```python
def solution(A):
    # write your code in Python 3.6
    numbers = set(A)    
    for i in range(1,len(A) + 1):
        if i not in numbers:
            return 0
    
    return 1    
```





















