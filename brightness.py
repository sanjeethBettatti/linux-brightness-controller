import subprocess
import optparse
import re
import os

parser=optparse.OptionParser()
parser.add_option("-b","--brightness",dest="b",help="To adjust brightness")
(options,arguments)=parser.parse_args()
current_brightness=subprocess.check_output(["cat", "/sys/class/backlight/amdgpu_bl0/brightness"])
res=re.search(r"\d\d|\d",str(current_brightness))
current_brightness=res.group()
final_brightness=int(options.b)+int(current_brightness)
execute="echo "+ str(final_brightness)+ " > /sys/class/backlight/amdgpu_bl0/brightness"
os.system(execute)

