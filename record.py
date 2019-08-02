import time

class Log:
    def __init__(self):
        self.start_ts = None
        self.start_tf = None
        self.end_ts = None
        self.end_tf = None
        self.cnt=0
        self.fcnt=0
        
    def timer_start(self):
        self.start_ts = time.time()
        self.start_tf = time.strftime("%m-%d %H:%M:%S", time.localtime())
    
    def timer_end(self):
        self.end_ts = time.time()
        self.end_tf = time.strftime("%m-%d %H:%M:%S", time.localtime())
        

    def conf_save(self, device):
        if device is None:
            return 0
        
        fo = open("serial-port-test-log", "w+")
        fo.write("Serial port name:")
        fo.write('\n')
        fo.write(device)
        fo.write('\n')
        fo.close

    def conf_read(self):
        try:
            fo = open("serial-port-test-log", "r")
        except FileNotFoundError:
            return ''
        fo.readline()
        str = fo.readline().splitlines()
        fo.close
        return str
        
    def file_rep(self):
        fo = open("serial-port-test-log", "a")
        fo.write("---------------------------------\n")
        fo.write(" Succeed count : %d \n" % (self.cnt-self.fcnt))
        fo.write(" Failed count  : %d \n" % self.fcnt)
        fo.write(" Success rate  : %.2f%% \n" % ((self.cnt-self.fcnt)/self.cnt*100))
        fo.write(" Start time    : %s\n" % (self.start_tf))
        fo.write(" End time      : %s\n" % (self.end_tf))
        fo.write(" Execution time: %.2fs \n" % (self.end_ts-self.start_ts))
        fo.write("\n")
        fo.close

