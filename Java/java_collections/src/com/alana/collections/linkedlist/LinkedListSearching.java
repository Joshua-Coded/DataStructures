package com.alana.collections.linkedlist;

import java.util.Iterator;
import java.util.LinkedList;

public class LinkedListSearching {

	public static void main(String[] args) {
		
		LinkedList<String> programmingLanguage = new LinkedList<String>();
		programmingLanguage.add("C++");
		programmingLanguage.add("RUBY");
		programmingLanguage.add("JAVA");
		programmingLanguage.add("PYTHON");
		programmingLanguage.add("C#");
		programmingLanguage.add("JAVASCRIPT");
		
		
		boolean result = programmingLanguage.contains("C");
		System.out.println(result);
		
		// iterator way of searching element in linkedlist
		Iterator<String> iterator = programmingLanguage.iterator();
		while (iterator.hasNext()) {
			String prog = (String) iterator.next();
			System.out.print(prog);
		}
		
		
		// For Each method of searching 
		
		programmingLanguage.forEach((e) -> {
			System.out.println(e);
		});
		
		// for each advanced method
		
		for (String e : programmingLanguage) {
			System.out.print(e);
		}
		
		// simple for loop
	

	}

}
