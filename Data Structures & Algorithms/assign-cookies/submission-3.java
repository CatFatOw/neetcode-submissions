class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);
        int children = 0;
        int g_idx = 0;

        for (int size : s){
            if (g_idx < g.length && g[g_idx] <= size){
                children ++;
                g_idx += 1;
            }
            
        }
        return children;
        
    }
}