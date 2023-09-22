package AnswerPackage;

public class exampleUsage {
    public static void main(String[] args) {
		// String filename = "junior/j1/j1.01.in";
		// System.out.println("Hello World");
		// getInputs(filename);
		// checkAnswer("junior/j1/j1.01.out", "900");

		AnswerFunction sayHello = (inputs) -> {
            int P = Integer.parseInt(inputs.get(0));
            int C = Integer.parseInt(inputs.get(1));
            System.out.printf("P: %d, C: %d\n", P, C);
			int output = 50*P - 10*C;
            if (P > C)
            {
                output += 500;
            }
			return String.valueOf(output);
		};

		checkAnswer.checkAnswers("j1.01.in", sayHello);
	}
}
