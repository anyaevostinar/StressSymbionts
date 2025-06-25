import os.path
import gzip

folder = '../../Data/6-23-25_stress_death_chance_repeat/'

treatment_postfixes = ["DEATH0", "DEATH0.05", "DEATH0.1", "DEATH0.15", "DEATH0.2", "DEATH0.25"]
treatment_postfixes2 = ["SIZE0.00033", "SIZE6.7e-05"]
partners = ["Host"] #I think would only include Host? not Sym
tasks = ["NOT", "NAND", "AND", "ORN", "OR", "ANDN", "NOR", "XOR", "EQU"]
reps = range(1,9)
header = "uid treatment replicate updates tasks count organism\n" #I think I need to change the header to something
#mutation size and host death chance updates

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for a in treatment_postfixes:
    for t in treatment_postfixes2:
        for r in reps:
            for p in partners:
                fname = folder + "Tasks_" + t + "_" + a + "_SEED" + str(r)+ ".data"
                uid = t + "_" + str(r)
                curFile = open(fname, 'r')
                for line in curFile:
                    if (line[0] != "u"):
                        splitline = line.strip().split(',')
                        for task_i in range(1, len(splitline), 2):
                            task = tasks[(task_i-1)//2]
                            host_outstring = "{} {} {} {} {} {} {}\n".format(uid, t + a, r, splitline[0], task, splitline[task_i], "Host")
                            outFile.write(host_outstring)
                curFile.close()
outFile.close()
