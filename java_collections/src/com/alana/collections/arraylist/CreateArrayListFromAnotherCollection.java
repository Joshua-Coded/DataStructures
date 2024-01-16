package com.alana.collections.arraylist;

import java.util.ArrayList;
import java.util.List;

public class CreateArrayListFromAnotherCollection {
	public static void main(String[] args) {
		
		
		// create arraylist object
		List<Integer> firstFivePrimeNumber = new ArrayList<Integer>();
		
		firstFivePrimeNumber.add(2);
		firstFivePrimeNumber.add(3);
		firstFivePrimeNumber.add(5);
		firstFivePrimeNumber.add(7);
		firstFivePrimeNumber.add(11);
		
		
		List<Integer> firstTenPrimeNumber = new ArrayList<Integer>(firstFivePrimeNumber);
			
		List<Integer> nextFivePrimeNumbers = new ArrayList<Integer>();
		
			nextFivePrimeNumbers.add(13);
			nextFivePrimeNumbers.add(17);
			nextFivePrimeNumbers.add(19);
			nextFivePrimeNumbers.add(23);
			nextFivePrimeNumbers.add(29);
			
			firstTenPrimeNumber.addAll(nextFivePrimeNumbers);
			System.out.println(firstTenPrimeNumber);
	}
}
