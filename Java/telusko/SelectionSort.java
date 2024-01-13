public class SelectionSort {
    public static void main(String[] args) {
        int nums[] = {3,7,8,3,4,2,9};
        int size = nums.length;
        int temp = 0;
        int minIndex = -1;

        System.out.println("Before Sorting... ");
        for (int num : nums){
            System.out.print(num);
        }

        
        for (int i = 0; i < size -1; i++) {
            minIndex = i;    
            for (int j = i; j< size; j++) {
                if(nums[minIndex] > nums[j]) {
                    minIndex = j;
                }
            }

            // let's do the actual swapping
            temp = nums[minIndex];
            nums[minIndex] = nums[i];
            nums[i] = temp;


            for (int num : nums) {
                System.out.print(num + " ");
            }
            System.out.println();
        }


        System.out.println("After Sorting... ");
        for (int num : nums){
            System.out.print(num);
        }
    }
}