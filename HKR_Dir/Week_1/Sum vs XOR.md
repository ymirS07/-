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

