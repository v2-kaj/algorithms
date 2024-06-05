package DynamicConnectivity;

public class QuickUnionUF implements UF{
    private int[] id;
    public QuickUnionUF(int N){
        id = new int[N];
        for(int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    private int root(int i){
        while(i != id[i]) i=id[i];
        return i;
    }
    public boolean connected(int p, int q){
        return root(p)==root(q);
    }
    public void union(int p, int q){
        int rp = root(p);
        int rq = root(q);
        id[rp]=rq;
    }
}
