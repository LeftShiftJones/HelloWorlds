import java.util.Scanner;

public class TwitterSplitter {

    public void split_message(String message) {
        int message_length = message.length();
        String local_message = message;
        while(true) {
            int last_space = -1;
            //ending / shorter than 140 case
            if(local_message.length() < 140) {
                System.out.println(local_message);
                break;
            }
            for(int i = 139; i > 0; i--) {
                if(local_message.charAt(i) == ' ') {
                    last_space = i;
                    break;
                }
            }
            if(last_space == -1) {
                System.out.println(local_message.substring(0, 140) + "\n");
                local_message = local_message.substring(140);
            } else {
                System.out.println(local_message.substring(0, last_space) + "\n");
                local_message = local_message.substring(last_space+1);
            }
        }

    }

    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String message = scan.nextLine();
        TwitterSplitter ts = new TwitterSplitter();
        ts.split_message(message);
        scan.close();
    }
}