class Main
{
	public static void main(String[] args)
	{
		int[] a = {1,2,3,4,5};
		System.out.println(sumElements(a)); //should print 15
	}
	public static int sumElements(int[] array)
	{

        int x = 0;
    
    for (int i = 0; i < array.length; i++){
        x += array[i];
    }


    return x;
	}
}