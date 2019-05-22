# PassingCars


<a href="https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/">原文</a>

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.</br>

Array A contains only 0s and/or 1s:</br>

<ul>
    <li>0 represents a car traveling east,</li>
    <li>1 represents a car traveling west.</li>
</ul>

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.</br>

For example, consider array A such that:</br>

```
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
```

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).</br>

Write a function:</br>
```
    class Solution { public int solution(int[] A); }
```

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.</br>

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.</br>

For example, given:</br>

```
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
```
the function should return 5, as explained above.</br>


Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an integer within the range [1..100,000];
    <li>each element of array A is an integer that can have one of the following values: 0, 1.</li>
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

分析:先利用set判斷是否有無重複數字，再利用XOR 判斷 

C#
```csharp
using System;
using System.Collections.Generic;
class Solution {
    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
          HashSet<int> SetNumbers = new HashSet<int>(A);
        if (SetNumbers.Count!=A.Length)
            return 0;
        
        int sum = 0;
        for (int i = 0; i < A.Length; i++)
        {
            sum ^= A[i];
            sum ^= (i + 1);
        }
        return sum == 0 ? 1 : 0;
    }
}
```
python
```python
def solution(A):
    # write your code in Python 3.6
    SetNumbers=set(A)
    if len(set(A))!=len(A):
        return 0
    sum=0
    for i,value in enumerate(A,1):
        sum^=value
        sum^=i
    
    return 1 if sum == 0 else 0;   
```





















