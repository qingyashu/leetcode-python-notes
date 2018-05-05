### 685. First Unique Number In Stream
  - 另解：用双向链表队列记录unique item，repeated数组记录是否出现大于1次

### 384. Longest Substring Without Repeating Characters
  - 哈希表存字母最后一次出现的位置
  - 遍历字符串，根据包含左边字母的最长子串来计算包含当前字母的结果，更新哈希表和长度

### 401. Kth Smallest Number in Sorted Matrix
  - 用heap维护最小数
  - 先插入第一行， 之后每次拿出最小数，再放进下一行的数
  - 只需要循环k-1次即可

### 528.Flatten_Nested_List_Iterator
  - 3种解法
    - 用递归，在初始化时直接flatten成数组记录下来。这种方法最容易实现，但也性能最差：初始化时O(n)，还占用O(n)空间
    - 用栈保存倒置的数组，hasNext时检查栈顶元素，如果是数组就弹栈、再压入倒置数组，直到栈顶为数。next调用hasNext后直接返回栈顶元素。这种方法初始化快，最差性能和第一种方法一样，但仍需要拷贝数组
    - 基本思路和第二种一样，但只用栈保存数组指针和下标，hasNext时检查栈顶，遇到数组就把这一层数组压栈，再压入下一层数组。这种方法初始化O(1)，不需要拷贝数组，空间O(d)，d为深度
