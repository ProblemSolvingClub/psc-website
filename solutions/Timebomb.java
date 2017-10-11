/*
 Author: Martin Tran
 Email: martin.tran@ucalgary.ca

 Feel free to send any questions about this problem to the email
 above or ask in the CPC discord. (discord.gg/MEXwfze)
 */
import java.util.Scanner;

public class Timebomb {

    public static void main(String args[]) {
	// ASCII 0-9. Each line is one number.
	String[] numbers = {"**** ** ** ****",
			    "  *  *  *  *  *",
			    "***  *****  ***",
			    "***  ****  ****",
			    "* ** ****  *  *",
			    "****  ***  ****",
			    "****  **** ****",
			    "***  *  *  *  *",
			    "**** ***** ****",
			    "**** ****  ****"};

	String[] bombcode = {"", "", "", "", "", "", "", ""};

	Scanner sc = new Scanner(System.in);
	String line;
	for (int i = 0; i < 5; i++) {
	    line = sc.nextLine() + " ";
	    for (int j = 0; j < line.length()/4; j++)
		bombcode[j] += line.substring(4*j, (4*(j+1))-1);
	}

	String translated_code = "";
	for (String s : bombcode) {
	    if (s.equals(numbers[0]))
		translated_code += "0";
	    else if (s.equals(numbers[1]))
		translated_code += "1";
	    else if (s.equals(numbers[2]))
		translated_code += "2";
	    else if (s.equals(numbers[3]))
		translated_code += "3";
	    else if (s.equals(numbers[4]))
		translated_code += "4";
	    else if (s.equals(numbers[5]))
		translated_code += "5";
	    else if (s.equals(numbers[6]))
		translated_code += "6";
	    else if (s.equals(numbers[7]))
		translated_code += "7";
	    else if (s.equals(numbers[8]))
		translated_code += "8";
	    else if (s.equals(numbers[9]))
		translated_code += "9";
	    else if (s.equals(""))
		continue;
	    else {
		System.out.println("BOOM!!");
		return;
	    }
	}
	
	if ((Integer.parseInt(translated_code) % 6) == 0)
	    System.out.println("BEER!!");
	else
	    System.out.println("BOOM!!");
    }
}
