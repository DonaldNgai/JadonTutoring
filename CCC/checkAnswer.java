
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class checkAnswer {

	private static void getLines(String filepath){
		BufferedReader reader;
		
		try {
			reader = new BufferedReader(new FileReader("sample.txt"));
			String line = reader.readLine();

			while (line != null) {
				System.out.println(line);
				// read next line
				line = reader.readLine();
			}

			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		String filename = "j1/j1.01.in";
		System.out.println("Hello World");
		getLines(filename);
	}

	

}