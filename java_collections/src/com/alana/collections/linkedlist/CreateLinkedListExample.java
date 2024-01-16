package com.alana.collections.linkedlist;

import java.util.LinkedList;


// add()
// add(2, element)
// addFirst()
// addLast()
public class CreateLinkedListExample {

	public static void main(String[] args) {
		LinkedList<String> fruits = new LinkedList<String>();
		fruits.add("Banana");
		fruits.add("Mango");
		fruits.add("Apple");
		
		System.out.print(fruits);
		

		// Add an element at the specified position in the linkedlist
		
		fruits.add(2, "Watermelon");
		System.out.println("After adding watermelon => " + fruits);
		
		// Adding Element at the beginning of a linkedlist
		fruits.add(0, "Avicado");
		
		System.out.print("After adding Avocado hoow ou list => " + fruits);
		
		
	}

}
