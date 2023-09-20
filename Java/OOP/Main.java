public class Main {
    public static void main(String[] args) {

        // create a new instance of the student class
        Student student = new Student(12, "joshua alana", 32);

        System.out.println(student.rno);
        System.out.println(student.name);
        System.out.println(student.age);
    }
}

class Student {
    int rno;
    String name;
    float age;

    // constructor parameters
    Student(int rno, String name, float age) {
        this.rno = rno;
        this.name = name;
        this.age = age;
    }
}