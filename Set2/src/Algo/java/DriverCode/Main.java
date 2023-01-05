package DriverCode;

import java.util.*;
import DuplicatesPac.Duplicates;

public class Main {
    public static void main(String[] args){
        Duplicates obj = new Duplicates();
        List<Integer> list = Arrays.asList(1, 2, 3);
        System.out.println();
        System.out.println(obj.findDuplicates(list, 5));
    }
}