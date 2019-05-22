using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {

    ////100
    //O(N) or O(N * log(N))1
    //Linq
    public int solution(int X, int Y, int D) {
        return (A.Length == 0 || A.Length == A.Max()) == true ? A.Length + 1 : Enumerable.Range(1, A.Length + 1).Except(A).First();
    }

    public int solution_1(int X, int Y, int D)
    {
        //100% or O(N) or O(N * log(N))
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
	
	//O(N) or O(N * log(N))
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