package com.test1;

public class ClassTwo {
	public static int rank(int key, int[] a) {
		//rank 这是常用的搜索方法，但是这种方法相交于二分法和并归排序法还是差很多
		for (int i = 0; i<a.length; i++) 
		{
			if (a[i] == key) return i;
		}
		return -1;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
