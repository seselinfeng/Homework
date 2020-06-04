import os
import shlex
import signal
import subprocess

import pytest


@pytest.fixture(scope='module', autouse=True)
def record():
    """
    录像功能
    :return:
    """
    cmd = shlex.split("scrcpy --record ../record/tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.SIGINT)
