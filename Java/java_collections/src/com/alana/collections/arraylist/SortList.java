package com.alana.collections.arraylist;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class SortList {

	public static void main(String[] args) {
		// create list 
//		List<Integer> list = new ArrayList<Integer>();
//		list.add(10);
//		list.add(30);
//		list.add(90);
//		list.add(70);
//		list.add(20);
//		list.add(40);
//		
//		
//		Collections.sort(list);  // sort in ascending order
//		System.out.println(list);
//		
//		Collections.reverse(list);  // sort in descending order
//		System.out.println(list);

		
		List<Employee> employee = new ArrayList<Employee>();
		employee.add(new Employee(10, "Java", 40, 50000));
		employee.add(new Employee(15, "C", 80, 60000));
		employee.add(new Employee(11, "C#", 90, 80000));
		employee.add(new Employee(12, "Python", 70, 90000));
		employee.add(new Employee(13, "C", 30, 20000));
		
//		
//		Collections.sort(employee, new MySort());
//		System.out.println(employee);
		
		Collections.sort(employee, new Comparator<Employee>() {
			
			@Override
			public int compare(Employee o1, Employee o2) {
				return (int) (o1.getSalary() - o2.getSalary());
			}
		});
		
		// using lambda expression 
		
		Collections.sort(employee, (o1, o2) -> (int) (o1.getSalary() - o2.getSalary()));
				System.out.println(employee);
		
	}
		
}

class MySort implements Comparator<Employee>{
	
	@Override
	public int compare(Employee o1, Employee o2) {
		return (int) (o1.getSalary() - o2.getSalary());
	}
}
