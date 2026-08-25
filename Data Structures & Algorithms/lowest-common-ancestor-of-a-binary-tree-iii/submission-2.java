/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node lowestCommonAncestor(Node p, Node q) {
        return dfs(p, q);
        
    }

    public int depth(Node node) {
        int count = 0;

        while (node != null) {
            count++;
            node = node.parent;
        }

        return count;
    }

    public Node dfs(Node p, Node q){
        
        if (p == null && q == null){
            return null;
        }
        
        if (p == q){
            return p;
        }
        int depth_q = depth(q);
        int depth_p = depth(p);
        
        if (depth_p > depth_q){
            return dfs(p.parent, q);
        }
        else if (depth_p < depth_q){
            return dfs(p, q.parent);
        }
        else{
            return dfs(p.parent, q.parent);
        }
    }

    
}