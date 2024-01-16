package com.alana.collections.linkedlist;

import java.util.LinkedList;

public class RetriveLinkedListElements {

	public static void main(String[] args) {
		LinkedList<String> fruits = new LinkedList<String>();
		fruits.add("Mango");
		fruits.add("Banana");
		fruits.add("Apple");
		fruits.add("orange");
		
		
		// Getting first element in the linkedlist using getFirst()
		
		String firstElement = fruits.getFirst();
		System.out.println(firstElement);
	
		// getting the last element in a linkedlsit
		String lastElement = fruits.getLast();
		System.out.println(lastElement);
		
		String elements = fruits.get(2);
		System.out.print(elements);
		
		// iterate over a list
		for (String e : fruits) {
			System.out.println(e);
		}
		
		
	}

}
