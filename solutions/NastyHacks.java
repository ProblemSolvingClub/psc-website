/*
 Author: Jenny Le
 Email: jenny.le@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */

import java.util.*;

public class NastyHacks {
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int cases = kb.nextInt();

        for(int i = 0; i < cases; i++){
            int revNoAdvertise = kb.nextInt(); // revenue if you DON'T advertise
            int revAdvertise = kb.nextInt(); // revenue if you DO advertise
            int cost = kb.nextInt(); // cost of advertising

            revAdvertise = revAdvertise - cost; // add the cost of advertising to revAdvertise

            if (revNoAdvertise == revAdvertise){ // if both revenues are even
                System.out.println("does not matter");
            } else if (revNoAdvertise > revAdvertise) { // not advertising costs LESS than advertising
                System.out.println("do not advertise");
            } else {
                System.out.println("advertise"); // advertising costs LESS than not advertising
            }
        }
    }
}
