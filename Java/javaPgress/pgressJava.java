package javaPgress;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Arrays;
import java.util.InputMismatchException;

public class pgressJava {
	
	public void salary() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Total Working Hours: ");
		short workingH = Short.parseShort(scanner.nextLine());
		System.out.print("Hourly rate: ");
		float hourly_rate = Short.parseShort(scanner.nextLine());
		System.out.println("Monthly Salary for this month is $ " + hourly_rate * workingH);
	}
	
	public void InfoDisplay() {

		
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter name: ");
		String nameScanner = scanner.nextLine();
		System.out.print("Enter admin number: ");
		String adminScanner = scanner.nextLine();
		System.out.print("Enter age: ");
		byte ageScanner = Byte.parseByte(scanner.nextLine());
		System.out.print("Enter gender (Male / Female): ");
		String genderScanner = scanner.nextLine();
		System.out.print("Enter weight (kg): ");
		float weightScanner = Float.parseFloat(scanner.nextLine());
		System.out.print("Enter height (m): ");
		float heightScanner = Float.parseFloat(scanner.nextLine());
		System.out.println("Hello " + nameScanner);
		System.out.println("Your admin no is " + adminScanner + " and age is " + ageScanner);
		System.out.println("Your gender is " + genderScanner + " and bmi is " + weightScanner/heightScanner);

		
		
	}
	
	public void finalMark() {
		Scanner scanner = new Scanner(System.in);
		float totalScore = 0f;
		for (int i = 1; i <= 3; i++) {
			System.out.print("What is your score for Test " + i + ": ");
			byte scoreScanner = Byte.parseByte(scanner.nextLine());
			System.out.print("What is percentage for Test " + i + ": ");
			byte percentageScanner = Byte.parseByte(scanner.nextLine());
			totalScore += scoreScanner * percentageScanner/100;
		}
		System.out.print("What is your score for Exam: ");
		byte examScanner = Byte.parseByte(scanner.nextLine());
		totalScore += examScanner * 0.5;
		System.out.println("Your final mark is " + totalScore);

	}
	
	public void challenge() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter current price for ABC Bank Corporation (S$):");
		float current_price = Float.parseFloat(scanner.nextLine());
		float prev_com = 2000 * 0.4f * 0.03f;
		float curr_com = 2000 * current_price * 0.02f;
		float total_com = prev_com + curr_com;
		float profit = (current_price * 2000) - (2000 * 0.4f) - total_com;
		System.out.println("You paid total commission of (S$) " + total_com);
		System.out.println("You made a profit of (S$) " + profit);
		
	}
	
	public void temperature() {
		Scanner scanner = new Scanner(System.in);
	try {
		while (true) {
		System.out.print("What degree Celcius do you want to convert to Fahrenheit: ");
		float convert = Float.parseFloat(scanner.nextLine());
		float fahrenheit = convert * (9/5) + 32;
		System.out.println("Fahrenheit: " + fahrenheit);}}
		catch(IllegalArgumentException i) {
			System.out.println("EXIT");
			}
		}
	
	public void timeChallenge () {
		Scanner scanner = new Scanner(System.in);
		System.out.print("How many seconds do you want to convert: ");
		long seconds = Long.parseLong(scanner.nextLine());
		long real_seconds = seconds;
		int hours = (int)(Math.floorDiv(seconds, 3600));
		seconds -= (hours * 3600);
		int minutes = (int)Math.floorDiv(seconds, 60);
		seconds -= (minutes * 60);
		System.out.println(real_seconds + " seconds is " + hours + " hours, " + minutes + " minutes and " + seconds + " seconds.");
	}
	
	public void Optional() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("What is your yearly gross salary: ");
		float monthly = Integer.parseInt(scanner.nextLine()) / 12 * 0.8f - 1500;
		System.out.println("Your take-home pay is $" + monthly);
		
	}
	
	public void Q1MarkCheck() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("What is your mark: ");
		byte mark = Byte.parseByte(scanner.nextLine());
		if (mark >= 50) {
			System.out.println("You have passed!");
		}
		else if (0 <= mark || mark < 50) {
			System.out.println("You have failed!");
		}
		else {
			;
		}
	}
	
	public void gpa() {
		HashMap<Float, String> gpa_hash = new HashMap<Float,String>();
	}
	
	
	
	


	public static void main(String[] args) {
		pgressJava Questions = new pgressJava();
		//Questions.salary();
		//Questions.InfoDisplay();
		//Questions.finalMark();
		//Questions.challenge();
		//Questions.temperature();
		//Questions.timeChallenge();
		//Questions.Optional();
		

		
		

	}

}
