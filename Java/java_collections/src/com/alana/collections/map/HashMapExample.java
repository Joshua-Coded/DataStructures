package com.alana.collections.map;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapExample {

	public static void main(String[] args) {
		
		// example for mapping integers
		Map<String, Integer> numberMapping = new HashMap<>();
		
		// add key-value to map
		numberMapping.put("one", 1);
		numberMapping.put("two", 2);
		numberMapping.put("three", 3);
		numberMapping.put("four", 4);
		numberMapping.put("five", 5);
		
		System.out.println(numberMapping);
		
		
		// important methods of hashmap
		
		// check if hashmap is empty
		
		System.out.println(numberMapping.isEmpty());
		
		// how to find the size of a hashmap
		
		System.out.println(numberMapping.size());
		
		// how to check if a key exit in a hashmap
		
		if(numberMapping.containsKey("four")) {
			System.out.println("exits");
		}
		else {
			System.out.println("not exit");
		}
		
		// how to check if values exit
		
		if(numberMapping.containsValue(5)) {
			System.out.println("found");
		}
		else {
			System.out.println("not found!");
		}

		// how to get value from hashmap
		
		Integer V1 = numberMapping.get("one");
		System.out.println(V1);
		
		// how to remove keys from hashmap
		
		numberMapping.remove("one");
		System.out.println(numberMapping);
		
		// retrieve only keys from the map
		
		Set<String> keys = numberMapping.keySet();
		System.out.println(keys);
		
		Collection<Integer> values = numberMapping.values();
		System.out.println(values);
		
		// different ways to iterate over hashmap
		
		// for each method
		for(Map.Entry<String, Integer> entry: numberMapping.entrySet()) {
			System.out.println("Key -> " + "" + entry.getKey() + " " +  "Values -> " + entry.getValue());
		}
		
		// the iterator method
		Set<Map.Entry<String, Integer>> entries = numberMapping.entrySet();
		Iterator<Map.Entry<String, Integer>> iterator = entries.iterator();
		
		while(iterator.hasNext()) {
			Map.Entry<String, Integer> entry = iterator.next();
			System.out.println("Key -> " + entry.getKey() + " value " + entry.getValue());
		}
	}

}

