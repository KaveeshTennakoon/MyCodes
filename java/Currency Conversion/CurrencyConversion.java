import java.util.Scanner;
import java.util.InputMismatchException;


public class CurrencyConversion {

    public static void main(String[] args) {

        // main code which ask the user to choose between two options to convert

        Scanner input = new Scanner(System.in);

        int option; 

        while (true) { //validates by looping untill correct data is entered 

            try { // exception handling
                System.out.println("Choose the conversion \n    1. USD to LKR \n    2. LKR to USD\n");
                System.out.print("Your option: ");

                option = input.nextInt();

                if (option == 1 || option == 2) {
                    break;
                } else {
                    System.out.println("\nPlease enter enter either '1' or '2'.\n");
                }
                
            } catch(InputMismatchException e) {
                System.out.println("\nPlease enter a valid integer.\n");
                input.nextLine();
            }
        }
        
        if (option == 1) {
            USDtoLKR(input);
        } else {
            LKRtoUSD(input);
        }

        input.close();
           
    }


    private static void USDtoLKR (Scanner input){

        // method that converts USD input into LKR

        Float USD; 
        while (true) { // loops untill non-negative float is entered

            try { // exception handling 

                System.out.print("\nEnter the amount in USD: ");
                USD = input.nextFloat();

                if (USD >= 0) {
                    break;
                } else {
                    System.out.println("Amount must not be negative");
                }
            } catch(InputMismatchException e) {
                System.out.println("Enter valid amount.");
                input.nextLine();
            }
        }

        Float LKR = USD * 320; //convertion by taking the rate as 320

        System.out.println("Your amount in LKR is Rs." + LKR);  
    }


    private static void LKRtoUSD(Scanner input){

        //method that converts LKR input into USD

        Float LKR; 
            while (true) { // loops untill non-negative float is entered

                try { // exception handling

                    System.out.print("\nEnter the amount in LKR: ");
                    LKR = input.nextFloat();

                    if (LKR >= 0) {
                        break;
                    } else {
                        System.out.println("Amount must not be negative");
                    }
                } catch(InputMismatchException e) {
                    System.out.println("Enter valid amount.");
                    input.nextLine();
                }
            }

            Float USD = LKR / 320; //conversion by the rate is 320

            System.out.println("Your amount in LKR is $" + USD);

    }
}