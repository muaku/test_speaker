#!/usr/bin/env python
# -✳- coding: utf-8 -✳-

import subprocess
import os
import sys
from time import sleep

if __name__=='__main__':
    commandText = u'/root/AquesTalkPi \"こんにちはケニーさん.今日の笑顔はいいですね.何か良いことありましたか.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
    subprocess.call(commandText, shell=True)
    sleep(1)
    commandText1 = u'/root/AquesTalkPi \"でも今朝は少しお熱があるみたい.体温計ってもらいましょう.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
    subprocess.call(commandText1, shell=True)
    sleep(1)
    commandText2 = u'/root/AquesTalkPi \"今日の心拍は64.呼吸は14です.体の調子は良いでしょう.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
    subprocess.call(commandText2, shell=True)
    sleep(1)
