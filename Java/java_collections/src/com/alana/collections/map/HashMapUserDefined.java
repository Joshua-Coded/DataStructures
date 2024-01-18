package com.alana.collections.map;

import java.util.HashMap;
import java.util.Map;

public class HashMapUserDefined {

	public static void main(String[] args) {
		
		Map<Integer, Student> student = new HashMap<>();
		student.put(1, new Student("Ramash", "Fadate"));
		student.put(2, new Student("Tony", "Fada"));
		student.put(3, new Student("Ramma", "date"));
		student.put(4, new Student("ola", "adate"));
		
//		System.out.println(student.values());
		
		for(Map.Entry<Integer, Student> entry: student.entrySet()) {
			System.out.println("Key -> " + entry.getKey() + "Students: " + entry.getValue());
		}
		

	}

}
