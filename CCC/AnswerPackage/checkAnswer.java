
package AnswerPackage;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.nio.file.Path;
import java.nio.file.Paths;

interface AnswerFunction{
	String process(List<String> inputs);
}

public class checkAnswer {

	private static List<String> getLines(String filepath){
		BufferedReader reader;
		List<String> lines = new ArrayList<String>();
		
		try {
			reader = new BufferedReader(new FileReader(filepath));
			String line = reader.readLine();

			while (line != null) {
				// System.out.println(line);
				lines.add(line);
				// read next line
				line = reader.readLine();
				
			}

			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

		// return inputs.toArray(new String[inputs.size()]);
		return lines;
	}

	public static List<String> getInputs(String path)
	{
		String file_dir = System.getProperty("user.dir");
		File inputFile = new File(file_dir,path);
		// System.out.println(inputFile.getPath());
		List<String> inputs = getLines(path);
		inputs.forEach((e) -> {
			// e = e * 10;
			System.out.printf("Input Line: %s\n", e);
		  });

		System.out.println();
		return inputs;
	}

	public static void checkAnswer(String path, String answer)
	{
		String file_dir = System.getProperty("user.dir");
		File inputFile = new File(file_dir,path);
		// System.out.println(inputFile.getPath());
		List<String> outputs = getLines(path);

		if (answer.equals(outputs.get(0)))
		{
			System.out.println("WOOOHOOO!!! ANSWER IS CORRECT!");
		}
		else
		{
			System.out.println("INCORRECT ANSWER!");
		}
		System.out.printf("Correct Answer is: %s, Answer Function Returned is: %s\n\n", outputs.get(0), answer);
		  
	}

	public static void checkAnswers(String question, AnswerFunction answerFunc)
	{
		File questionDir = new File("junior/" + "j1/");
		String contents[] = questionDir.list();
		
		for(int i=0; i<contents.length; i++) {
			// System.out.println(contents[i]);
			if (contents[i].endsWith(".in")){

				File inputFile = new File(questionDir.getPath() + "/" +  contents[i]);
				System.out.println("Input File: " + inputFile.getPath());
				List<String> inputs = getInputs(inputFile.getPath());

				String answer = answerFunc.process(inputs);
				int extensionIndex = contents[i].lastIndexOf('.');
				File outputFile = new File(questionDir.getPath() + "/" + contents[i].substring(0,extensionIndex) + ".out");
				// System.out.println("Output File: " + outputFile.getPath());
				checkAnswer(outputFile.getPath(), answer);
				
			}
		}
		
	}

}