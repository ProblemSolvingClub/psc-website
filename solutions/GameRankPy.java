/*
 Author: Martin Tran (based on Thomas Vu's Python solution)
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem
 to the email above or ask in the CPC discord.
 */
import java.util.Scanner;

public class GameRankPy {

    public static int rank = 25;
    public static int stars = 0;
    public static int streak = 0;
    public static boolean isLegend = false;
    
    public static void main(String args[]) {
	Scanner sc = new Scanner(System.in);
	String sequence = sc.next();
	sc.close();

	// Loop through each match in the sequence.
	for (int i = 0; i < sequence.length(); i++) {
	    if (sequence.charAt(i) == 'W') {
		streak ++;
		if (streak >= 3 && rank <= 25 && rank >= 6)
		    addStar();
		addStar();
	    } else {
		streak = 0;
		if (rank <= 19 || (rank == 20 && stars > 0))
		    loseStar();
	    }
	}

	if (isLegend)
	    System.out.println("Legend");
	else
	    System.out.println(rank);
    }

    // Returns the number of stars needed to rank up.
    public static int starsForRank() {
	if (rank <= 25 && rank >= 21)
	    return 2;
	if (rank <= 20 && rank >= 16)
	    return 3;
	if (rank <= 15 && rank >= 11)
	    return 4;
	if (rank <= 10 && rank >= 1)
	    return 5;
	else
	    return 0;
    }

    // Adds a star or rank up if you have enough stars.
    public static void addStar() {
	if (stars == starsForRank()) {
	    rank --;
	    stars = 1;
	    if (rank == 0)
		isLegend = true;
	} else
	    stars ++;
    }

    // Lose a star or rank if we are past rank 20.
    public static void loseStar() {
	if (stars == 0) {
	    rank ++;
	    stars = starsForRank() - 1;
	} else
	    stars --;
    }
}
