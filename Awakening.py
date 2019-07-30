#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:22:10 2019

@author: damienrigden
"""

s = 'No conditions are permanent; No conditions are reliable; Nothing is self.'

encrypt = asleep(s)

print(encrypt)
{85: [0, 3374], 168: [1, 3423], 6: [2, 3377, 3392, 3431], 149: [3, 3396], \
 164: [4], 162: [5, 3373], 145: [6], 79: [7, 3381, 3428], 155: [8, 3400], \
 161: [11, 3379], 178: [12], 215: [14, 3408], 216: [16], 223: [18], \
 153: [19, 3407, 3427], 88: [20, 3420], 228: [21], 136: [22], 225: [23, 3434], \
 75: [24], 220: [25], 233: [26], 175: [27], 122: [29], 170: [30, 3411], \
 82: [31], 174: [33], 84: [34], 141: [35], 159: [37], 144: [38], 167: [39], \
 98: [40], 103: [41], 78: [42], 146: [45], 129: [46], 143: [48], 213: [49], \
 157: [50, 3429, 3433], 200: [51], 72: [52], 210: [53], 212: [54], 176: [55], \
 52: [57], 154: [58], 156: [60], 158: [61], 150: [62, 3436], 160: [66, 3435], \
 173: [68], 199: [3, 3366]}

decrypt = awake(encrypt)

print(decrypt)
'No conditions are permanent; No conditions are reliable; Nothing is self.'

print(decode)
{96: [0], 144: [1, 84, 87, 131, 188], 63: [2, 214], 136: [3, 79, 178], \
 191: [4], 210: [5, 46, 95, 100, 142, 192, 193, 202, 207], \
 200: [6, 102, 143, 195], 142: [7, 55, 72, 85, 93, 97, 186, 203], \
 194: [8, 118], 213: [9, 64, 114, 153, 179, 194, 200], 139: [10, 77, 165, 201], \
 219: [11, 39, 121], 218: [12, 136, 151, 173, 205], \
 60: [13, 83, 110, 115, 157, 160, 167, 171, 175], 233: [14], 202: [15, 139], \
 143: [16, 56, 58, 89, 91, 99, 156, 163, 170], 208: [17, 45, 140, 148], \
 217: [18, 35, 196], 147: [20, 145, 168, 181], 151: [21, 149], 209: [22, 185], \
 125: [24, 62, 68, 73, 107, 169], 226: [25, 190], 157: [26, 146], 148: [27], \
 145: [28, 86, 105], 223: [31], 201: [32, 128, 150, 191], 224: [33], \
 129: [34, 60, 74, 101, 122, 124, 154], 205: [35, 52, 65, 183], \
 197: [37, 96, 112, 155], 137: [38, 106, 137, 158, 211], 160: [41], \
 220: [43], 196: [45, 104, 133], 176: [47], 206: [50, 206], \
 207: [51, 109, 125, 129, 152, 184], 134: [53], 212: [54, 94], 232: [55], \
 138: [59, 76, 81, 166, 172], 126: [62], \
 133: [64, 120, 134, 141, 162, 164, 199], 131: [66, 198], 132: [72, 213], \
 72: [74], 170: [76], 222: [82, 108, 130, 174], 214: [87, 119], 216: [95], \
 211: [97, 116, 182, 208], 215: [101, 123], 229: [110], 221: [111], \
 199: [116, 3, 18], 203: [119], 135: [122], 74: [128, 189], 93: [131], \
 149: [143], 146: [145], 195: [160, 209], 227: [161, 180], 153: [171], \
 150: [181, 210], 94: [188], 141: [196]}

decoded = awake(decode)

decoded = ???

print(decode2)
{142: [3, 235], 217: [4, 68, 83, 154, 171, 250, 274, 277], 122: [5], \
 211: [6, 113, 184], 212: [8, 79, 123, 170, 176, 212, 245, 255], 127: [9, 130], \
 134: [10, 121, 146, 214, 276], 198: [11, 210], 219: [12, 127], \
 140: [13, 91, 132, 135], 206: [14, 162, 264, 267], 223: [15], 125: [16, 172], \
 234: [17], 148: [19, 129, 218], 201: [20, 99, 258, 273], \
 209: [21, 101, 119, 199, 263], \
 56: [23, 88, 98, 116, 131, 139, 145, 158, 163, 215, 219, 223, 229, 252, 272], \
 228: [24], 199: [25, 166, 180, 201, 4, 66], 232: [26], 205: [28, 231], \
 220: [29, 100, 209, 266], 135: [31, 147, 213, 256, 270], 196: [32, 168, 191, 261], \
 141: [33, 174, 221, 226, 227, 265], 216: [34, 179, 239], 204: [35, 111, 122, 125], \
 214: [36], 203: [41, 173, 178, 188], 207: [42, 115, 248, 259], 147: [43], \
 139: [44, 137, 236], 162: [45], 138: [46, 120, 133, 143, 262], \
 213: [47, 118, 156, 175, 206, 242], 197: [48, 165, 187], 130: [49], 193: [51], \
 221: [53, 198, 268], 191: [56], 200: [63, 128, 160], 195: [65], 150: [73, 225], \
 137: [75], 77: [77], 97: [79], 65: [80, 155, 197], 133: [81, 205], \
 124: [83, 243], 192: [87, 240], 128: [88], 208: [89, 177, 183, 232, 244, 249], \
 215: [90, 186, 196, 254], 121: [91, 182, 185, 203, 217, 233], 202: [92], \
 218: [96, 200, 253, 260], 194: [98], 226: [100], 231: [103, 211], 132: [106], \
 224: [108], 123: [120, 230], 129: [128, 208], 210: [129, 251, 275], 157: [131], \
 154: [132, 195], 161: [133], 70: [141, 237], 176: [143], 229: [146], \
 143: [155, 220, 247], 149: [161], 126: [163], 145: [167], 222: [173, 238], \
 188: [180], 136: [185], 189: [196], 151: [208], 175: [210], 158: [217]}

decoded2 = awake(decode2)

decoded2 = ???

Just to make sure you really have it, decode this as well.

print(decode3)
{79: [3, 3886], 158: [4, 3909], 77: [5], 147: [6, 3859], 81: [7, 3872, 3905], \
 145: [8], 73: [9], 133: [10, 3875, 3921], 149: [11, 3869, 3887, 3919], 154: [12], \
 67: [13, 3866], 156: [14, 3899], 103: [15], -20: [16, 3896], 206: [17], \
 213: [19, 3862], 159: [20, 3870], 229: [22], 134: [23, 3882, 3888], 234: [24], \
 189: [26], 2: [27], 160: [30], 161: [32], 65: [33], 151: [35], 167: [36], 78: [37], \
 132: [38], 144: [39], 140: [40], 163: [42, 3895, 3903], 93: [43], 85: [44], \
 150: [48, 3918], 199: [49, 4, 3846], 224: [50, 3907], 212: [51], 220: [52], \
 169: [53], 124: [56], 153: [57], 84: [59, 3922], 82: [60], 136: [61], 164: [63], \
 141: [65], 75: [67], 152: [69], 86: [70, 3912], 166: [72], 219: [73], 172: [74], \
 210: [75], 168: [76], 175: [79]}

decoded3 = awake(decode3)

decoded3 = ???
