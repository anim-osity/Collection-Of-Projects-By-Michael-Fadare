import java.util.Scanner;
import java.util.Random;

public class Main
{
public static void main(String[] args)
{
Scanner scan = new Scanner(System.in);

// Choose a random number from 0-100
int random = (int)(Math.random() * 50 + 1);
int count = 0;


// Ask the user to guess a number from 0 to 100
System.out.print("Enter a number from 0 to 100!: ");

// Get the first guess using scan.nextInt();
int userinput = scan.nextInt();
if (userinput == random){
  System.out.println("You got it!");
}
if(userinput != random){
  if (userinput < random){
    System.out.println("Too low!");
  }
  else if(userinput > random){
    System.out.println("Too high!");
  }
}

// Loop while the guess does not equal the random number,
if (userinput == random){
System.out.print("You got it");
}
else {
  do {
  System.out.print("Enter a number from 0 to 100!: ");
  userinput = scan.nextInt();
  if (userinput == random){
System.out.print("You got it!");
count += 1;
}
  if (userinput < random){
  System.out.println("Too low!");  
  } 
  if (userinput > random && count != 1) {
    System.out.println("Too high!!");
  }




} while (userinput != random);

}



// If the guess is less than the random number, print out "Too low!"
// If the guess is greater than the random number, print out "Too high!"
// Get a new guess (save it into the same variable)

// Print out something like "You got it!"


}
}