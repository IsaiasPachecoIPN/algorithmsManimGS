# algorithmsManimProyect

Project developed to show how Gale-Shapley algorithm works to create stable matchings using Manim.

The "inputdata" file contains all the elements and their preference list.

	xavier;amy,bertha,clare
	yancey;bertha,amy,clare
	zeus;amy,bertha,clare
	*
	amy;zeus,xavier,yancey
	bertha;xavier,yancey,zeus
	clare;xavier,yancey,zeus

>Example of input data file

The "*" is used to separate the groups. Also a "#" can be added to ignore the elemet of the GS algorithm.

	xavier;amy,bertha,clare
	#yancey;bertha,amy,clare
	#zeus;amy,bertha,clare
	*
	amy;zeus,xavier,yancey
	#bertha;xavier,yancey,zeus
	#clare;xavier,yancey,zeus

>Example of the use of "#"

To run the project, manim have to be installed and all its requirement. The run the following code.

	manim -pql main.py CreateScene

##Output

![](https://github.com/IsaiasPachecoIPN/algorithmsManimProyect/blob/main/Result4.gif)
