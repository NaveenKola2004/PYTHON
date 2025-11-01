public class Main{
    public static void main(String[] args) {

        int n[]={1,1,2,3,1,2,7};
        int c[]=new int[100];

        for (int i=0;i<n.length;i++){
            c[n[i]]++;
        }
        for (int j=0;j<c.length;j++){
            if (c[j]>1){
                System.out.println(j);
            }
        }
    }
}