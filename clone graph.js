// leetcode  Given a reference of a node in a connected undirected graph.

// Return a deep copy (clone) of the graph.

// Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

// class Node {
//     public int val;
//     public List<Node> neighbors;
// }

const cloneGraph = function (node) {
  if (!node) return node;
  const hash = {};

  return helper(node, hash);
};

function helper(node, hash) {
  if (node.val in hash) return hash[node.val];
  const curr = new Node(node.val);
  hash[node.val] = curr;
  for (let child of node.neighbors) curr.neighbors.push(helper(child, hash));
  return curr;
}
