# MaxCounters

<a href="https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/">原文</a>

You are given N counters, initially set to 0, and you have two possible operations on them:</br>

<ul>
    <li>increase(X) − counter X is increased by 1,</li>
    <li>increase(X) − counter X is increased by 1,</li>
</ul>

A non-empty array A of M integers is given. This array represents consecutive operations:</br>

<ul>
    <li>if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),</li>
    <li>if A[K] = N + 1 then operation K is max counter.</li>
</ul>


For example, given integer N = 5 and array A such that:</br>

```
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
```
the values of the counters after each consecutive operation will be:</br>

```
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
```    
    
The goal is to calculate the value of every counter after all operations.</br>

Write a function:</br>

class Solution { public int[] solution(int N, int[] A); }</br>

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.</br>

Result array should be returned as an array of integers.</br>

For example, given:</br>
```
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
```
the function should return [3, 2, 2, 4, 2], as explained above.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N and M are integers within the range [1..100,000];</li>
    <li>each element of array A is an integer within the range [1..N + 1].</li>
</ul>



分析:利用迴圈,當值小於N時+1,1並取得目前最大值,當值N+1時全部更新為最大值,注意此方法只有score 88,當陣列過大時會timeout


```python
def solution2(N, A):
    # write your code in Python 3.6    
    B=[0]*N
    max=0
    for x in A:   
        if x <=N:            
            B[x-1]+=1
            max= B[x-1] if B[x-1]> max else max
        else if x==N+1:
            B=[max]*N
    return B
```
分析:修改上方最後在更新(N=N+1部分),若迴圈中更新需先更新到(N=N+1)在執行加1

```python
def solution(N, A):
    # write your code in Python 3.6    
    B=[0]*N
    max=0
    add=0
    for x in A:   
        if x <=N:
            if B[x-1] <add:
               B[x-1]= add+1              
            else:
                B[x-1]+=1  
            max= B[x-1] if B[x-1]> max else max
        else:            
            add=max
     
    for i in range(len(B)):
        if B[i]<add:
            B[i]=add 
    return B
```



