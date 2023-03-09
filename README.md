Original source : https://github.com/meetU-MasterStudents/2022--2023-SU-Team3 <br>

# 2022-2023-Sorbonne University-Team SAJAS <br>

Members : Stéphane Wang, Alix Bonard, Junwoo Park, Assane Fall, Samuel Lalam<br>

<br>
<h3>Requirement</h3>
1. openbabel<br>
2. Java version 8 to 18<br>
3. Python 3.10 if GLIBC_2.35 err <br><br>

<h3>Purpose</h3> 
Constructing the pipeline of 
<br>
1. pocket detection in a protein
<br>
2. protein-ligand docking simulation
<br>
3. protein-ligand interaction scoring
<br>
<br>
<br>

![](https://github.com/JunwooParkSaribu/PLI/blob/main/img/pipeline_flowchart.png)

<br>
<h3>Tutorial</h3>
Installation of openbabel : In terminal, install openbabel<br>
Example(Mac) : brew install open-babel <br>
Example(Linux) : sudo apt-get install openbabel <br>
Parameter setting : params.txt <br>
Pipleline start(Mac) : ./PipeLine_mac <br>
Pipleline start(Linux) : ./PipeLine_linux <br>


<br>
<h3>Current versions</h3>
Python : 3.10 <br>
Scoring : convex-pl 0.3 <br>
Docking : autodock_vina_1_1_2_64bit <br>
Pocket detection : p2rank 2.4.1 <br>
Ligand : rdkit 2022.9.3 <br>
NMA : NOLB <br>

<br>
<h3>Links</h3>
NOLB : https://team.inria.fr/nano-d/software/nolb-normal-modes/ <br>
NMA : https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2279292/ <br>
Amber : https://ambermd.org/ <br>
Rdkit : https://www.rdkit.org/ <br>
MMFF94 : https://doi.org/10.1002/(SICI)1096-987X(199604)17:5/6<490::AID-JCC1>3.0.CO;2-P <br>
p2rank : https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0285-8 <br>
Autodock Vina : https://vina.scripps.edu/ <br>
Convex-PL : https://team.inria.fr/nano-d/software/convex-pl/ <br>
<br>
<br>


![](https://github.com/JunwooParkSaribu/PLI/blob/main/img/red_withligand.gif)

