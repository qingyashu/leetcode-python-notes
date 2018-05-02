### 685. First Unique Number In Stream
  - 另解：用双向链表队列记录unique item，repeated数组记录是否出现大于1次

### 384. Longest Substring Without Repeating Characters
  - 哈希表存字母最后一次出现的位置
  - 遍历字符串，根据包含左边字母的最长子串来计算包含当前字母的结果，更新哈希表和长度

### 401. Kth Smallest Number in Sorted Matrix
  - 用heap维护最小数
  - 先插入第一行， 之后每次拿出最小数，再放进下一行的数
  - 只需要循环k-1次即可