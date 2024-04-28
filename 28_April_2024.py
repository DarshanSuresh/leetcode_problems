"""
834. Sum of Distances in Tree
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:
Input: n = 1, edges = []
Output: [0]

Example 3:
Input: n = 2, edges = [[1,0]]
Output: [1,1]
 
Constraints:
1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""
from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list to represent the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize arrays to store subtree sizes and distances
        subtree_sizes = [0] * n
        node_distances = [0] * n
        
        # Step 2: Perform DFS to calculate subtree sizes and distances
        def dfs(node, parent):
            subtree_sizes[node] = 1
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    subtree_sizes[node] += subtree_sizes[child]
                    node_distances[node] += node_distances[child] + subtree_sizes[child]
        
        dfs(0, -1)  # Start DFS from node 0
        
        # Step 3: Calculate answer array based on distances
        result = [0] * n
        result[0] = node_distances[0]
        
        def calculate_distances(node, parent):
            for child in graph[node]:
                if child != parent:
                    result[child] = result[node] - subtree_sizes[child] + (n - subtree_sizes[child])
                    calculate_distances(child, node)
        
        calculate_distances(0, -1)
        return result
