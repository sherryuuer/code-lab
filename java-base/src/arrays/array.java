package arrays;

public class array {
    public static void main(String[] args) {
        int value;
        int[] result = new int[3];

        value = 1;

        result[0] = 1;
        result[1] = 2;
        result[3] = 3;

        System.out.println(result[value]);

        // array初始化
        int[] array = new int[] { 1, 2, 3, 4, 5 };

        System.out.println(array[0]);
        System.out.println(array[1]);
        System.out.println(array[2]);
        System.out.println(array[3]);
        System.out.println(array[4]);
        System.out.println(array[5]);

        // 2次元array
        String[][] array2 = new String[][] {
                { "hello", "world" },
                { "hello", "sally" },
        };
        System.out.println(array2[1][1]); // "sally"

        // array practice 1
        int[] age = new int[10];

        age[0] = 14;
        age[1] = 21;
        age[2] = 22;
        age[3] = 19;
        age[4] = 31;
        age[5] = 18;
        age[6] = 20;
        age[7] = 21;
        age[8] = 33;
        age[9] = 18;

        int a = age[1] + age[8];

        System.out.println(a);

        // array practice 2
        String[] name = new String[] { "田中", "山田", "高橋", "木村" };

        System.out.print(name[0] + ",");
        System.out.print(name[1] + ",");
        System.out.print(name[2] + ",");
        System.out.println(name[3]);

        // array practice 3
        int[][] tall = new int[3][4];

        tall[0][0] = 173;
        tall[0][1] = 169;
        tall[0][2] = 176;
        tall[0][3] = 182;

        tall[1][0] = 170;
        tall[1][1] = 171;
        tall[1][2] = 175;
        tall[1][3] = 172;

        tall[2][0] = 180;
        tall[2][1] = 168;
        tall[2][2] = 167;
        tall[2][3] = 173;

        System.out.println(tall[0][0] + "," + tall[0][1] + "," + tall[0][2] + "," + tall[0][3]);
        System.out.println(tall[1][0] + "," + tall[1][1] + "," + tall[1][2] + "," + tall[1][3]);
        System.out.println(tall[2][0] + "," + tall[2][1] + "," + tall[2][2] + "," + tall[2][3]);

    }

}
