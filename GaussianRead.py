import sys
import os

from subprocess import call
import subprocess


def Gaussian(input_file,out_file):
    msg="Normal termination of Gaussian"
    
    path_to_gaussian ="C:\\G03W" #DEFAULT
    #path_to_gaussian="C:\G98W"
    os.chdir(path_to_gaussian)
    path_to_input="C:\\G03W\\QMCalc2\\input\\"
    path_to_output="C:\\G03W\\QMCalc2\\output\\"
    input_file=path_to_input+input_file
    out_file=path_to_output+out_file
    print(input_file)
    print(out_file)
    #call(["del", out_file], shell=True)
    output=call(["G03.exe",input_file,out_file], shell=True)
    f = open(out_file, "r")
    text=f.read()
    if msg in text:
        print(msg)
    else:
        print("Hubo un error en el cálculo")
    f.flush()
    f.close()
 
    return text

