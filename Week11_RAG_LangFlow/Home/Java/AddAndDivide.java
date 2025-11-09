import java.util.Scanner;

public class AddAndDivide {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ask how many numbers to add
        System.out.print("Enter how many numbers you want to add: ");
        int count = scanner.nextInt();

        double sum = 0;

        // Input numbers and calculate sum
        for (int i = 1; i <= count; i++) {
            System.out.print("Enter number " + i + ": ");
            double num = scanner.nextDouble();
            sum += num;
        }

        // Ask for divisor
        System.out.print("Enter the number to divide the sum by: ");
        double divisor = scanner.nextDouble();

        // Handle division by zero
        if (divisor == 0) {
            System.out.println("Error: Cannot divide by zero.");
        } else {
            double result = sum / divisor;
            System.out.println("Sum of numbers: " + sum);
            System.out.println("Result after division: " + result);
        }

        scanner.close();
    }
}