/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.*;

public class QuickBrownFox {

    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	HashMap<String, Boolean> letter_check = new HashMap<String, Boolean>(26);
	String[] alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
			     "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
			     "u", "v", "w", "x", "y", "z"};

	int n = sc.nextInt();
	sc.nextLine();
	for (int i = 0; i < n; i++) {
	    for (String letter : alphabet)  // Reset the hashmap
		letter_check.put(letter, false);

	    String phrase = sc.nextLine().toLowerCase();
	    for (char letter : phrase.toCharArray()) {
		String sletter = Character.toString(letter);
		if (letter_check.containsKey(sletter))
		    letter_check.put(sletter, true);
	    }

	    String ans = "";
	    for (Map.Entry<String, Boolean> entry : letter_check.entrySet())
		if (entry.getValue().equals(false))
		    ans += entry.getKey();

	    ans = ans.equals("") ? "pangram" : "missing " + ans;
	    System.out.println(ans);
	}

	sc.close();
    }
}
