public class BinaryRepresentation {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            int value = i;
            StringBuilder binaryRepresentation = new StringBuilder();

            for (int j = 7; j >= 0; j--) {
                int bit = (value & (1 << j)) != 0 ? 1 : 0;
                binaryRepresentation.append(bit);
            }

            System.out.println(i + " in binary: " + binaryRepresentation);
        }
    }
}
