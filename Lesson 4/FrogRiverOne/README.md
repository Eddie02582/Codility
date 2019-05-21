# FrogJmp


<a href="https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/">原文</a>

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.</br>

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.</br>

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.</br>

For example, you are given integer X = 5 and array A such that:</br>
```
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
```
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.</br>

Write a function:</br>

class Solution { public int solution(int X, int[] A); }</br>

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.</br>

If the frog is never able to jump to the other side of the river, the function should return −1.</br>

For example, given X = 5 and array A such that:</br>
```
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
```
the function should return 6, as explained above.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N and X are integers within the range [1..100,000];
    <li>each element of array A is an integer within the range [1..X].
</ul>



分析:給定一bool 陣列長度為X,使用Count 計數，當陣列值皆為true(count等於X) 即表示1,..,X皆出現

C#
```csharp
using System;
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
	
}
```

python 


```python
def solution(X, A):
    tiles=[Fasle]*X
    count=0  
    for i,value in enumerate(A)	
        index=value-i
        if index<X and !tiles[index]:
            count+=1
            tiles[index]=True
        if todo==X:		
            return i
	return -1
    
```

分析:題目有說A的值[1..X]不然這方法會有問題，建立一個set 陣列 當set 陣列長度==X 即表示1..X皆出現


python 
```python
def solution(X, A):
	S = set()
	count = len(A)
	for i in range(0, count):
		S.add(A[i])
		if(len(S) == X):
			return i
	return -1
```    

若題目沒說加上判斷是 A[i]<=X 即可以
C#
```csharp
using System;
using System.Collections.Generic;
class Solution {
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
	
}
```












