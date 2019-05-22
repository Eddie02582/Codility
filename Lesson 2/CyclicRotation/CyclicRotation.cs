using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {	
	
    public int [] solution(int[] A, int K)
	{    
		return A.Select((x, i) => A[(A.Length - K % A.Length + i) % A.Length]).ToArray();
    }	
	

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