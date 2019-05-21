# CyclicRotation
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.</br>

Write a function:</br>

```csharp
class Solution { public int[] solution(int[] A, int K); }
```

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.</br>

For example, given</br>

```
A = [3, 8, 9, 7, 6]
K = 3 
```

the function should return [9, 7, 6, 3, 8]. Three rotations were made:</br>

```
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
```
For another example, given </br>

```
    A = [0, 0, 0]
    K = 1
```    
    
the function should return [0, 0, 0] </br>

Given </br>

```
    A = [1, 2, 3, 4]
    K = 4 
```    

the function should return [1, 2, 3, 4] </br>

Assume that:
<ul>
    <li>N and K are integers within the range [0..100];
    <li>each element of array A is an integer within the range [−1,000..1,000].</li></br>  
</ul>



分析:向右移動的步數可以簡化成K除A取餘數，新的位置的值及為原本位置的值加上移動的部數。注意輸入Array 為null


```csharp
using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    
	public int[] solution(int[] A, int K) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int len=A.Length;
        if (len==0)
            return new int[] { };    
            
        int Count = K % len;
        int[] B = new int[len];
        for (int i = 0; i < len; i++)
        {
            B[(i + Count) % len] = A[i];
        }
        return B;

    }
}
```

分析:向右移動的步數可以簡化成K%len(A)，利用切片直接取得平移後的位置

```python
def solution(A, K): 
    if A:
        move=K%len(A)
        return  A[len(A)-move:]+A[:len(A)-move] 
    else:		
        return  []
```