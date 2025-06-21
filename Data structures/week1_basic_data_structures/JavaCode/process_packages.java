import java.io.IOException;
import java.util.*;

class Request {
    public Request(int arrival_time, int process_time) {
        this.arrival_time = arrival_time;
        this.process_time = process_time;
    }

    public int arrival_time;
    public int process_time;
}

class Response {
    public Response(boolean dropped, int start_time) {
        this.dropped = dropped;
        this.start_time = start_time;
    }

    public boolean dropped;
    public int start_time;
}

class Buffer {
    private static int current_time = 0;
    public Buffer(int size) {
        this.size_ = size;
        this.finish_time_ = new LinkedList<>();
        this.last_process_time = 0;
    }

    private final int size_;
    private final Deque<Integer> finish_time_;
    int last_process_time;

    public Response Process(Request request) {
        // write your code here
        int req_finish_time;

        while (!finish_time_.isEmpty()){
            if (request.arrival_time < finish_time_.peek()){
                break;
            }else{
                finish_time_.remove();
            }
        }

        if(!finish_time_.isEmpty()){
            if(finish_time_.peekLast() < request.arrival_time){
                req_finish_time = request.arrival_time + request.process_time;
                last_process_time = request.arrival_time;
            }else{
                req_finish_time = finish_time_.peekLast() + request.process_time;
                last_process_time = finish_time_.peekLast();
            }
        }else {
            req_finish_time = request.arrival_time + request.process_time;
            last_process_time = request.arrival_time;
        }

        if (finish_time_.size() == size_){
            return new Response(true, -1);
        }else{
            finish_time_.add(req_finish_time);
            return new Response(false, last_process_time);
        }

    }

//    private ArrayList<Integer> finish_time_;
}

class process_packages {
    private static ArrayList<Request> ReadQueries(Scanner scanner) throws IOException {
        int requests_count = scanner.nextInt();
        ArrayList<Request> requests = new ArrayList<Request>();
        for (int i = 0; i < requests_count; ++i) {
            int arrival_time = scanner.nextInt();
            int process_time = scanner.nextInt();
            requests.add(new Request(arrival_time, process_time));
        }
        return requests;
    }

    private static ArrayList<Response> ProcessRequests(ArrayList<Request> requests, Buffer buffer) {
        ArrayList<Response> responses = new ArrayList<Response>();
        for (int i = 0; i < requests.size(); ++i) {
            responses.add(buffer.Process(requests.get(i)));
        }
        return responses;
    }

    private static void PrintResponses(ArrayList<Response> responses) {
        for (int i = 0; i < responses.size(); ++i) {
            Response response = responses.get(i);
            if (response.dropped) {
                System.out.println(-1);
            } else {
                System.out.println(response.start_time);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        int buffer_max_size = scanner.nextInt();
        Buffer buffer = new Buffer(buffer_max_size);

        ArrayList<Request> requests = ReadQueries(scanner);
        ArrayList<Response> responses = ProcessRequests(requests, buffer);
        PrintResponses(responses);
    }
}
