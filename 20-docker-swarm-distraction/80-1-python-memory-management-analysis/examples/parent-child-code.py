import os
 
exitstat = 0
 
 
# Function that is executed after os.fork() that runs in a new process
def child():
    global exitstat
    exitstat += 1
    print('Hello from child', os.getpid(), exitstat)
     
    # End this process using os._exit() and pass a status code back to the shell
    os._exit(exitstat)
 
 
# This is the parent process code
def parent():
    while True:
        # Fork this program into a child process
        newpid = os.fork()
         
        # newpid is 0 if we are in the child process
        if newpid == 0:
            # Call child()
            child()
             
        # otherwise, we are still in the parent process
        else:
            # os.wait() returns the pid and status and status code
            # On unix systems, status code is stored in status and has to
            # be bit-shifted
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q':
                break
 
 
if __name__ == '__main__':
    parent()

