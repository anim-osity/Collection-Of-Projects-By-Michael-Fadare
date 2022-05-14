class Main {
  public static void main(String[] args) {
   String[] words = {"ten", "fading", "post", "card", "thunder", "hinge", "trailing", "batting"};

  for(int i = 0; i < words.length; i++){
  String test = words[i];
  if (test.endsWith("ing")){
    System.out.println(test);
  }

  }

    
  }
}