using System;
using System.Collections.Generic;
using System.Linq;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
	
	public int solution(int X, int[] A) 
	{
        bool[] tiles = new bool[X];
        int count = 0;

        for (int i = 0; i < A.Length; i++)
        {
            int internalIndex = A[i] - 1;
            if (internalIndex < X && !tiles[internalIndex])
            {
                count++;
                tiles[internalIndex] = true;
            }

            if (count == X)
                return i;
         }

         return -1;
    }
	//O(N)
	public int solution(int X, int[] A)
	{
	  HashSet<int> hash = new HashSet<int>();

	  for(int i=0;i<A.Length;i++)
	  {
		  if(A[i]<=X)
		  {
			hash.Add(A[i]);
			if(hash.Count == X)
				return i;
		  }
	  }
	  return -1;
	}    
	
	public int solution(int X, int[] A) 
	{
        List<int> Leaf =new List<int>();            
        for (int i = 0; i < A.Length; i++)
        {                
             Leaf.Add(A[i]);
             Leaf=Leaf.Distinct().ToList();
             if (Leaf.Count() == X)
                 return i;
         }
         return -1;
    }
	
}

