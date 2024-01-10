import java.util.Random;

public class Exercise2 {
    public static void main(String[] args) {
        Random rand = new Random();

        for (int i = 0; i < 25; i++){
            int j = rand.nextInt(100);
            int k = rand.nextInt(100);

            if (j > k) {
                System.out.println(j +  " " + "Is greater than k" + k);
            }
            else if (j < k) {
                System.out.println(j + " " + "is lesser than k" + k);
            }
            else {
                System.out.println(j + " " +"is equal to k" + k);
            }
        }
    }
}