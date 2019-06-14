from __future__ import print_function, division
import numpy as np
from sisl import *
import matplotlib.pyplot as plt

graphene = geom.graphene(1.44)
open('RUN.fdf', 'w').write("""%include STRUCT.fdf
SystemLabel graphene
PAO.BasisSize SZP
MeshCutoff 250. Ry
CDF.Save true
CDF.Compress 9
SaveHS true
SaveRho true
%block kgrid.MonkhorstPack
  61  1 1 0.
   1 61 1 0.
   0  0 1 0.
%endblock
%include band.fdf
""")
graphene.write('STRUCT.fdf')


