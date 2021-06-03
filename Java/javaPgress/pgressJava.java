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
	
	public void Q3GradeConvert() {
		HashMap<Character, Float> gpa_hash = new HashMap<Character,Float>();
		gpa_hash.put('A', 4.0F);
		gpa_hash.put('B', 3.0F);
		gpa_hash.put('C', 2.0F);
		gpa_hash.put('D', 1.0F);
		Scanner scanner = new Scanner(System.in);
		System.out.print("What is your grade: ");
		Character gpa = scanner.nextLine().charAt(0);
		System.out.println("Your gpa is " + gpa_hash.get(gpa));
		
		
		
	}
	
	public void Q6TicketPrice() {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter age: ");
		int age = Integer.parseInt(scanner.nextLine());
		System.out.print("Enter day of the week: ");
		byte day = Byte.parseByte(scanner.nextLine());
		float ticketPrice;
		
		if (day == 6 || day == 7) {
			System.out.println("You have to pay $10.00 for the ticket.");
			java.lang.System.exit(0);
		}
		else if (day > 7 || day < 0) {
			throw new IllegalArgumentException("Please input a proper day!");
		}
		else {

		if (age < 16 && age >= 0) {
			ticketPrice = 7.5f;
		}
		
		else if (age >= 16 && age < 65) {
			ticketPrice = 10f;
		}
		
		else if (age >= 65 && age <= 130) {
			ticketPrice = 5.5f;
		}
		
		else {
			throw new IllegalArgumentException("Age cannot be negative!");
		}
		String formattedTicketPrice = String.format("%.2f", ticketPrice);
		System.out.println("You have to pay $" + formattedTicketPrice + " for the ticket.");
		}
		
	}
	
	public void bmi_assess() {
		Scanner scanner = new Scanner(System.in);
		try {
		System.out.print("Enter your weight (kg): ");
		float weight = Float.parseFloat(scanner.nextLine());
		System.out.print("Enter your height (m): ");
		float height = Float.parseFloat(scanner.nextLine());
		float bmi_calc = Math.max(weight/height, 0f);
		
		String bmi_assessment;
		if (bmi_calc >= 27.5) {
			bmi_assessment = "Obese";
		}
		
		else if (bmi_calc < 27.5 && bmi_calc >= 23) {
			bmi_assessment = "Overweight";

		}
		
		else if (bmi_calc < 23 && bmi_calc >= 18.5) {
			bmi_assessment ="Normal";
		}
		
		else {
			bmi_assessment = "Underweight";
		}
		
		String bmi_calc_formatted = String.format("%.2f", bmi_calc);
		System.out.println("Your BMI is " + bmi_calc_formatted + " and you are " + bmi_assessment);
		}
		
		catch (IllegalArgumentException i) {
			System.out.println("Invalid Input! Please try again.");
		}
	}
	
	public void bmi_best() {
		Scanner scanner = new Scanner(System.in);
		try {
		System.out.print("Enter your height: ");
		float height = Float.parseFloat(scanner.nextLine());
		System.out.println("Your ideal height is " + 18.5 * height + " - " + 22.9 * height);
		}
		
		catch (IllegalArgumentException i) {
			System.out.println("Invalid Input! Please try again.");
		}
		
		catch (NullPointerException i) {
			System.out.println("Something is null lmao");
		}
	}
	
	public void sumForLoop() {
		long sum = 0;
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter number: ");
		int num = Integer.parseInt(scanner.nextLine());
		for (;0 < num; num--) {
			sum += num;
		}
		System.out.println(sum);
		
		
	}
	
	public void sumWhileLoop() {
		;
	}
	
	public void wheelOfFortune() {
		
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
		//Questions.Q3GradeConvert();
		//Questions.Q6TicketPrice();
		//Questions.bmi_assess();
		//Questions.bmi_best();
		Questions.sumForLoop();

		

		
		

	}

}
