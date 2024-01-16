package com.alana.collections.interfaces;

import java.util.ArrayList;
import java.util.Collection;

public class CollectionDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Collection<String> fruitCollection = new ArrayList<String>();
		fruitCollection.add("banana");
		fruitCollection.add("mango");
		fruitCollection.add("apple");
		
		System.out.println(fruitCollection);
		for(String fruit : fruitCollection)
			System.out.println(fruit);
		
		// to remove item use the remove() method
		fruitCollection.remove("mango");
		for(String fruit : fruitCollection)
			System.out.println(fruit);
		
		
		// check for a particular element
		
		System.out.println(fruitCollection.contains("apple"));
		
		
		// another way of using forEach method
		fruitCollection.forEach((e) -> {
			System.out.println(e);
		});
		
		
		
		
		
		
	}

}
