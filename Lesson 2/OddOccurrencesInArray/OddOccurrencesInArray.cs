using System;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
	
	//Detected time complexity:O(N) or O(N*log(N))
    public int solution(int[] A) 
	{    
		return A.Select(x => x).GroupBy(y => y).Where(z=>z.Count()%2 !=0).Sum(x=>x.Key);
    }
	public int solution_1(int[] A) 
	{    
		return A.Aggregate(0, (a, b) => a ^ b);
    }
	
	//O(N) or O(N*log(N))
	public int solution(int[] A) {        
        int sum = 0;        
        foreach (int num in A)
            sum ^= num;            
        return sum;

    }
}