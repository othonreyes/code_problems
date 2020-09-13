Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.


Q. I am the PM for a mobile app that helps nature photographers.  Before launch, I need you, the dev, to provide production quality implementation for a core feature API.
Feature API: A user should be able to provide

a) the layout of their surrounding trees,
b) their camera specifications, and

to the app, which will recommend to them, 

the best camera orientation for capturing the maximum number of trees in a single picture.






					N
				 T7	i      					
					i     	T1
					i         
					i     		T2
			T6		i   			
					i  
					X	T3
					   
			                                 
       		T4
T5	  



----------------------------------------------------------------------------
N
				 T7	i       I					
					i      I	T1 T1
					i     I     
					i    I  		T2
			T6		i   I  			
					i  I
					X	T3
					    I
			                                  I
        I		T4
T5	          I
	            I
		----------------------------------------------------------------------------
trees = {30, 52, 110, 260, 300, 320};
//           l         r 
//                112
angle = 60
double recommendOrientation(double[] trees, double angle) {
	double resultAngle = 0.0d;
	int countTrees = Integer.MIN_VALUE;
	
	for (int i = 0; i<trees.length; i++) {
		double maxAngle = trees[i] + angle;
		int count = 0;
		int j = trees[i];
		int k = i;
		while (j< maxAngle ) {
			count += 1;
			j = trees[k++];
}
if (count > countTrees ) {
	countTrees = count;
	resultAngle = trees[i];
}
}
return resultAngle;
}


//------------------------
trip seattle to boston
// Solution using sliding window
Thre problem is about finding the 



?>..I:							



aA)AAaAAaaa	ASDASDFssdf																