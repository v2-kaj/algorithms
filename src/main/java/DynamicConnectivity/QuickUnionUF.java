package DynamicConnectivity;

public class QuickUnionUF implements UF{
    private final int[] roots;
    public QuickUnionUF(int N){
        roots= new int[N];
        for(int i=0;i<roots.length;i++){
            roots[i]=i;
        }
    }  private int root(int k) throws IndexOutOfBoundsException {
        try{
            while(k!=roots[k]) k=roots[k];
            return k;
        }catch(IndexOutOfBoundsException e){
            throw new IndexOutOfBoundsException(k+" not in the graph");
        }

    }



    public boolean connected(int p, int r){
        try{
            return root(p)==root(r);
        }catch (IndexOutOfBoundsException e){
            System.out.println(e.getMessage());
            return false;
        }

    }

    public void union(int p, int r){
        try {
            int rp = root(p);
            int rr = root(r);
            roots[rp] = rr;
        }catch(IndexOutOfBoundsException e){
            System.out.println(e.getMessage());
        }
    }

}
