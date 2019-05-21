# PermMissingElem

<a href="https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/">原文</a>

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.</br>

Your goal is to find that missing element.</br>

Write a function:</br>

class Solution { public int solution(int[] A); }</br>

that, given an array A, returns the value of the missing element.</br>

For example, given array A such that:</br>
```
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
```
the function should return 4, as it is the missing element.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an odd integer within the range [1..1,000,000];</li>
    <li>the elements of A are all distinct;</li>
    <li>each element of array A is an integer within the range [1..(N + 1)].</li>
    <li>the function should return 7, as explained in the example above.</li>
</ul>



分析:若A長度為4,假設A=[2,3,1,5]，(1+...+(N+1))總和-A總和 ，即為消失的數字</br> 

C#
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
        int sum = 0;
        int total = 0;
        for (int i = 0; i < A.Length; i++)
        {
            sum += A[i];
            total += i + 1;
        }
        int result = total + A.Length + 1 - sum;
        return result;
    }	
}
```


分析:利用XOR，A總和XOR (1+...+(N+1))總和，下面分別sum(A)^(1+...+(N))，最後在XOR N+1</br>
C#
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

