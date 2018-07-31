import sys
import numpy as np

if len(sys.argv) != 1:
     print "Usage:"
     sys.exit(0)

f=open("asarpy.txt","w+")
print "change helicity False"
print "change rwgt_dir rwgt"
print ""
print ""
f.write("#*******************************************\n")
f.write("#QGC Par     ZV channel     step\n")
f.write("#FS0        [-35.0,35.0]      0.5\n")
f.write("#FS1        [-25.0,25.0]      0.5\n")
f.write("#FT0        [-1.2,1.2]        0.2\n")
f.write("#FS1        [-1.0,1.0]        0.01\n")
f.write("#FT2        [-2.1,2.1]        0.1\n")
f.write("#FM0        [-4.8,4.8]        0.2\n")
f.write("#FM1        [-15.0,15.0]      0.5\n")
f.write("#FM6        [-10.0,10.0]      0.2\n")
f.write("#FM7        [-25.0,25.0]      0.5\n")
f.write("#*******************************************\n\n")
f.write("change helicity False\n")
f.write("change rwgt_dir rwgt\n")
f.write("\n")
f.write("\n")

count=0
for i in np.arange(-35.0,35.5,0.5):
    if i%0.5 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FS0	***************************"
     	print "launch --rwgt_name=FS0_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FS0	***************************\n")
	f.write("launch --rwgt_name=FS0_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")

for i in np.arange(-25.0,25.5,0.5):
    if i%0.5 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FS1	***************************"
     	print "launch --rwgt_name=FS1_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FS1	***************************\n")
	f.write("launch --rwgt_name=FS1_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")

for i in np.arange(-1.2,1.4,0.2):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FT0	***************************"
     	print "launch --rwgt_name=FT0_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FT0	***************************\n")
	f.write("launch --rwgt_name=FT0_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")


for i in np.arange(-1.0,1.0,0.01):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FT1	***************************"
     	print "launch --rwgt_name=FT1_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FT1	***************************\n")
	f.write("launch --rwgt_name=FT1_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")


for i in np.arange(-2.1,2.2,0.1):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FT2	***************************"
     	print "launch --rwgt_name=FT2_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FT2	***************************\n")
	f.write("launch --rwgt_name=FT2_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")

for i in np.arange(-4.8,4.9,0.2):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FM0	***************************"
     	print "launch --rwgt_name=FM0_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FM0	***************************\n")
	f.write("launch --rwgt_name=FM0_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")


for i in np.arange(-15.0,15.5,0.5):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FM1	***************************"
     	print "launch --rwgt_name=FM1_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FM1	***************************\n")
	f.write("launch --rwgt_name=FM1_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")


for i in np.arange(-10.0,10.2,0.2):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FM6	***************************"
     	print "launch --rwgt_name=FM6_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FM6	***************************\n")
	f.write("launch --rwgt_name=FM6_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")

for i in np.arange(-25.0,25.5,0.5):
#    if i%0.2 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FM7	***************************"
     	print "launch --rwgt_name=FM7_"+test
     	print "        set anoinputs 11 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""
	f.write("#************	FM7	***************************\n")
	f.write("launch --rwgt_name=FM7_"+test+"\n")
	f.write("        set anoinputs 11 0.000000e+00\n")
	f.write("        set anoinputs 1 " +str((i*1.0)) + "00000e-12"+"\n")
	f.write(" \n")
	f.write(" \n")


f.close()
