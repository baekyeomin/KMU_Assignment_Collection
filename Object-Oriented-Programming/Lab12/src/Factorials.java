// ****************************************************************
// Factorials.java
//
// Reads integers from the user and prints the factorial of each.
// Handles exceptions for invalid input.
//
// ****************************************************************
import java.util.Scanner;

public class Factorials {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char keepGoing = 'y';

        while (keepGoing == 'y' || keepGoing == 'Y') {
            try {
                System.out.print("Enter an integer: ");
                int val = in.nextInt();
                System.out.println("Factorial(" + val + ") = " + MathUtils.factorial(val));
            } catch (IllegalArgumentException e) {
                // Handle invalid input
                System.out.println("Error: " + e.getMessage());
            }

            System.out.print("Another factorial? (y/n) ");
            keepGoing = in.next().charAt(0);
        }

        System.out.println("Goodbye!");
    }
}
