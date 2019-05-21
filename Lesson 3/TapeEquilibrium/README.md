# TapeEquilibrium

<a href="https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/">原文</a>

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.</br>

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].</br>

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|</br>

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.</br>

For example, consider array A such that:</br>
```
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
```
We can split this tape in four places:</br>
<ul>
    <li>P = 1, difference = |3 − 10| = 7 </li>
    <li>P = 2, difference = |4 − 9| = 5 </li>
    <li>P = 3, difference = |6 − 7| = 1 </li>
    <li>P = 4, difference = |10 − 3| = 7 </li>
</ul>
Write a function:</br>

class Solution { public int solution(int[] A); }</br>

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.</br>

For example, given:</br>
```
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
```
the function should return 1, as explained above.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an integer within the range [2..100,000];</li>
    <li>each element of array A is an integer within the range [−1,000..1,000].</li>
</ul>



分析:利用雙指針，右邊值為總合，左邊為零，最小值一開始為right - 2*A[0]絕對值


```csharp
using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {	
	
	public int solution(int[] A)
    {      
        int right = A.Sum();
        int left = 0;
        int min = Math.Abs(right - 2*A[0]);//min i=0 right-left
        for (int i = 0; i < A.Length - 1; i++)
        {
            left += A[i];
            right = right - A[i];           
            int temp = Math.Abs(right - left);
            min = temp < min ? temp : min;
        }
        return min;
    }
}
```


分析:利用XOR，A總和XOR (1+...+(N+1))總和，下面分別sum(A)^(1+...+(N))，最後在XOR N+1</br>

```csharp
using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {	
	
    public int solution(int[] A) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int sum=0;
        for (int i = 0; i < A.Length; i++)
        {
            sum ^= A[i];
            sum ^= i+1;
        }
        return sum ^= A.Length+1;
    }	
}
```

