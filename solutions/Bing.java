/* 
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca
 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
*/

import java.util.Scanner;
import java.util.TreeMap;

public class Bing {

    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	int N = sc.nextInt();

	TreeMap<String, Integer> search_history = new TreeMap<String, Integer>();
	for (int i = 0; i < N; i++) {
	    String word = sc.next();
	    if (search_history.containsKey(word))
		System.out.println(search_history.get(word));
	    else
		System.out.println(0);

	    for (int j = 1; j < word.length()+1; j++) {
		String word_slice = word.substring(0, j);
		if (search_history.containsKey(word_slice))
		    search_history.put(word_slice, search_history.get(word_slice)+1);
		else
		    search_history.put(word_slice, 1);
	    }
	}
    }
}
