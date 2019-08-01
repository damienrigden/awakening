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


From question 4, here is an example of two different dictionaries that if put into awake() will produce the same string:
dictionary = asleep('Check out my custom dict.')
print(dictionary)
{112: [9, 420], 199: [10, 422, 84, 402], 113: [11], 187: [12], 198: [13], 122: [14, 419], \
 194: [15], 152: [16], 193: [17], 150: [18], 121: [19], 233: [20], 133: [21], 111: [22], \
 238: [23], 223: [24, 418], 234: [25, 423], 196: [26], 227: [30], 58: [33]}

print(customdict)
{171: [117], 205: [118], 172: [119], 193: [120], 257: [121], 128: [122, 215], 253: [123], \
 188: [124], 199: [125, 2313444, 198], 186: [126], 180: [127], 269: [128], 139: [129], \
 117: [130], 274: [131], 259: [132], 270: [133, 219], 202: [134], 206: [135], 118: [137], \
 263: [138], 182: [139], 64: [141]}
print(awake(customdict))
Check out my custom dict.


encrypt12 = asleep("\x00\x00")
print(encrypt12)
{63: [0], 113: [1], 199: [3, 6]}

encrypt13 = asleep("\x00\x01")
print(encrypt13)
{65: [0], 116: [1], 199: [3, 2]}

encrypt14 = asleep("\x01\x01")
print(encrypt14)
{64: [0], 114: [1], 199: [3, 6]}

encrypt15 = asleep("A")
print(encrypt15)
{136: [18], 199: [1299, 171]}

encrypt16 = asleep("AB")
print(encrypt16)
{136: [18], 168: [19], 199: [1299, 171]}

encrypt17 = asleep("BA")
print(encrypt17)
{137: [18], 167: [19], 199: [1299, 171]}


