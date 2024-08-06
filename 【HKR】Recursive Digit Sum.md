# Recursive Digit Sum
### 题目描述：
We define super digit of an integer `x` using the following rules:<br/>
Given an integer, we need to find the super digit of the integer.<br/>
- If `x` has only 1 digit, then its super digit is `x`.<br/>
- Otherwise, the super digit of `x` is equal to the super digit of the sum of the digits of `x`.<br/>

For example, the super digit of `x` will be calculated as:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super_digit(9875)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9+8+7+5 = 29<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super_digit(29)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 + 9 = 11<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super_digit(11)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 + 1 = 2<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;super_digit(2)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= 2<br/>  

The Initial input of `x` can be multiply by number `k`<br/>

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.<br/>

SuperDigit has the following parameter(s):<br/>
- string `n`: a string representation of an integer<br/>
- int `k`: the times to concatenate to make<br/>

Returns<br/>
int: the super digit of  repeated  times<br/>

Constraints<br/>
- 1<= `n` <= 10^100000<br/>
- 1<= `k` <= 10^5<br/>

### 解题思路：
1. 题目的标题已经很明确的告诉我们，这是用递归解决问题
2. 递归问题的常规思路
   1. 定义边界条件---从题目给到的例子，我们很容易想到，边界条件为`len(n)`为1的时候，此时直接`return` `n`的整数形式。
   2. 定义重复的字问题---那么每次递归，下一阶的输入应该是上一阶`n`的所有位数的加和，字符串形式。注意，除了第一次`k`为输入值，后续应都为`1`。
  
### Python语法:
1. `String`的Multiply，可以直接使用`*`，即 `n` * `k`
2. `String`的每一位相加，不需要把`String`转换成`Array`，因为`String`也可以用：`[x for x in str]`的表达式
