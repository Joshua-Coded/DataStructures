package com.alana.collections.interfaces;

import java.util.ArrayList;
import java.util.List;

public class ListDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<String> list = new ArrayList<String>();
		
		// List allows us to add duplicate elements
//		list.add("Element 1");
//		list.add("Element 1");
//		list.add("Element 2");
//		list.add("Element 2");
//		
//		list.forEach((e) -> {
//			System.out.println(e);
//		});
//		
		// List allows us to have null elements
//		list.add(null);
//		list.add(null);
//		list.add(null);
//		list.add(null);
//		
//		list.forEach((e) -> {
//			System.out.println(e);
//		});
		
		
		
		// insertion order
		
		list.add("Element 1");
		list.add("Element 2");
		list.add("Element 3");
		list.add("Element 4");
		
		System.out.println(list);
		
		// accessing elements from a list
		System.out.println(list.get(0));
		System.out.println(list.get(2));
		
		
	}

}
