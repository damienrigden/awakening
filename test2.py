#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:44:49 2019

@author: damienrigden
"""

from awake import asleep, awake
import random

log = open('Log2.txt', 'w')
errors = []

test = 0
passed = 0
failed = 0

log.write('TEST LOG FILE FOR AWAKENING CRYPTO PROBLEM\n')
log.write('\n')

for a in range(7776):
    testword = ''
    first = random.randint(33,126)
    second = random.randint(33,126)
    third = random.randint(33,126)
    fourth = random.randint(33,126)
    fifth = random.randint(33,126)
    testword = chr(first) + chr(second) + chr(third) + chr(fourth) + chr(fifth)
    log.write("Word tested: {}\n".format(testword))
    tosleep = asleep(testword)
    log.write(str(tosleep))
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
    
    log.write('/n')
    test += 1
                    
log.write('Number of tests: {}\n'.format(test))
log.write('Number passed: {}\n'.format(passed))
log.write('Number failed: {}\n'.format(failed))
log.write('Error Log:\n')
for item in errors:
    log.write(str(errors))

log.close()