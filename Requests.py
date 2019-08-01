#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:30:28 2019

@author: damienrigden

This file will contain examples that may be considered spoilers, but using this will not exclude you from winning the prize.
Using this or not is just personal preference.

"""

encrypt = asleep("Hello world!")
print(encrypt)
{135: [6], 214: [7, 7], 138: [8], 220: [10, 10], 140: [11, 15], 145: [13], 209: [14], 225: [15], 130: [16], 199: [19, 6]}

encrypt2 = asleep("world! Hello")
print(encrypt2)
{164: [3], 206: [4], 126: [5], 196: [6], 191: [7], 123: [8], 115: [9], 105: [10], 178: [11], 203: [12], 120: [13], 200: [14], 199: [4, 402]}

encrypt3 = asleep("🐐")
print(encrypt3)
{128078: [3], 199: [4, 11]}
(haha good one.)

encrypt4 = asleep("a")
print(encrypt4)
{171: [27], 199: [6564, 363]}

encrypt5 = asleep("aa")
print(encrypt5)
{160: [0], 210: [1], 199: [3, 6]}

bonus single character:
encrypt6 = asleep('aaaaaaaa')
print(encrypt6)
{160: [0], 210: [1], 127: [2, 11], 203: [3], 206: [4], 205: [5], 198: [6], 199: [3, 6]}

encrypt7 = asleep("🂡")
print(encrypt7)
{127195: [9], 199: [84, 51]}

encrypt8 = asleep("⟰")
print(encrypt8)
{10285: [6], 199: [19, 18]}

encrypt9 = asleep("")
print(encrypt9)
error

encrypt10 = asleep("\x00")
print(encrypt10)
{65: [0], 199: [3, 2]}

encrypt11 = asleep("\x01")
print(encrypt11)
{66: [0], 199: [3, 2]}

encrypt12 = "\x00\x00"
encrypt13 = "\x00\x01"
encrypt14 = "\x01\x01"
encrypt15 = "A"
encrypt16 = "AB"
encrypt17 = "BA"
