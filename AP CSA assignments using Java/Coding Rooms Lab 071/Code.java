class Main
{
	public static double[] timesTen(double[] arr)
	{
		for (int i = 0; i < arr.length; i++) {
  
            // accessing each element of array
            double x = arr[i];
            arr[i] = x * 10;
        }

        return arr;
	}
	
	public static void main(String[] args)
	{

    double arr[] = {1.0,2.0,3.0,4.0,5.0};
	timesTen(arr);
	}
}