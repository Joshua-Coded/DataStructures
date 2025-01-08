#include <stdio.h>

// function for inserting

void insertionSort(int A[], int n) {
for (int j = 2; j <= n; j++) {
	int key = A[j];
	int i = j - 1;

// print current element being considered.
printf("\nInserting element a[%d] = %d\n", j, key);

// we need to move elements greater than key one position ahead

while (i > 0 && A[i] > key) {
A[i + 1] = A[i];
i = i - 1;

// let's see the array state during shifting
printf("Shiftting: ");
for (int k = 1; k <= n; k++){
	printf("%d", A[k]);
}
printf("\n");
}

// now after shifting we insert array in the correct position
A[i + 1] = key;

// print array state after insertion
printf("After insertion: ");
for (int k = 1; k <= n; k++){
printf("%d", A[k]);
}
printf("\n");
}
}

int main() {

int A[] = {0,5,2,4,6,1,3};
int n = 6;

printf("Original Array: ");
for (int i = 1; i <= n; i++) {
printf("%d", A[i]);
}
printf("\n");

insertionSort(A, n);

printf("\nFinal Sort array: ");
for (int i = 1; i <= n; i++){
printf("%d ", A[i]);
}
printf("\n");

return 0;
}
