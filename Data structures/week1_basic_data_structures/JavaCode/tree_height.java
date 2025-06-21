import java.util.*;
import java.io.*;

public class tree_height {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;

        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }
        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    public class TreeHeight {
        int n;
        int parent[];
        int depth[];

        void read() throws IOException {
            FastScanner in = new FastScanner();
            n = in.nextInt();
            parent = new int[n];
            depth = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = in.nextInt();
                depth[i] = -1;
            }
        }



        int computeHeight() {
            // Replace this code with a faster implementation
//            int maxHeight = 0;
//            for (int vertex = 0; vertex < n; vertex++) {
//                int height = 0;
//                for (int i = vertex; i != -1; i = parent[i])
//                    height++;
//                maxHeight = Math.max(maxHeight, height);
//            }
//            return maxHeight;

            int maxHeight = 0;
            for (int i = 0; i < n; i++){
                findDepth(i);
            }

            for (int i = 0; i < n; i++){
                maxHeight = Math.max(maxHeight,depth[i]);
            }
            return maxHeight;

        }

        int findDepth(int i){

            if (parent[i] == -1){
                depth[i] = 1;
                return 1;
            }else if (parent[i] != -1 && depth[i] == -1){
                return depth[i] = 1 + findDepth(parent[i]);
            }else{
                return depth[i];
            }

        }



    }

    static public void main(String[] args) throws IOException {
        new Thread(null, new Runnable() {
            public void run() {
                try {
                    new tree_height().run();
                } catch (IOException e) {
                }
            }
        }, "1", 1 << 26).start();
    }
    public void run() throws IOException {
        TreeHeight tree = new TreeHeight();
        tree.read();
        System.out.println(tree.computeHeight());
    }
}
