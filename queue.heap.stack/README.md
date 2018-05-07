### 685. First Unique Number In Stream
  - 另解：用双向链表队列记录unique item，repeated数组记录是否出现大于1次

### 401. Kth Smallest Number in Sorted Matrix
  - 用heap维护最小数
  - 先插入第一行， 之后每次拿出最小数，再放进下一行的数
  - 只需要循环k-1次即可

### 528. Flatten Nested List Iterator
  - 3种解法
    - 用递归，在初始化时直接flatten成数组记录下来。这种方法最容易实现，但也性能最差：初始化时O(n)，还占用O(n)空间
    - 用栈保存倒置的数组，hasNext时检查栈顶元素，如果是数组就弹栈、再压入倒置数组，直到栈顶为数。next调用hasNext后直接返回栈顶元素。这种方法初始化快，最差性能和第一种方法一样，但仍需要拷贝数组
    - 基本思路和第二种一样，但只用栈保存数组指针和下标，hasNext时检查栈顶，遇到数组就把这一层数组压栈，再压入下一层数组。这种方法初始化O(1)，不需要拷贝数组，空间O(d)，d为深度

### 104. Merge K Sorted Lists
  - 解法一：用堆，首先放入所有的非空链表头，之后一次弹出堆首加入新链表，堆中放入下一个节点
    - 注意：python heap中，push进的元素形式，用val做tuple首项元素，或者做key。
  - 解法二：用分治法，把数组分成两份，递归合并成两个链表，再对两个链表合并。
    - 注意：合并两个链表时注意仔细处理各种分情况：p1=None, p2=None。用dummy head。