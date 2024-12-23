# [2471. Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level?envType=daily-question&envId=2024-12-23)

**Type:** Medium <br>
**Topics:** Tree, Breadth First Search, Binary Tree <br>
**Companies:** Guidewire, Amazon
<hr>

You are given the `root` of a binary tree with **unique values**.

In one operation, you can choose any two nodes **at the same level** and swap their values.

Return *the minimum number of operations needed to make the values at each level sorted in a ***strictly increasing order***.*

The **level** of a node is the number of edges along the path between it and the root node.
<hr>

### Examples:
- **Example 1:** <br>
![](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174006-2.png) <br>
**Input:** root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10] <br>
**Output:** 3 <br>
**Explanation:** <br> - Swap 4 and 3. The 2nd level becomes [3,4]. <br> - Swap 7 and 5. The 3rd level becomes [5,6,8,7]. <br> - Swap 8 and 7. The 3rd level becomes [5,6,7,8]. <br> We used 3 operations so return 3. <br> It can be proven that 3 is the minimum number of operations needed.

- **Example 2:** <br>
![](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174026-3.png) <br>
**Input:** root = [1,3,2,7,6,5,4] <br>
**Output:** 3 <br>
**Explanation:** <br> - Swap 3 and 2. The 2nd level becomes [2,3]. <br> - Swap 7 and 4. The 3rd level becomes [4,6,5,7]. <br> - Swap 6 and 5. The 3rd level becomes [4,5,6,7]. <br> We used 3 operations so return 3. <br> It can be proven that 3 is the minimum number of operations needed.

- **Example 3:** <br>
![](https://assets.leetcode.com/uploads/2022/09/18/image-20220918174052-4.png) <br>
**Input:** root = [1,2,3,4,5,6] <br>
**Output:** 0 <br>
**Explanation:** Each level is already sorted in increasing order so return 0.
<hr>

### Constraints:
- The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.
- <code>1 <= Node.val <= 10<sup>5</sup></code>
- All the values of the tree are **unique**.
<hr>

### Hints:
- We can group the values level by level and solve each group independently.
- Do BFS to group the value level by level.
- Find the minimum number of swaps to sort the array of each level.
- While iterating over the array, check the current element, and if not in the correct index, replace that element with the index of the element which should have come.
<hr>