/*
 Author: Michael Hoang
 Email: mlhoang@ucalgary.ca

 Feel free to send any questions about this problem to the email above
 or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.*;

class Pet {
  public static void main(String args[]) {
    Scanner scan = new Scanner(System.in);
    int greatest = 0;
    int bigRow = 0;
    for(int i = 0; i < 5; i++) {
      int contender = 0;
      contender += scan.nextInt();
      contender += scan.nextInt();
      contender += scan.nextInt();
      contender += scan.nextInt();
      if(contender > greatest){
        greatest = contender;
        bigRow = i+1;
      }
    }
    System.out.println(bigRow + " " + greatest);
  }
}
