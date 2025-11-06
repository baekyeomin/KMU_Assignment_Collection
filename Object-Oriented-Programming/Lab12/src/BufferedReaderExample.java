import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BufferedReaderExample {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;

        System.out.println("Enter text (type 'quit' to exit):");
        try {
            while (true) {
                line = in.readLine(); // 한 줄을 읽음
                if (line.equals("quit")) { // "quit"이면 종료
                    System.out.println("Exiting program.");
                    break;
                }

                StringTokenizer tokenizer = new StringTokenizer(line); // 입력된 줄로 초기화
                int wordCount = tokenizer.countTokens(); // 단어 수 계산

                System.out.println("There are " + wordCount + " words in this line.");
                while (tokenizer.hasMoreTokens()) { // 토큰이 남아있는 동안 반복
                    System.out.println(tokenizer.nextToken()); // 한 단어씩 출력
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading input: " + e.getMessage());
        }
    }
}
