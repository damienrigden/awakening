#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:44:49 2019

@author: damienrigden
"""

from awake import asleep, awake
import random

log = open('Log4.txt', 'w')
errors = []

test = 0
passed = 0
failed = 0

log.write('TEST LOG FILE FOR AWAKENING CRYPTO PROBLEM\n')
log.write('\n')

for a in range(8000):
    testword = ''
    D1 = random.randint(33,126)
    D2 = random.randint(33,126)
    D3 = random.randint(33,126)
    D4 = random.randint(33,126)
    D5 = random.randint(33,126)
    D6 = random.randint(33,126)
    D7 = random.randint(33,126)
    D8 = random.randint(33,126)
    D9 = random.randint(33,126)
    D10 = random.randint(33,126)
    D11 = random.randint(33,126)
    D12 = random.randint(33,126)
    D13 = random.randint(33,126)
    D14 = random.randint(33,126)
    D15 = random.randint(33,126)
    D16 = random.randint(33,126)
    D17 = random.randint(33,126)
    D18 = random.randint(33,126)
    D19 = random.randint(33,126)
    D20 = random.randint(33,126)
    testword = chr(D1) + chr(D2) + chr(D3) + chr(D4) + chr(D5) + chr(D6) + chr(D7) + \
    chr(D8) + chr(D9) + chr(D10) + chr(D11) + chr(D12) + chr(D13) + chr(D14) + chr(D15) + \
    chr(D16) + chr(D17) + chr(D18) + chr(D19) + chr(D20) 
    log.write("Word tested: {}\n".format(testword))
    tosleep = asleep(testword)
    log.write(str(tosleep) + '\n')
    awoken = awake(tosleep)
    if awoken == testword:
        log.write('Test passed!\n')
        passed += 1
    
    else:
        log.write('Test failed!\n')
        message = 'Expected: {}, Returned: {}\n'.format(testword, awoken)
        log.write(message)
        failed += 1
        errors.append(message)
    
    log.write('\n')
    test += 1
                    
log.write('Number of tests: {}\n'.format(test))
log.write('Number passed: {}\n'.format(passed))
log.write('Number failed: {}\n'.format(failed))
log.write('Error Log:\n')
for item in errors:
    log.write(str(item) + '\n')

log.close()