import java.util.Arrays;
public class Main {

    public static void main(String[] args)
    {
        int[] T = {2, 32, 3, 53, 34, 2, 432, 4, 2, 0, -1, -324, 0};
        MergeSort sort = new MergeSort(T);
        sort.start();

        try
        {
            sort.join();
        }
        catch(Exception e) {}

        for(int i = 0; i < T.length; i++)
            System.out.print(T[i] +" ");

    }
}