package com.alana.collections.linkedlist;
import java.util.LinkedList;


public class RemoveLinkedListElement {
	public static void main(String[] args) {
		LinkedList<String> fruits = new LinkedList<String>();
		
		fruits.add("Mango");
		fruits.add("Orange");
		fruits.add("Apple");
		
		// remove first element in a linked list
		String element = fruits.removeFirst();
		System.out.println("Elements removed from list " + element);
		System.out.println("Elements " + fruits);
		
		// Remove last elements in a linked list
		fruits.removeLast();
		System.out.println(fruits);
		
		fruits.remove("Orange");
		System.out.println(fruits);
		

	}

}
