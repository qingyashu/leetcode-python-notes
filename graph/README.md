# 1366. Directed Graph Loop
  - 基本思路：先构建图，然后判断是否存在环
  - BFS会超时
  - DFS需要注意数据类型才能通过：
    - 用outerVisited数组记录检查过的节点，按照一整颗树DFS遍历，把走过的节点都设成outervisited
    - 用recurVisited数组记录本次检查的节点，每次开始遍历一棵树时需要清零，回溯也需要清零
  - 需要注意的地方：
    - 用dict记录树的节点时，注意有些孤节点可能没有边相连，所以不会出现在V中。注意保持V和visited数组不会出现越界访问
