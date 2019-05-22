#Prefix sums

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


python
```python
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

```

