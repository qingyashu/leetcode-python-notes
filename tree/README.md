### 94. Binary Tree Maximum Path Sum
  - 用递归：分别先计算左边最大半路径、右边最大半路径，更新最大路径，再返回最大半路经
  - 注意：考虑到负数，更新最大路径时，需要加入单自己节点、最大半路径的情况