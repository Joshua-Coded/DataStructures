import java.util.Scanner;

public class VelocityCalculator {
    public static void main(String[] args) {
 
    Scanner scanner = new Scanner(System.in);

    // get distance from user.
    System.out.println("Enter the distance (in meters) ");
    double distance = scanner.nextDouble();


    // get time from the user.
    System.out.println("Enter the time (in seconds) ");
    double time = scanner.nextDouble();

    // calulate the velocity using the formula: velocity = distance / time
    double velocity = calulateVelocity(distance, time);

    // display the result
    System.out.println("The velocity is " + velocity + " meters per second");

   
}

public static double  calulateVelocity(double distance, double time) {
    return distance / time;
}
}