 import java.util.Random;

class Main {
  public static void main(String[] args) {
  int LargestNumber = 0; // for finding the largest number within     within each array 
    
  int StoredNumbers[]; // intitalizes the array that will store the   randomly generated numbers 
    
  StoredNumbers = new int[3]; // defines the array that will store    the randomly generated numbers to the length of 2, meaning that     it will have spaces total for elements
    
  int LargestNumberFound[]; // defines the array used to find the     largest number within the largest numbers 
    
  LargestNumberFound = new int[11];  // initializes the array with    a length of 11, should be 10 but I was lazy and just skipped over   the first element in the array later one 
    
  int total = 0; // defines and initalizes the variable that will     be used to store the total of the maxmiums
    
  for (int i = 1; i < 11; i++){ // does the loop 10 times total
    
  LargestNumber = 0; // sets the largest number back to 0 for each    iteration to prevent the largest number staying the same            throughout the entire loop

  for (int a = 0; a < StoredNumbers.length; a++){ // does this loop   3 times to generate the 3 numbers
  int random = (int)Math.floor(Math.random()*(50-1+1)+1); //          generates a random number between 1 and 50
  StoredNumbers[a] = random; // stores the random number in the       storednumbers array
  }
  for (int b = 0; b <= 2; b++){ // within the storedNumbers array,    finds the biggest number 
  if (StoredNumbers[b] > LargestNumber){
  LargestNumber = StoredNumbers[b];
  LargestNumberFound[i] = LargestNumber;
    }
  }

  // prints out the 3 randomly generated numbers along with the       largest number of the 3 
  System.out.println(i + " The maxmium number of ("+                  StoredNumbers[0] + "," + StoredNumbers[1] + "," + StoredNumbers[2]  + ") is " + LargestNumber);
  System.out.println(" ");

  } // end of for loop

  // prints out all the elements of the largestNumberFound array,     im pretty sure that it skips over the 1st element 
  System.out.print("The array of maxmiums is [");
  for (int n = 1; n < LargestNumberFound.length; n++){
  total+= LargestNumberFound[n];
  System.out.print(LargestNumberFound[n] + ", ");
  }
  System.out.print("]");
  System.out.println(" "); 
  System.out.println(" ");
  // prints out the total of the maximums
  System.out.println("The total of the maxmiums is " + total);
    
    }
  }

    
  
    
    
  
