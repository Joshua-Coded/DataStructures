package com.alana.collections.arraylist;

import java.util.ArrayList;
import java.util.List;

public class AccessElementsFromArrayList {
	public static void main(String[] args) {
		
		
		List<String> topProgramming = new ArrayList<String>();
		
		// check if ArrayList is empty or not..
		System.out.println("Is topProgramming ArrayList Empty :  " + topProgramming.isEmpty());
		
		topProgramming.add("C");
		topProgramming.add("JAVA");
		topProgramming.add("PYTHON");
		topProgramming.add("C#");
		topProgramming.add("C++");
		
		
		// check the size of the  ArrayList..
				System.out.println("Here are the top " +  topProgramming.size() + " Programming Language in the world");
		
				
		// retrieve the elements at a given index....
			String bestProgramming = topProgramming.get(1);
			System.out.println(bestProgramming);
			
			
			for (int i = 0; i < topProgramming.size(); i++) {
				System.out.println(topProgramming.get(i));
			}
			
			topProgramming.forEach((e) -> {
				System.out.println(e);
			});
					
	}
}
