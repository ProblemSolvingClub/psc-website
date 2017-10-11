/*
 Author: Jenny Le
 Email: jenny.le@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */

import java.util.*;
 
public class Bijele {
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        
        int[] set = {1, 1, 2, 2, 2, 8}; // number of pieces in the set
        int[] userSet = new int[6]; // user input array
        int[] output = new int[6]; // result array

        for(int i = 0; i < 6; i++){
            userSet[i] = kb.nextInt(); // get the user input into here
        }

        for(int j = 0; j < 6; j++){
            output[j] = set[j] - userSet[j]; // set count - user count = result
            System.out.print(output[j] + " "); // print the result
        }        
    }

    public static void simplerButLessEfficientWay() {
        Scanner kb = new Scanner(System.in);

        String result = "";

        int king = kb.nextInt();
        int kingDifference = 1-king; // default piece count - user input

        int queen = kb.nextInt();
        int queenDifference = 1-queen;

        int rooks = kb.nextInt();
        int rooksDifference = 2-rooks;

        int bishops = kb.nextInt();
        int bishopsDifference = 2-bishops;

        int knights = kb.nextInt();
        int knightsDifference = 2-knights;

        int pawns = kb.nextInt();
        int pawnsDifference = 8-pawns;

        System.out.println(kingDifference + " " + queenDifference + " " +
			   rooksDifference + " " + bishopsDifference + " " +
			   knightsDifference + " " + pawnsDifference);
        // put it all together in a string
	
}
