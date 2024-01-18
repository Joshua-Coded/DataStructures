package com.alana.collections.set;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class HashSetOverview {

	public static void main(String[] args) {
	//	nullValueDemo();
		duplicateValueDemo();
	//	unorderedDemo();
	
	Set<String> programming = new HashSet<String>();
	programming.add(".Net");
	programming.add("C++");
	programming.add("C#");
	programming.add("Python");
	programming.add("JAVA");
	
		
		//use for loop with iterator to print out values
		for (Iterator<String> iterator = programming.iterator(); iterator.hasNext();) {
			String prog = (String) iterator.next();
			System.out.println(prog);
		}
		
		// use while loop with iterator to print out values of hashset
		Iterator<String> iterator = programming.iterator();
		while(iterator.hasNext()) {
			String prog = (String) iterator.next();
			System.out.println(prog);
			
		}
		
		// for each with lambda expression
		
		programming.forEach((e) -> System.out.println(e));
		
		// for each + lambda + streams + jdk 8
		programming.stream().filter((e) -> ! "JAVA".equals(e))
		.forEach((e) -> System.out.println(e));
	
	}
	
	// set cannot contain duplicate values
	private static void nullValueDemo() {
		Set<String> set = new HashSet<>();
		set.add(null);
		set.add(null);
		System.out.println(set.toString());
	} 
	
	// it cannot contain duplicate elements
	private static void duplicateValueDemo() {
		Set<String> set = new HashSet<>();
		set.add("element1");
		set.add("element1");
		set.add("element2");
		set.add("element2");
		System.out.println(set.toString());
	}
	
	// unordered values
	private static void unorderedDemo() {
		Set<String> set = new HashSet<>();
		set.add("element1");
		set.add("element2");
		set.add("element3");
		set.add("element4");
		set.add("element5");
		set.add("element6");
		System.out.println(set.toString());
	}
	
}
