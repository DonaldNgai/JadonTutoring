package AnswerPackage;
import java.util.Scanner;
public class Jadon4 {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in); 
        System.out.print("Enter your electricity usage: ");

        int eUsage = userInput.nextInt();
        double subtotal = 0.0;
        if (eUsage < 0)
        {
            System.out.println("Invalid");   
        }
        else{
            if(eUsage >= 50){
                subtotal += 0.5*50;
                eUsage -= 50;
            }
            else if(eUsage < 50 && eUsage > 0 ){
                subtotal += 0.5*eUsage ;

            }
            
            if(eUsage >= 100 || eUsage > 50 && eUsage < 100){
                subtotal += 1.0*100;
                eUsage -= 100;
            }
            if(eUsage >= 100){
                subtotal += 1.2*100;
                eUsage -= 100;
            }
            if(eUsage >=250){
                subtotal += 2.5*eUsage;
                eUsage -= 250;
            } 
        }
		// AnswerFunction sayHello = (inputs) -> {
        //     int P = Integer.parseInt(inputs.get(0));
        //     int C = Integer.parseInt(inputs.get(1));
        //     System.out.printf("P: %d, C: %d\n", P, C);
		// 	int output = 50*P - 10*C;
        //     if (P > C)
        //     {
        //         output += 500;
        //     }
		// 	return String.valueOf(output);
		// };

		// checkAnswer.checkAnswers("j1.01.in", sayHello);






	}
}
