package DynamicConnectivity;

public class QuickFindUF  implements UF{
    private int[] id;
    public QuickFindUF(int N){
        if(N<=0){
            throw new IllegalArgumentException("Graph must contain at least 1 object");
        }
        id = new int[N];
        for(int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    public void union(int p, int q){
        int idp = id[p];
        int idq = id[q];
        for(int i=0; i<id.length;i++){
            if(id[i]==idp) id[i]=idq;
        }
    }
    public boolean connected(int p, int q){
        return id[q]==id[p];
    }
}
