import java.util.*;
public class Main{
	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		String input=s.nextLine();
		String[] parts = input.split("/");
        int[] da = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            da[i] = Integer.parseInt(parts[i]);
        }
		if (da[0] + da[2] < da[1] || da[1] == 0) {
            System.out.println("hasu");
        } else {
            System.out.println("gosu");
        }
	}
}