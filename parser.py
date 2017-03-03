from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    lines = open(fname).readline()
    lineNum = 0
    while lineNum < len(lines):
    	add = 2
    	cmd = lines[lineNum]
    	if cmd == "line":
    		args = lines[lineNum+1].split(" ")
    		addEdge(points,args[0],args[1],args[2],args[3],args[4],args[5])
    	elif cmd == "ident":
    		add = 1
    		ident(transform)
    	elif cmd == "scale":
    		args = lines[lineNum+1].split(" ")
    		scale = make_scale(args[0],args[1],args[2])
    		matrix_mult(scale, transform)
    	elif cmd == "translate":
    		args = lines[lineNum+1].split(" ")
    		translate = make_translate(args[0],args[1],args[2])
    		matrix_mult(translate, transform)
    	elif cmd == "rotate":
    		args = lines[lineNum+1].split(" ")
    		rotate = []
    		if args[0] == "x":
    			rotate = make_rotX(args[1])
    		if args[0] == "y":
    			rotate = make_rotY(args[1])
    		if args[0] == "z":
    			rotate = make_rotZ(args[1])
    		matrix_mult(rotate, transform)
    	elif cmd == "xrotate":
			args = lines[lineNum+1]
			rotate = make_rotX(args)
    	elif cmd == "yrotate":
			args = lines[lineNum+1]
			rotate = make_rotY(args)
    	elif cmd == "zrotate":
    		args = lines[lineNum+1]
    		rotate = make_rotZ(args)
    	elif cmd == "apply":
    		add = 1
    		matrix_mult(transform, points)
    	elif cmd == "display":
    		add = 1
    		draw_lines( points, screen, color )
			display(screen)
    	elif cmd == "save":
    		args = lines[lineNum+1]
    		draw_lines( matrix, screen, color )
    		save_extension(screen,args)
    	elif cmd == "quit":
    		break
    	lineNum += add