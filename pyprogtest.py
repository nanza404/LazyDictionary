import os


def testid():
    term1 = os.getpgrp()
    term2 = os.getpid()
    term3 = os.getegid()
    term4 = os.geteuid()
    term5 = os.getgid()
    term6 = os.getuid()

    print("term1(getpgrp)  "+str(term1)+"\n"+"term2(getpid)  "+
          str(term2)+"\nterm3(getegid)  "+str(term3)+
          "\nterm4(geteuid)  "+str(term4)+"\nterm5(getgid)  "
          +str(term5)+"\nterm6(getuid)  "+str(term6))


testid()
