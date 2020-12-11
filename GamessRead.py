"""

@author: Pedro González Beermann
         Universidad Autónoma de Chiriquí
         Panamá
@email:pedro.gonzalez@unachi.ac.pa
"""
import os

from subprocess import call



def Gamess(filename):
    msg="EXECUTION OF GAMESS TERMINATED NORMALLY"
    
    input_file=filename.split(".inp")[0]
    print(input_file+".inp")
    out_file=input_file+".log"
    print(out_file)
    
    #Delete files from restart directory
    restart ="C:\\Users\\Public\\gamess-64\\restart\\"  #this is my restart folder
    os.chdir(restart)
    #call(["del", "*.dat"], shell=True)
    #call(["del", "*.rst"], shell=True)
    #call(["del", "*.trj"], shell=True)
    call(["del",input_file+ ".*"], shell=True)

    path_to_gamess ="C:\\Users\\Public\\gamess-64\\" #this is my gamess-64 folder
    os.chdir(path_to_gamess)

    call(["del", out_file], shell=True)
    call(["rungms.bat",input_file, "2019.R1.P1.mkl", "1", "0",out_file], shell=True)
    f = open(out_file, "r")
    text=f.read()
    if msg in text:
        print(msg)
    else:
        print("Calculation error...")
    f.flush()
    f.close()
    return text


