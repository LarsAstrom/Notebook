/**
 * Constructs a Fenwick (Binary Indexed) Tree. It is possible to 
 * update bits in a leaf and to get the sum of all nodes up to i.
 *
 * Time Complexity: O(NlogN) for construction, O(logN) for update 
 *                              and querry, where N is len(arr).
 * Space Complexity: O(N)
 */
import java.io.*;

public class fenwicktree{
    public static int[] fenwicktree(int[] arr){
        int[] ret = new int[arr.length+1];
        for(int i = 0; i < arr.length; i++) 
            updatebit(ret,arr.length,i,arr[i]);
        return ret;
    }

    public static void updatebit(int[] fwtree, int n, int i, int val){
        i++;
        while(i <= n){
            fwtree[i] += val;
            i += i&(-i);
        }
    }

    public static int getsum(int[] fwtree, int i){
        int s = 0;
        i++;
        while(i > 0){
            s += fwtree[i];
            i -= i&(-i);
        }
        return s;
    }
}
