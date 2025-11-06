import java.io.*;
import java.util.StringTokenizer;

public class UpdateInventory {
    public static void main(String[] args) {
        final int MAX = 100;
        InventoryItem[] items = new InventoryItem[MAX];
        StringTokenizer tokenizer;
        String line, name, file = "inventory.dat";
        int units, count = 0;
        float price;

        try {
            // Open the input file
            FileReader fr = new FileReader(file);
            BufferedReader inFile = new BufferedReader(fr);

            // Read data from the file and initialize inventory items
            line = inFile.readLine();
            while (line != null) {
                tokenizer = new StringTokenizer(line);
                name = tokenizer.nextToken();
                try {
                    units = Integer.parseInt(tokenizer.nextToken());
                    price = Float.parseFloat(tokenizer.nextToken());
                    items[count++] = new InventoryItem(name, units, price);
                } catch (NumberFormatException exception) {
                    System.out.println("Error in input. Line ignored.");
                    System.out.println(line);
                }
                line = inFile.readLine();
            }
            inFile.close();

            // Restock inventory
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("\nEnter the number of additional units for each item:");
            for (int i = 0; i < count; i++) {
                System.out.print(items[i].getName() + ": "); // 물품 이름 출력
                try {
                    int addedUnits = Integer.parseInt(userInput.readLine()); // 사용자 입력 읽기
                    items[i].restock(addedUnits); // 재고 갱신
                } catch (NumberFormatException exception) {
                    System.out.println("Invalid number. No units added for " + items[i].getName());
                }
            }

            // Write updated inventory back to the file
            FileWriter fw = new FileWriter(file);
            BufferedWriter outFile = new BufferedWriter(fw);

            for (int i = 0; i < count; i++) {
                outFile.write(items[i].getName() + " " + items[i].getUnits() + " " + items[i].getPrice());
                outFile.newLine();
            }

            outFile.close();
            System.out.println("\nInventory successfully updated!");

        } catch (FileNotFoundException exception) {
            System.out.println("The file " + file + " was not found.");
        } catch (IOException exception) {
            System.out.println("Error reading or writing file: " + exception.getMessage());
        }
    }
}
