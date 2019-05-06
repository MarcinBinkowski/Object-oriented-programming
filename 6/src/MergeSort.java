import java.util.Arrays;

public class MergeSort extends Thread {

    public  int[] array;

    public MergeSort(int[] a)
    {
        array = a;
    }

    private int[] merge(int[] l, int[] r) {


        int size = l.length + r.length;
        int[] mergedArray = new int[size];
        int first = 0;
        int sec = 0;
        int index = 0;
        while (index < size) {
            if ((first < l.length) && (sec < r.length)) {
                if (l[first] < r[sec])
                    mergedArray[index++] = l[first++];

                else
                    mergedArray[index++] = r[sec++];
            } else {
                if (first >= l.length) {
                    while (sec < r.length)
                        mergedArray[index++] = r[sec++];
                }
                if (sec >= r.length) {
                    while (first < l.length)
                        mergedArray[index++] = l[first++];
                }
            }
        }
        return me
    }

    private void mergeSort()
    {
        if (array.length > 1) {
            int q = array.length/2;

            int[] leftArray = Arrays.copyOfRange(array, 0, q);
            int[] rightArray = Arrays.copyOfRange(array, q, array.length);

            MergeSort s1 = new MergeSort(leftArray);
            MergeSort s2 = new MergeSort(rightArray);
            s1.start();
            s2.start();
            try
            {
                s1.join();
                s2.join();
            }
            catch (Exception e) {}
            merge(leftArray,rightArray);
        }
    }

    public void run()
    {
        mergeSort();
    }

}








/*
public class MergeSort extends Thread{

    private int[] array;
    private int start, middle, end;

    public MergeSort(int[] newArray, int newStart, int newEnd){
        array = newArray;
        start = newStart;
        end = newEnd;
        middle = (start + end)/2;

    }
    private void merge(int[] temp)
    {
        int tempi = 0;

        while (start < middle && middle < end) {
            if (array[start] < array[middle])
                temp[tempi++] = array[start++];
            else
                temp[tempi++] = array[middle++];
        }

        while (start <  end / 2) {
            temp[tempi++] = array[middle++];
        }

        while (middle < end) {
            temp[tempi++] = array[middle++];
        }

        System.arraycopy(array, start, temp, 0, end - start);
    }
    private void insertionSort()
    {
        for (int i = start; i < end; i++)
        {
            int j, v = array[i];

            for (j = i - 1; j >= 0; j--) {
                if (array[j] <= v)
                    break;
                array[j + 1] = array[j];
            }

            array[j + 1] = v;
        }
    }
    public void run() {

        if ((end - start) <1) {
            insertionSort();
            return;
        }
        int[] temp = new int[end];
        MergeSort sort1 = new MergeSort(array, start, start + ((end-start)/2));
        MergeSort sort2 = new MergeSort(array, start + ((end-start)/2), end);

        sort1.start();
        sort2.start();
        try {
            sort1.join();
            sort2.join();
        }
        catch (Exception e) {}

        System.out.println( temp[0]);
        merge(temp);
        }

}
*/











/*public class MergeSort extends Thread
{
    private int[] tab;
    private int start, end;
    public MergeSort(int[] x, int a, int b){
        tab = x;
        start = a;
        end = b;
    }

    private void merge(int[] pomoc,int p, int s, int k){

        int l1,l2,l3,l;
        l1 = p;
        l2 = s + 1;
        l3 = k;
        l = 0;
        while ((l1 <= s)&&(l2 <= k)){

            if (tab[l2] < tab[l1]){
                pomoc[l] = tab[l2];
                l2 = l2 + 1;
                l = l + 1;
            }
            else{
                pomoc[l] = tab[l1];
                l1 = l1 + 1;
                l = l + 1;
            }
        }
        if (l1 <= s)
            while(l1 <= s){


                pomoc[l] = tab[l1];
                l1 = l1 + 1;
                l = l + 1;
            }
        else{
            while (l2 <= l3){
                pomoc[l] = tab[l2];
                l2 = l2 + 1;
                l = l + 1;

            }

        }
        l1 = 0;
        while (p + l1 <= k){
            tab[p+l1] = pomoc [l1];
            l1 = l1 + 1;
        }



    }
    private void dwa(){

        int j;

        if (end - start == 1 ){
            if (tab[start] > tab[end] ) {
                j = tab[end];
                tab[end] = tab[start];
                tab[start] = j;
            }

        }
    }
    public void run() {
        if (end - start < 2){
            dwa();
        }
        else{
            int[] pom = new int[end + 1];
            int mid = (end + start) /2;

            MergeSort left = new MergeSort(tab,start,mid);
            MergeSort right = new MergeSort(tab,mid + 1,end);

            left.start();
            right.start();
            try{
                left.join();
                right.join();
            }
            catch (Exception e) {}
            merge(pom, start, mid, end);
        }


    }
}
*/