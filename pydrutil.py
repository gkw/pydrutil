import subprocess

def execute(command, param):

  outputj = {}
  output = []
  p = subprocess.Popen([command, param], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in p.stdout.readlines():
    output.append(line.replace('\n','').strip())

  retval = p.wait()
  outputj = {'command': command, 'param':param, 'output': output, 'returnVal': retval}
  return outputj

#test

params = ['atip', 'eject','burn']

for p in params:
  print execute("drutil",p)
