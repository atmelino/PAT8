from datetime import datetime
import time
import traceback

i=5
print i



try:
    print i
    i=i+1
    curdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fh = open("writeFiles/Hello.txt", "a")
    output="%s %8d Hello World again\n" %(curdate,i)
    fh.write(output)
    fh.close 
    #time.sleep(1)
    
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"


