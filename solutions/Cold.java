/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.Scanner;

public class Cold {

    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	
	int count = 0;
	int n = sc.nextInt(); 
	
	for(int i = 0; i < n; i++){
	    int next = sc.nextInt();
	    
	    if(next < 0)
		count ++;
	}
	
	System.out.println(count);
	sc.close();	
    }   
}
