/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.lang.Math;

public class Peragrams {

    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	String string_to_check = sc.next();
	sc.close();

	// Note that we can NOT use primitive types in collections.
	HashMap<String, Integer> letter_count_map = new HashMap<String, Integer>();

	for (int i = 0; i < string_to_check.length(); i++) {
	    String character = Character.toString(string_to_check.charAt(i));
	    if (letter_count_map.containsKey(character)) {
		letter_count_map.put(character, letter_count_map.get(character)+1);
	    } else    // Add the letter to the map if it doesn't exist.
		letter_count_map.put(character, 1);
	}

	ArrayList<Integer> letter_counts = new ArrayList<Integer>(letter_count_map.values());
	int odd_counts = 0;
	// Iterate through the letter counts and count how many are odd.
	for (Integer n : letter_counts) {
	    if (n % 2 != 0)
		odd_counts++;
	}

	System.out.println(Math.max(odd_counts-1, 0));
    }
}
