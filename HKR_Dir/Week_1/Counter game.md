# Counter game
### 题目描述：
Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2.<br/>
If it is, they divide it by 2.<br/>
If not, they reduce it by the next lower number which is a power of 2. Whoever reduces the number to 1 wins the game.<br/>
**Louise always starts.** <br/>

Given an initial value, determine who wins the game.

Example:

It's Louise's turn first. She determines that 132 is not a power of 2. The next lower power of 2 is 128, so she subtracts that from 132 and passes 4 to Richard.<br/>
4 is a power of 2, so Richard divides it by 2 and passes 2 to Louise.<br/>
Likewise, 2 is a power so she divides it by 2 and reaches 1. She wins the game.<br/>

**HINT** Update If they initially set counter to 1, Richard wins. Louise cannot make a move so she loses.

counterGame has the following parameter(s):<br/>
int n: the initial game counter value

Returns<br/>
string: either Richard or Louise

### 解题思路：
1. 模拟的思路：如果输入即为1，那么按照题目，Richard获胜；如果输入大于一，那么进入循环（或者递归）：判断当前输入是否为2的幂（power of 2），如果是，那么直接除二，如果不是，则减去该数范围内2最大的幂。
2. 要注意的是，判断谁赢取决于谁拿到了最后一步，那么就要记录操作次数来判断。因为循环条件为`>1`，所以退出循环即为所有操作完成，即当操作次数为单数时，Louise获胜，当操作次数为双数时，Richard获胜。
3. 计算是否为2的幂的方法，调用math包的log2()方法，`math.log2(n)==0`，如果是整数，那么n为2的幂，否则不是。
