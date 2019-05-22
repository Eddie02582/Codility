# BinaryGap

<a href="https://app.codility.com/programmers/lessons/1-iterations/binary_gap/">原文</a>


A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N. </br>

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.</br>

Write a function:</br>

class Solution { public int solution(int N); }</br>

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.</br>

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.</br>


分析:將整數N 轉成bin ，再利用雙指針紀錄計算前後'1' 的距離，並且比較


```python
def solution(N):
    strbin=bin(N)[2:]
    left,max,right=0,0,0
    for index,s in enumerate(strbin):
        if s=='1':
            left=right
            right=index	
            max = right-left-1 if max <right-left-1 else max 	
    return  max
```


分析:將整數N轉成bin,在後頭加入e,在字串用'1',切割,取得不包含'e',最大長度</br>
Note:加入e的目的,避免最後一位非1
ex:'1000010000e'.split('1')</br>
    ['', '0000', '0000e']</br>

```python		
def solution(N):
    bin_array=(bin(N)[2:]+'e').split('1') 
    max=0
    for x in bin_array:
        if x !="" and 'e' not in x:
            max = len(x) if max <len(x) else max 
    return max
    
```

