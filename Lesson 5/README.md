# Prefix sums

有一種簡單而強大的技術，可以快速計算總和,再給給定切片中的元素（數組的連續段）。</br> 
它的主要思想是使用前綴和被定義為第一個0,1,2，...的連續總數。。。 ，n個數組元素。</br>

<table>
    <th>
        <td>a<sub>0</sub></td>
        <td>a<sub>1</sub></td>
        <td>a<sub>2</sub></td>       
        <td>....</td>
        <td>a<sub>n-1</sub></td>
    </th>
    <tr>
        <td>p<sub>0</sub>=0</td>
        <td>p<sub>1</sub>=a<sub>0</sub></td>
        <td>p<sub>2</sub>=a<sub>0</sub>+a<sub>1</sub></td>
        <td>p<sub>3</sub>=a<sub>0</sub>+a<sub>1</sub>+a<sub>2</sub></td>
        <td>....</td>
        <td>p<sub>n</sub>=a<sub>0</sub>+a<sub>1</sub>+...+a<sub>n-1</sub></td>
    </tr>

</table>

** 5.1: Counting prefix sums — O(n).**

```python
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

```

同理假設我們想取得[x,y]之間的合,0 <= x ,y <= n,其總合為a<sub>x</sub>+a<sub>1</sub>+...+a<sub>y-1</sub>+a<sub>y</sub> </br>

<table>
    <th>
        <td>p<sub>y+1</sub></td>
        <td>a<sub>0</sub></td>
        <td>a<sub>1</sub></td>       
        <td>....</td>
        <td>a<sub>x-1</sub></td>       
        <td>a<sub>x</sub></td>
        <td>a<sub>x+1</sub></td>
        <td>....</td>
        <td>a<sub>y-1</sub></td>       
        <td>a<sub>y</sub></td>    
    </th>
    <tr>
        <td>p<sub>x</sub></td>
        <td>a<sub>0</sub></td>
        <td>a<sub>1</sub></td>       
        <td>....</td>
        <td>a<sub>x-1</sub></td>       
        <td>a<sub>x</sub></td>
        <td>a<sub></sub></td>
        <td></td>
        <td>a<sub></sub></td>       
        <td>a<sub></sub></td>  
    </tr>
    <tr>
        <td>p<sub>y+1</sub>-p<sub>x</sub></td>
        <td></td>
        <td></td>       
        <td></td>
        <td></td>       
        <td>a<sub>x</sub></td>
        <td>a<sub>x+1</sub></td>
        <td>....</td>
        <td>a<sub>y-1</sub></td>       
        <td>a<sub>y</sub></td>  
    </tr>
</table>


**5.2: Total of one slice — O(1).**
```python
def count_total(P, x, y):
    return P[y + 1] - P[x]
```


## Exercise

Problem: You are given a non-empty, zero-indexed array A of n [1,100000],integers a0, a1, . . . , an−1 [0,1000]. </br>
This array represents number of mushrooms growing on the consecutive spots along a road. You are also given integers k and m [0,n].</br>
A mushroom picker is at spot number k on the road and should perform m moves. </br>
In one move she moves to an adjacent spot. She collects all the mushrooms growing on spots she visits. </br>
The goal is to calculate the maximum number of mushrooms that the mushroom picker can collect in m moves.</br>
A such that [2,3,7,5,1,3,9]

The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might move to spots 3, 2, 3, 4, 5, 6 and thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the maximal number of mushrooms she can collect.</br>

k為起點,m為可移動步伐,要找到總和最大的值</br>

**Solution** O(m<sup>2</sup>): Note that the best strategy is to move in one direction optionally followedby some moves in the opposite direction. </br>
In other words, the mushroom picker should not change direction more than once. With this observation we can find the simplest solution.</br>
Make the first p = 0, 1, 2, . . . , m moves in one direction, then the next m − p moves in theopposite direction. </br>
This is just a simple simulation of the moves of the mushroom picker </br>
which requires O(<sup>2</sup>)time.</br>



**Solution** O(n+m): A better approach is to use prefix sums. If we make p moves in one direction, we can calculate the maximal opposite location of the mushroom picker.</br>
The mushroom picker collects all mushrooms between these extremes. </br>
We can calculate the total number of collected mushrooms in constant time by using prefix sums.</br>


** 5.3: Mushroom picker — O(n + m)**

```python
def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    for p in xrange(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in xrange(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return resul
```


