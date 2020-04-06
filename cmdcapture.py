import subprocess

def myrun(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print (line)
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)
print(myrun("top"))
