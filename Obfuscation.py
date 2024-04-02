'''
THIS MODULE NEED RUN IN THE VIRTUAL MACHINE WHICH INVOKE-OBFUSCATION DOWNLOADED!!!
Download Invoke-Obfuscation: https://github.com/danielbohannon/Invoke-Obfuscation
Manually install module into powershell: https://randomnote1.github.io/powershell/manually-install-module-from-the-powershell-gallery/
'''
import os
import subprocess
from subprocess import Popen, PIPE, run
from tqdm import tqdm

def obfuscator(link1):
    obsCMD = "Invoke-Obfuscation -ScriptPath {path1} -Command 'TOKEN, ALL, 1' -Quiet".format(path1=link1)
    cmd = ["powershell"]+[obsCMD]
    result = subprocess.Popen(cmd, stdout=PIPE)
    return result.communicate()[0]
    




#writeFile = ["Invoke-Obfuscation -ScriptPath C:\\Users\\17zf17\\Desktop\\test.txt -Command 'TOKEN, ALL, 1, ENCODING, 1, CLIP' -Quiet"] #,OUT C:\\Users\\17zf17\\Desktop\\Obfuscated.txt


for file in tqdm(list(os.scandir("C:\\Users\\17zf17\\Desktop\\mixed_malicious"))):
    if file.is_file():
        basename = os.path.basename(file)
        filename ="C:\\Users\\17zf17\\Desktop\\mixed_malicious\\" +basename #get the powershell script

        obfuscatedResult = obfuscator(filename) #obfuscate it!

        #write obfuscated context to text.
        outfile = "C:\\Users\\17zf17\\Desktop\\Obfuscated\\{fileName}".format(fileName="obfuscated_"+basename[:-4]+".txt")
        with open(outfile, 'w') as fa:

            try:
                fa.write(obfuscatedResult.decode('latin1', 'ignore'))
            except:
                print(str(basename)+" Is Passed")
                pass

            
            fa.close()
