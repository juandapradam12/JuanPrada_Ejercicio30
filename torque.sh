#!/bin/bash
#PBS -l nodes=1:ppn=1, mem=1gb,walltime=00:05:00
#PBS -M jd.prada11@uniandes.edu.co
#PBS -m abe
#PBS -N JuanPrada_Ejercicio27

# COMPILO CON chmod u+x torque.sh Y EJECUTO CON ./torque.sh 

export OMP_NUM_THREADS=2

gcc advection.c -o advection.x -lm 
./advection.x

gcc -fopenmp advectionOPENMP.c -o advectionOPENMP_c 
./advectionOPENMP_c 

gcc walk.c -o walk.x -lm  
./walk.x

gcc -fopenmp walkOPEN.c -o walkOPEN_c 
./walkOPEN_c


rm *_c
rm *.x 

python plots.py

rm *.dat



