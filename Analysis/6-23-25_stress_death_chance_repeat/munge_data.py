import os.path
import gzip

folder = '../../Data/6-23-25_stress_death_chance_repeat/'

treatment_postfixes = ["DC0", "DC0.05", "DC0.1", "DC0.15", "DC0.2", "DC0.25"]
treatment_potfixes2 = ["MS0.000067", "MS0.00033"]
partners = ["Host"] #I think would only include Host? not Sym
reps = range(1,9)
header = "uid treatment rep update donate partner\n" #I think I need to change the header to something
#mutation size and host death chance updates

outputFileName = "munged_basic.dat"

outFile = open(outputFileName, 'w')
outFile.write(header)

for t in treatment_postfixes:
    for a in treatment_potfixes2:
        for r in reps:
            for p in partners:
                fname = folder + p + "Death_" + t + "Size_" + a + "_SEED" + str(r)+ ".data"
                uid = t + "_" + str(r)
                curFile = open(fname, 'r')
                for line in curFile:
                    if (line[0] != "u"):
                        splitline = line.split(',')
                        outstring1 = "{} {} {} {} {} {}\n".format(uid, t, r, splitline[0], splitline[1], p)
                        outFile.write(outstring1)
                curFile.close()
outFile.close()
