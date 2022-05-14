class Main {




  
  public static void main(String[] args) {
  int[] itemsSold = {48,50,37,62,38,70,55,37,64,60,37,70};

   int biggestindex = 0;int smallestindex = 0;int smallest = 0;int biggest = 0; 
      
   smallest = itemsSold[0];
    
   for (int i = 0; i < itemsSold.length; i++){
     if (itemsSold[i] < smallest){
       smallest = itemsSold[i];
       smallestindex = i;
       }
     
     }
    System.out.println("Smallest number sold is "+ smallest + " and the index in the array is " +smallestindex);

    // gets the biggest number within the itemsSold array
    for (int i = 0; i < itemsSold.length; i++) {
      if (itemsSold[i] > biggest){
        biggest = itemsSold[i];
        biggestindex = i;}
      }

    System.out.println("Biggest number sold is "+ biggest + " and the index in the array is " +biggestindex);

  int sum = 0;

    for (int i = 0; i <itemsSold.length; i++){
      sum += itemsSold[i];
    }


   int average = (sum);
    System.out.print(average);

    

    
  }
}