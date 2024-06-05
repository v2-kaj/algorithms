package DynamicConnectivity;

public class QuickFindUF {
    private int[] id;
    public QuickFindUF(int N){
        id = new int[N];
        for(int i=0;i<id.length;i++){
            id[i]=i;
        }
    }
    public boolean connected(int p, int q){
        return id[p]==id[q];
    }

    public void union(int p, int q){
        int pid = id[p];
        int qid = id[q];
        //0,1,2,3,4,5
        //3,1,5,3,5,5

        //union(4,2)
        //union(2,5)
        //union(0,3)
        for(int i=0; i<id.length;i++){
            if (id[i]==pid) id[i]=qid;
        }
    }
}
