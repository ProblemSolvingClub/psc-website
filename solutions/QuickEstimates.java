/*
 Author: Martin Tran
 Discord: Theo
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem
 to the email above or ask in the CPC discord.
 */
import java.util.Scanner;

public class QuickEstimates {

    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	int N = sc.nextInt();

	for (int i = 0; i < N; i++) {
	    String number = sc.next();    // Just read the number as a string.
	    int length = number.length();    // Get the length of the 'number'.
	    System.out.println(length);
	}
    }
}
