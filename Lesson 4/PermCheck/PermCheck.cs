using System;
using System.Linq;
using System.Collections.Generic;
class Solution {
   
    //Note sum= A[i]-(i + 1) 會遇到總和 一樣 但是並非排列
    public int solution(int[] A)
    {
        // write your code in C# 6.0 with .NET 4.5 (Mono)
        int sum = 0;
        for (int i = 0; i < A.Length; i++)
        {
            sum ^= A[i];
            sum ^= (i + 1);
        }
        return sum == 0 ? 1 : 0;
    }
   
    public int solution(int[] A)
    {
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
   
    //先排序 一一比較
	//O(N) or O(N * log(N))		
	
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
	 
	 //Using Linq O(N) or O(N * log(N))
	 public int solution(int[] A)
	 {
        return A.OrderBy(x => x).Where((x, i) => x == (i + 1)).Count() == A.Count() ? 1 : 0;
     }
	 
	
}