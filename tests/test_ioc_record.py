import subprocess
from hamcrest import *
import time

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def test_syntax_error_in_IOC_DB_records():
    time.sleep(7)
    for path in execute(["python","validateDBDir.py","../db/","../dbd/sampleIOC.dbd"]):
        assert_that(path[:8], is_("Checking"))
