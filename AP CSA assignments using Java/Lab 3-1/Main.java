class Main {
  public static void main(String[] args) {
  int firstGrade, secondGrade, thirdGrade;
  firstGrade = secondGrade = thirdGrade = 3;
  int Sum;
  double Average;

  Sum = firstGrade + secondGrade + thirdGrade;
  Average = (double) Sum / 3; 

  System.out.print(Average);

  double variance; // to find the variance you find the mean of the numbers, then calculate the difference of the numbers from the calculated mean then square each difference and then find the average once again 


variance = (Math.pow((firstGrade - Average), 2) + Math.pow((secondGrade - Average),2) + Math.pow((thirdGrade - Average), 2)) / 3;

double standardDeviation;

standardDeviation = Math.sqrt(variance);

System.out.println("");
System.out.print(variance);
System.out.println("");
System.out.print(standardDeviation);

  

  }
}

// https://www.mathsisfun.com/data/standard-deviation.html

// 9. Print out the variance and standard deviation.
