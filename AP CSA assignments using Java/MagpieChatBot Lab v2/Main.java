class Main {
  public static void main(String[] args) {
       String message = "I love cats! I have a cat named Coco. My cat's very smart!";

      String copy = message; // creates a copy of the original message

     
      int index = message.indexOf("cat"); // takes the index of the first occurance of "cat" from the original message
      while(index >= 0) { // loop that terminates once every occurance of "cat" is found
         copy = copy.substring(0, index) + "dog" + copy.substring(index + 3);
         index = message.indexOf("cat", index+1);
        }
      




        // Write a loop here that replaces every occurrence of "cat"
       // in the message with "dog", using indexOf and substring.


 

       System.out.println(copy);



















  }
}