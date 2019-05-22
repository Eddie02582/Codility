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