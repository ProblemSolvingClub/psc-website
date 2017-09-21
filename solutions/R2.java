/*
 Author: Martin Tran
 Discord: Theo
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem
 to the email above or ask in the CPC discord.
 */
import java.util.Scanner;

public class R2 {

    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	
	int r1 = sc.nextInt();
	int s = sc.nextInt();
	sc.close();
	
	int r2 = 2 * s - r1;
	
	System.out.println(r2);
    }
}
