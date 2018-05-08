### QSort
  - Lumoto实现：pivot选最后一个数，用左起的指针推进指向比pivot小的数
  - Hoare实现，pivot选第一个数，左右两个指针同时向中间推进，找到一组>=pivot和<=pivot时就交换，相交时返回右指针