import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();

        boolean error = false;
        int errorBracketPosition = -1;
        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);

            if (next == '(' || next == '[' || next == '{') {
                opening_brackets_stack.push(new Bracket(next, position));
            }

            if (next == ')' || next == ']' || next == '}') {
                if (!opening_brackets_stack.isEmpty()){
                    Bracket bracket = opening_brackets_stack.peek();
                    if(bracket.type == '{'){
                        if(next == '}') {
                            opening_brackets_stack.pop();
                        }else{
                            error = true;
                            errorBracketPosition = position;
                            break;
                        }
                    }
                    else if(bracket.type == '('){
                        if(next == ')'){
                            opening_brackets_stack.pop();
                        }else{
                            error = true;
                            errorBracketPosition = position;
                            break;
                        }
                    }
                    else if(bracket.type == '['){
                        if(next == ']'){
                            opening_brackets_stack.pop();
                        }else{
                            error = true;
                            errorBracketPosition = position;
                            break;
                        }
                    }
                }else{
                    error = true;
                    errorBracketPosition = position;
                    break;
                }
            }
        }

        if (error){
            System.out.println(errorBracketPosition+1);
        } else if (!opening_brackets_stack.isEmpty()) {
            System.out.println(opening_brackets_stack.pop().position+1);
        } else{
            System.out.println("Success");
        }
    }
}
