package DuplicatesPac;

import java.util.*;

public class Duplicates {
    public List<Integer> findDuplicates(List<Integer> integers, int numberOfDuplicates){
        Set<Integer> set = new HashSet<Integer>(integers);
        List<Integer> list_set = new ArrayList<Integer>();
        list_set.addAll(set);
        List<Integer> ret = new ArrayList<Integer>();
        int counter = 0;
        for (int i = 0; i < list_set.size(); i++) {
            for (int j = 0; j < integers.toArray().length; j++)
                if ((list_set.get(i)).equals(integers.get(j))) counter ++;
            if(counter == numberOfDuplicates) ret.add(list_set.get(i));
            counter = 0;
        }
        Collections.sort(ret);
        return ret;
    }
}
