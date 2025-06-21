import java.util.*;
import java.io.*;

public class StackWithMax {
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

    public void solve() throws IOException {
        FastScanner scanner = new FastScanner();
        int queries = scanner.nextInt();
//        Stack<Integer> stack = new Stack<Integer>();
        MyStack stack = new MyStack(5,5);

        for (int qi = 0; qi < queries; ++qi) {
            String operation = scanner.next();
            if ("push".equals(operation)) {
                int value = scanner.nextInt();
                stack.push(value);
            } else if ("pop".equals(operation)) {
                stack.pop();
            } else if ("max".equals(operation)) {
//                System.out.println(Collections.max(stack));
                System.out.println(stack.max());
            }
        }
    }

    static public void main(String[] args) throws IOException {
        new StackWithMax().solve();
    }
}

class MyStack{
    int initialSize;
    int[] numbers;
    int incrementValue;
    int size = 0;
    int currentPointer;

    public MyStack(int incrementValue, int initialSize){
        this.incrementValue = incrementValue;
        this.initialSize = initialSize;
        numbers = new int[initialSize];
    }

    public MyStack(){
        this(1,1);
    }

    void push(int number){
        if(size == 0){
            size++;
            numbers[0] = number;
            currentPointer = 0;
        }else if(currentPointer+1 == size){
            int[] tempArray = new int[size+incrementValue];
            for (int i = 0; i< size; i++){
                tempArray[i] = numbers[i];
            }
            numbers = tempArray;
            numbers[++currentPointer] = number;
            size++;
        }else{
            numbers[++currentPointer] = number;
            size++;
        }
    }

    void pop(){
        if(size > 0) {
            currentPointer--;
            size--;
        }
    }

    String max(){
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < size; i++){
            maxValue = Math.max(maxValue, numbers[i]);
        }

        if(maxValue != Integer.MIN_VALUE){
            return maxValue+"";
        }else{
            return "";
        }

    }

}
