package com.test1;

public class ClassTwo {
	public static int rank(int key, int[] a) {
		//rank ���ǳ��õ������������������ַ����ཻ�ڶ��ַ��Ͳ������򷨻��ǲ�ܶ�
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
