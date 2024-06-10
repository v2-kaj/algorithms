package org.example;

import DynamicConnectivity.QuickFindUF;
import DynamicConnectivity.QuickUnionUF;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        QuickFindUF uf = new QuickFindUF(5);
        uf.union(0,1);
        uf.union(0,2);
        uf.union(1,3);
        System.out.println(uf.connected(2,3));
    }
}