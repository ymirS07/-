# Sum vs XOR
### 题目描述
Given an integer `n`, find each `x` such that:
- 0 <= x <= n
- n + x = n @ x

where `@` denotes the `bitwise XOR` operator. Return the number of `x`'s satisfying the criteria.

Example:<br/>
n = 4<br/>
There are four values that meet the criteria:<br/>
4 + 0 = 4 @ 0<br/>
4 + 1 = 4 @ 1<br/>
4 + 2 = 4 @ 2<br/>
4 + 3 = 4 @ 3<br/>
Return 4.

Function sumXor has the following parameter(s):<br/>
- int n: an integer

Returns:<br/>
- int: the number of values found

Input Format:

A single integer, `n`.

Constraints: 0 <= n <= 10^15

### 解题思路
1. XOR的逻辑，位运算中，上下不同的将记为1，上下相同的将记为0<br/>
2. 因为x是小与n的所有整数，那么在二进制数中，x的二进制数的1的位置将永远是n的长度范围内，那么其实就是找0，然后排列组合<br/>
3. 我们发现规律，符合条件的个数为2的y-1(0的个数减首0)次方

### Python语法
1. bin(n)计算n的二进制数<br/>
2. bin(n)返回字符串
