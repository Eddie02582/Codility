# BinaryGap

<a href="https://app.codility.com/programmers/lessons/1-iterations/binary_gap/">原文</a>


A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N. </br>

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.</br>

Write a function:</br>

class Solution { public int solution(int N); }</br>

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.</br>

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.</br>


分析:將整數N 轉成bin ，再利用雙指針紀錄計算前後'1' 的距離，並且比較


```csharp
using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int N) {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        string strBin=Convert.ToString(N,2);
        int max=0;
        int left=0;
        int right=0;
        for (int i=0;i<strBin.Length;i++)
        {
            char c=strBin[i];
            if (c=='1')
            {
                left=right;
                right=i;
                max = max>(right-left-1) ? max:right-left-1;
            } 
        }
        return max;
    }
}

```python
def solution(N):
    strbin=bin(N)[2:]
    left,max,right=0,0,0
    for index,s in enumerate(strbin):
        if s=='1':
            left=right
            right=index	
            max = right-left-1 if max <right-left-1 else max 	
    return  max
```