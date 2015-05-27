# Summary 
Python code, using MDAnalysis, to calculate the radius of gyration of a solute in a MD trajectory. 

# Usage:

```python
./rgyr.py <system name> <pdb/prmtop/psf file> <trajectory file>
```
  Line 39: `nf = open('%s.rgyr.dat' %(system),'w')`; output is written to `%s.rgyr.dat` file.
  
  Frame number, time, and RGYR values are written to output in three columns. You should check that the time values are accurate. If not, either alter this script to obtain the accurate time values or just use frame numbers (the first column). 

# Notes:
MDAnalysis must be installed on your local computer.

Numpy must be installed on your local computer. 

You must alter the first line of the scripts to point towards the python command on the local computer.

