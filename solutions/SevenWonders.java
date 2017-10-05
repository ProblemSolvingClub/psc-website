/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.Scanner;
import static java.lang.Math.min;

public class SevenWonders {

    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	String cards = sc.next();
	sc.close();

	int tablet = 0;
	int compass = 0;
	int gear = 0;

	for (int i = 0; i < cards.length(); i++) {
	    switch (cards.charAt(i)) {
	    case 'T':
		tablet++;
		break;
	    case 'C':
		compass++;
		break;
	    case 'G':
		gear++;
		break;
	    }
	}

	int total = (tablet*tablet +
		     compass*compass +
		     gear*gear +
		     7*min(min(tablet, compass), gear));

	System.out.println(total);
    }
}
