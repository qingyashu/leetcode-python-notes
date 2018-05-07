### 384. Longest Substring Without Repeating Characters
  - Hash table
  - 哈希表存字母最后一次出现的位置
  - 遍历字符串，根据包含左边字母的最长子串来计算包含当前字母的结果，更新哈希表和长度

### 49. Sort Letters by Case
  - Python sort，用ord(c) 取字符ASCII码
  - 注意python函数参数为数组时，传递是数组引用，所以需要遍历传入的数组参数来修改
  - Python中sort()函数对原数组排序，返回None。读入的key参数为自定义函数，sort库根据key来递增排序

### 107. Word Break
  - DFS会超时
  - 动态规划
    - 注意在动归时，每一次状态更新都是遍历之前状态，而不是遍历dict中所有单词，因为后者还是会超时

### 118. Distinct Subsequences
  - DFS会超时
  - 动态规划
    - 注意python二维数组的初始化: 
```python
d = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
```
    - 为了边界条件方便，考虑用[i][j]表示i,j位置(exclusive)之前的情况，并且所有[i][0]=1