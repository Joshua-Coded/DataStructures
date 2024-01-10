import java.util.Random;

public class InfiniteRandomValues {
    public static void main(String[] args) {
        Random random = new Random();

        while (true) {
            int value1 = random.nextInt(100);
            int value2 = random.nextInt(100);

            if (value1 > value2) {
                System.out.println(value1 + " is greater than " + value2);
            } else if (value1 < value2) {
                System.out.println(value1 + " is less than " + value2);
            } else {
                System.out.println(value1 + " is equal to " + value2);
            }
        }
    }
}
