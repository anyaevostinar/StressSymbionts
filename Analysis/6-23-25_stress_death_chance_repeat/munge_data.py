import os.path
import gzip

folder = '../../Data/6-23-25_stress_death_chance_repeat/'

treatment_postfixes = ["DEATH0", "DEATH0.05", "DEATH0.1", "DEATH0.15", "DEATH0.2", "DEATH0.25"]
treatment_potfixes2 = ["SIZE0.00033", "SIZE6.7e-05"]
partners = ["Host"] #I think would only include Host? not Sym
reps = range(1,9)
header = "mutation size and host death chance updates\n" #I think I need to change the header to something
#mutation size and host death chance updates

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for a in treatment_postfixes:
    for t in treatment_potfixes2:
        for r in reps:
            for p in partners:
                fname = folder + "Tasks_" + t + "_" + a + "_SEED" + str(r)+ ".data"
                uid = t + "_" + str(r)
                curFile = open(fname, 'r')
                for line in curFile:
                    if (line[0] != "u"):
                        splitline = line.split(',')
                        outstring1 = "{} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], p)
                        outFile.write(outstring1)
                curFile.close()
outFile.close()
