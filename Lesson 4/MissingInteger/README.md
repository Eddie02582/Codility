# MissingInteger

<a href="https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/">原文</a>

This is a demo task.</br>

Write a function:</br>

class Solution { public int solution(int[] A); }</br>

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.</br>

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.</br>

Given A = [1, 2, 3], the function should return 4.</br>

Given A = [−1, −3], the function should return 1.</br>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>N is an integer within the range [1..100,000];</li>
    <li>each element of array A is an integer within the range [−1,000,000..1,000,000]</li>
</ul>




分析:建立一個bool 陣列長度為A陣列的長度,第一次迴圈判斷哪些數值存在,第二次迴圈取得不存在數字,如果都存在返回下一個數字

python
```python
def solution(A):
    # write your code in Python 3.6    
    appear=[False]*len(A)
    for x in A:
        if x<=len(A) and x>0:
            appear[x-1]=True 
    for i,bapper in enumerate(appear,1):
        if not bapper:
            return i;    
    return len(A)+1  
```





















