package com.test1;

public class ClassOne {
	public static int jCD (int p, int q) {
		// TODO Auto-generated method stub
		/**
		 * 欧几里得算法，求最大公约数
		 * euclidean algorithm，for to deal with the problem that find the greatest common divisor(gCD) 
		 */
		if ( q== 0) return p;
		int r = p % q;
		return jCD(q, r);

	}
	
	public static int findMaxArray(int[] a){
		/**计算数组中最大值
		 * calculation  the arraylist of max int
		 */
		int max = a[0];
		for (int i = 1; i < a.length; i++) {
			if (a[i] > max) max=a[i];
		}
		return max;
	}
	
	public static double findMeanArray(double[] a) {
		/**
		 * 计算数组元素的平均值
		 * findMeanArray
		 */
		double sum = 0.0;
		int N = a.length;
		for (int i = 0 ; i < N ; i ++) {
			sum += a[i];
		}
		return sum/N;
	}
	public static double[] copyArray(double[] a) {
		/**
		 * 复制数组
		 * copyArray
		 */
		int N = a.length;
		double[] b = new double[N];
		for (int i = 0 ; i < N ; i++) {
			b[i] = a[i];
		}
		return b;
	}
	public static double[] reversalArray(double[] a) {
		/**
		 * reversalArray
		 * 颠倒数组中元素的顺序
		 */
		int N = a.length;
		for(int i = 0; i < N/2; i++) {
			double temp = a[i];
			a[i] = a[N-1-i];
			a[N-i-1] = temp;
		}
		return a;
	}
	public static double[][] multiplyMatrix(double a[][], double b[][]){
		/**
		 * 矩阵相乘
		 * multiply matrix
		 */
		int N = a.length;
		double c[][] = new double[N][N];
		for(int i = 0; i < N ; i++) {
			for (int j=0; i<N ; j++) {
				for(int k = 0; k < N ; k++) {
					c[i][j] += a[i][k] * b[k][j];
				}
			}
		}
		return c;
	} 
	public static double[] anotherName (double[] a){
		/**
		 * 起别名
		 * anotherName
		 */
		int N = a.length;
		a[3] = 123456;
		double[] b = a;
		return b;
	}
	public static int abs(int x) {
		/**
		 * absolute value
		 * 求绝对值
		 */
		if(x<0) return -x;
		else return x;
	}
	public static double abs(double x) {
		/**
		 * 计算浮点绝对值
		 */
		if(x<0) return -x;
		else return x;
	}
	public static boolean isPrime(int N) {
		/**
		 * 判断是否是素数
		 */
		if (N < 2) return false;
		for (int i = 2; i*i <= N; i++)
			if(N % i == 0) return false;
		return true;
	}
	public static double sqrt(double c) {
		/**
		 * 牛顿迭代法计算平方根
		 */
		if (c<0) return Double.NaN;
		double err = 1e-15;
		double t = c;
		while(Math.abs(t - c/t) > err * t)
			t = (c/t + t )/2.0;
		return t;
	}
	public static double hypotenuse(double a, double b) {
		/**
		 * 计算直角三角形斜边
		 */
		return Math.sqrt(a*a + b*b);
	}
	public static double H(int N) {
		/**
		 * 计算调和级数
		 */
		double sum = 0.0;
		for(int i = 1; i<=N; i++)
			sum += 1.0/i;
		return sum;
	}
	public static int rank(int key, int[] a) {
		/**
		 * 二分法查找的递归实现
		 */
		return rank (key, a, 0, a.length -1);
	}

	private static int rank(int key, int[] a, int lo, int hi) {
		// TODO Auto-generated method stub
		if(lo > hi) return -1;
		int mid = lo + (hi - lo) / 2;
		if (key <a[mid]) return rank(key, a, lo, mid-1);
		else if (key > a[mid]) return rank(key, a, mid + 1, hi);
		else	return mid;
	}
	

}
