* Take a look to javascript code, there is another simple approach to solve this problem
#### **Approach 1 (Get Height Of Tree Rooted At Each Node)**
  * We can perform a traversal of the tree and at each node get the height of its left and right subtrees.
  * This wastes time as we will be repeating work and the traversal of nodes.
#### **Approach 2 (Drill Down With Recursion And Respond Back Up)**
  * We can notice that we don't need to know the heights of all of the subtrees all at once.
  * All we need to know is whether a subtree is height balanced or not and the height of the tree rooted at that node, not information about any of its descendants.
  * **Our base case** is that a null node (we went past the leaves in our recursion) is height balanced and has a height of -1 since it is an empty tree.
  * So the key is that we will drive towards our base case of the null leaf descendant and deduce and check heights on the way upwards.
#### Key points of interest:
  1. Is the subtree height balanced?
  2. What is the height of the tree rooted at that node?
#### Complexities
* **Time: O( n )**
  * This is a postorder traversal (left right node) with possible early termination if any left subtree turns out unbalanced and an early result bubbles back up.
  * **At worst** we will still touch all n nodes if we have no early termination.
* **Space: O( h )**
  * Our call stack (from recursion) will only go as far deep as the height of the tree, so h (the height of the tree) is our space bound for the amount of call stack frames that we will create.
