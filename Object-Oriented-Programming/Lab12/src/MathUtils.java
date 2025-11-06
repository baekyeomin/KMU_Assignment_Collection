// ****************************************************************
// MathUtils.java
//
// Provides static mathematical utility functions.
//
// ****************************************************************
public class MathUtils {
    //-------------------------------------------------------------
    // Returns the factorial of the argument given.
    // Throws IllegalArgumentException for invalid input.
    //-------------------------------------------------------------
    public static int factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers.");
        }
        if (n >= 17) {
            throw new IllegalArgumentException("Factorial result is too large for integers (n >= 17).");
        }

        int fac = 1;
        for (int i = n; i > 0; i--) {
            fac *= i;
        }
        return fac;
    }
}
