public class Main {
//When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return true if the party with the given values is successful, or false otherwise.
//cigarParty(30, false) → false
//cigarParty(50, false) → true
//cigarParty(70, true) → true
public static void main (String [] args){
boolean Party1 = cigarParty(30,false);
boolean Party2 = cigarParty(50,false);
boolean Party3 = cigarParty(70, true);
System.out.println(Party1);
System.out.println(Party2);
System.out.println(Party3);
}

public static boolean cigarParty(int cigars , boolean isWeekend){
if (isWeekend = true){
  if (cigars > 40){
  return true;
  }
}
else{
  if (cigars >= 40 && cigars <= 60){
  return true;
  }
}

return false;
  }

}

/*When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return true if the party with the given values is successful, or false otherwise.

cigarParty(30, false) → false
cigarParty(50, false) → true
cigarParty(70, true) → true
*/