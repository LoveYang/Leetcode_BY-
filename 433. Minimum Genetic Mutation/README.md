# Leetcode_BY-
工作前的刷题-转行的决心！
# Minimum Genetic Mutation
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, 

"AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"

end:   "AACCGGTA"

bank: ["AACCGGTA"]

return: 1

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

Example 3:

start: "AAAAACCC"

end:   "AACCCCCC"

bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3

解题思路：
1.count_dis 求两个基因的最小突变距离
用迭代的方式搜索bank中的基因，
minMutation
1. 移除bank中和start相同的基因
2. 在bank中找一个基因x，如果start到x的距离不是1，说明start不能突变到x，继续找下一个x，如果距离是1，就可以找x到end的距离（这一步可以用迭代完成）
3. 迭代退出条件： -1:bank搜索完毕也没找到或者bank长度小于start到end的距离。1：搜索到最后能在bank中找到离end距离为1的基因。如果找到（返回为1），后续返回每次+1就可以得到start到end 的距离。
4. 由于上面步骤找到的是按bank直接顺序搜索到的结果，不一定是最近距离，所以在每次搜索前按bank中的元素具end的距离从小到大排序，这样顺序搜索的结果就是最小值