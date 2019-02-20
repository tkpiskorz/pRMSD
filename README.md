# pRMSD
<<<<<<< HEAD
=======
Calculation of permuntative RMSD using bound-and-branch approach
The calcualtion works for now only for single atoms (or center of mass of molecules). 


If you want to consider also periodic images. You have to procide cell_vector variable. You can obtain it for example from MDAnalysis:

```
syst = mdreader.MDreader(internal_argparse=False)
syst.setargs(f="whole.gro", s="whole.gro")
syst.do_parse()

v1 = (syst.trajectory.ts._unitcell)[[0,3,4]]
v2 = (syst.trajectory.ts._unitcell)[[5,1,6]]
v3 = (syst.trajectory.ts._unitcell)[[7,8,2]]

cell_vector = []

# translation of periodic boundary condition, presented here order turned out to be optimal for my system:
for a in [[0, 0, 0], [0, -1, 0], [0, 1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 1, 1], [0, 0, -1], [1, -1, 0], [-1, 1, 0], [0, -1, -1], [-1, 1, 1], [1, 0, 1], [1, -1, -1], [-1, 0, 1], [-1, 0, -1], [1, 1, 0], [1, 0, -1], [1, 1, 1], [-1, -1, 0], [-1, -1, -1], [0, 1, -1], [0, -1, 1], [-1, 1, -1], [1, -1, 1], [-1, -1, 1], [1, 1, -1]]:
    cell_vector.append((a[0]*v1+a[1]*v2+a[2]*v3).astype(np.float32))
```


>>>>>>> 4edda5b471b94b54ba23b67efbf6697416b13b0c
