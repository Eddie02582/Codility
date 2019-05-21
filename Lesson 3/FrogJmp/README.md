# FrogJmp


<a href="https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/">原文</a>

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D. </br>

Count the minimal number of jumps that the small frog must perform to reach its target.</br>

Write a function:</br>

class Solution { public int solution(int X, int Y, int D); }</br>

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.</br>

For example, given:</br>
```
  X = 10
  Y = 85
  D = 30
```
the function should return 3, because the frog will be positioned as follows:</br>

<ul>
    <li>after the first jump, at position 10 + 30 = 40</li>
    <li>after the second jump, at position 10 + 30 + 30 = 70</li>
    <li>after the third jump, at position 10 + 30 + 30 + 30 = 100</li>
</ul>

Write an efficient algorithm for the following assumptions:</br>
<ul>
    <li>X, Y and D are integers within the range [1..1,000,000,000];</li>
    <li>X ≤ Y.</li>
</ul>



分析:(目地-起始位置)/步伐 ，無條件取整數

C#
```csharp
using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
    public int solution(int X, int Y, int D) {
        return (int)Math.Ceiling((double)(Y - X) / D);
    }
	
}
```
