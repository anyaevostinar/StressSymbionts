import os.path
import gzip

folder = '../../Data/6-30-25_stress_parasite_on/'

seeds = range(1, 30)
treatments_1 = [0.8]
treatments_2 = [0.85, 0.9, 0.95]
header_prefix = "seed,parasite_death_chance,size,"#going to add size but idk

def munge_file(out_file_name, out_file_header, in_file_prefix) :
    out_file = open(out_file_name, 'w')
    out_file.write(out_file_header + "\n")
    for seed in seeds :
        for t1 in treatments_1 :
            for t2 in treatments_2 :
                dc = str(t1) # parasite death chance
                s = str(seed) # seed 
                ms = str(t2) # its size
                in_file_name = in_file_prefix + "PARASITE_DEATH" + dc + "_HOSTDEATH" + ms + "_SEED" + s + ".data"
                line_prefix = s + "," + ms + "," + dc + ","
                try :
                    in_file = open(folder+in_file_name, 'r')
                    print("opened file")
                    next(in_file)
                    for line in in_file :
                        out_file.write(line_prefix + line)
                    in_file.close()
                except :
                    print("could not read", in_file_name)
    out_file.close()



header = header_prefix + "update,count,hosted_syms"
munge_file("org_counts.dat", header, "OrganismCounts")

header = header_prefix + "update,host_task_NOT,sym_task_NOT,host_task_NAND,sym_task_NAND,host_task_AND,sym_task_AND,host_task_ORN,sym_task_ORN,host_task_OR,sym_task_OR,host_task_ANDN,sym_task_ANDN,host_task_NOR,sym_task_NOR,host_task_XOR,sym_task_XOR,host_task_EQU,sym_task_EQU"
munge_file("task_counts.dat", header, "Tasks")
