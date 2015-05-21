#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# ./rgyr.py system_descripter pdb_file traj_file 

# calculate radius of gyration for a solute;  
# create a numpy array of frame #, Time value, Rgyr;
# only working for a single trajectory *** frames and time values btw traj files will be weird ***

# PREAMBLE:

import numpy as np
import MDAnalysis
import sys

system = sys.argv[1]
pdb = sys.argv[2]
traj = sys.argv[3]

# SUBROUTINES:

# MAIN PROGRAM:

u = MDAnalysis.Universe('%s' %(pdb), '%s' %(traj))

group = u.selectAtoms('resid 1:15')		# change the atom selection for your specific system

Frame = []
Time_ns = []
Rgyr = []
for ts in u.trajectory:
	Frame.append(ts.frame)
	Time_ns.append(u.trajectory.time * 0.002)	# units of time is in ns
	Rgyr.append(group.radiusOfGyration())

zipped = zip(Frame, Time_ns, Rgyr)
Rgyr_table = np.array(zipped)

nf = open('%s.rgyr.dat' %(system), 'w')

for row in zipped:
	nf.write ('%10.1f     %10.4f     %10.6f' %(row[0], row[1], row[2]))
	nf.write('\n')

nf.close()

