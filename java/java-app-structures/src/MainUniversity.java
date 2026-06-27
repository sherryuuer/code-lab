import university.Student;
import university.Course;
import university.Enrollment;

public class MainUniversity {
    public static void main(String[] args) {
        Student student = new Student();
        student.studentId = 101;
        student.name = "Jane Doe";

        Course course = new Course();
        course.courseId = 1;
        course.courseName = "Computer Science";

        Enrollment enrollment = new Enrollment();
        enrollment.student = student;
        enrollment.course = course;

        System.out.println("Student ID: " + enrollment.student.studentId + ", Name: " + enrollment.student.name);
        System.out.println("Course ID: " + enrollment.course.courseId + ", Name: " + enrollment.course.courseName);
    }

}
