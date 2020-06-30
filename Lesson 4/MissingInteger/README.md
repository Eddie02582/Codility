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




分析:建立一個set用來儲存數字,迴圈從1~len(A)+1 判斷是否數字在set裡面,沒有就回傳

python
```python
def solution(A):
    # write your code in Python 3.6
    #O(N) or O(N * log(N))
    numbers = set()
    for n in A:
        numbers.add(n)
        
    for i in range(1,len(A) + 1):
        if i not in numbers:
            return i
    
    return len(A) + 1    
     
```





















