// ****************************************************************
// CountLetters.java
//
// Reads a word or sentence from the standard input and prints the 
// number of occurrences of each letter. Non-alphabet characters are
// ignored but printed as "Not a letter".
//
// ****************************************************************
import java.util.Scanner;

public class CountLetters {
    public static void main(String[] args) {
        int[] counts = new int[26];
        Scanner in = new Scanner(System.in);

        // get word or sentence from user
        System.out.print("Enter a word or sentence: ");
        String input = in.nextLine();

        // convert to all upper case
        input = input.toUpperCase();

        // count frequency of each letter in the string
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            try {
                counts[ch - 'A']++;
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Not a letter: " + ch);
            }
        }

        // print frequencies
        System.out.println();
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] != 0) {
                System.out.println((char) (i + 'A') + ": " + counts[i]);
            }
        }
    }
}


