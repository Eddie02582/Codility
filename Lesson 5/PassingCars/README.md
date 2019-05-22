# PassingCars


<a href="https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/">原文</a>

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.</br>

Array A contains only 0s and/or 1s:</br>

<ul>
    <li>0 represents a car traveling east,</li>
    <li>1 represents a car traveling west.</li>
</ul>

The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.</br>

For example, consider array A such that:</br>

```
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
```

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).</br>

Write a function:</br>
```
    class Solution { public int solution(int[] A); }
```

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.</br>

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.</br>

For example, given:</br>

```
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
```
the function should return 5, as explained above.</br>


Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an integer within the range [1..100,000];
    <li>each element of array A is an integer that can have one of the following values: 0, 1.</li>
</ul>


**Solution** O(m<sup>2</sup>):
分析:利用雙重迴圈判斷

```python

#50%    Correctness=100% ,Performance=0%
def solution1(A): 
    count=0    
    for i in range(len(A)):        
        if A[i]==0:
            for j in range(i,len(A)):
                if A[j]==1:
                   count+=1  
    return count  
```

**Solution** O(m<sup>2</sup>):
分析:利用while

```python
#50%    Correctness=100% ,Performance=0%
def solution(A): 
    left,count=0,0
    len_A=len(A)
    right=len_A    
    while left< len_A-1:
        right-=1    
        if A[left]==0:        
            if A[left]!=A[right] :
                count+=1                  
        if A[left]==1 or left >= right-1:
            right=len_A
            left+=1    
    return count
```

**Solution** O(n):
分析:從範例來切入解題，可以看出0號向東行的車可以跟所有大於0號向西行的車作配對，2號向東行的車可以跟所有大於2號向西行的車作配對，由此可看出大於2號向西行的車都會被配對到兩次，他們既可以跟0號車配對，也可以跟2號車配對。
    所以利用迴圈記錄目前指針到的位置以前的A[i]=0的次數,之後遇到A[i]=1,一次增加配對數 


```python
def solution2(A): 
    add_base,count=0,0
    
    for i in range(len(A)):
        if(A[i]==0):
            add_base+=1
        else:
            count+=add_base

    if(count > 1000000000):
        return -1;
    return count
```
















