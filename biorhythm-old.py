#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2013-2014 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2013-2014 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2013-2014 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: biorhythm.py - Last Update: 07/25/2014 Ver. 1.2.8 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function
import sys
import os
import re
import time
import datetime
import math
import cmath
import decimal
import argparse
from PIL import Image, ImageDraw, ImageFont
if(__name__ == "__main__"):
    sys.tracebacklimit = 0
__version_info__ = (1, 2, 8, "RC 1")
if(__version_info__[3] != None):
    __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(
        __version_info__[2])+" "+str(__version_info__[3])
if(__version_info__[3] == None):
    __version__ = str(
        __version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])


def drawColorLine(ctx, x1, y1, x2, y2, color):
    ctx.line((x1, y1, x2, y2), fill=color)


def drawColorRectangle(ctx, x1, y1, x2, y2, color):
    ctx.rectangle([(x1, y1), (x2, y2)], fill=color)
# def drawColorText( ctx, size, x, y, text, color ):
# font = ImageFont.truetype(os.path.dirname(__file__)+os.sep+"OCRB.otf", size);
# text = str(text);
# ctx.text((x, y), text, font = font, fill = color);
# del(font);


def drawColorRectangleAlt(ctx, x1, y1, x2, y2, color):
    ctx.rectangle([(x1, y1), (x2, y2)], outline=color)


def CalcRhythm(daysAlive, period, multi=100):
    return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi) * multi)


def CalcRhythmAlt(daysAlive, period):
    return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi))


def CalcRoundRhythm(daysAlive, period, multi=100):
    return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi) * multi).quantize(decimal.Decimal(1.0))


def CalcRoundRhythmAlt(daysAlive, period, multi=100):
    return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi)).quantize(decimal.Decimal(1.0))


def csv(value):
    if(sys.version[0] == "2"):
        return map(str, value.split(","))
    if(sys.version[0] >= "3"):
        return list(map(str, value.split(",")))


parser = argparse.ArgumentParser(conflict_handler="resolve", add_help=True)
parser.add_argument(
    "birthday", help="enter your birthday in MM/DD/YYYY format")
parser.add_argument("-c", "--cdate", default=None, help="enter center date")
parser.add_argument("-b", "--backward", default=15,
                    help="number of days to show before center date")
parser.add_argument("-f", "--forward", default=15,
                    help="number of days to show affter center date")
parser.add_argument("-x", "--scalex", default=10,
                    help="number of pixels per periods")
parser.add_argument("-s", "--show", default="emotional,physical,intellectual",
                    type=csv, help="show theses on chart in csv format")
parser.add_argument("-v", "--version", action="version", version=__version__)
parser.add_argument("-V", "--verbose", action="store_true",
                    help="print various debugging information")
parser.add_argument("-T", "--verbosetype", default="text",
                    help="debugging information type")
parser.add_argument("-o", "--output", default=None,
                    help="input name of output image")
parser.add_argument("-d", "--display", action="store_true",
                    help="display image")
getargs = parser.parse_args()
if(getargs.verbosetype == "string"):
    getargs.verbosetype = "text"
if(getargs.verbosetype != "text" and getargs.verbosetype != "csv"):
    getargs.verbosetype = "text"
try:
    bdayinfo = time.strptime(getargs.birthday, "%m/%d/%y")
except ValueError:
    bdayinfo = time.strptime(getargs.birthday, "%m/%d/%Y")
numdaysbackward = int(getargs.backward)
numdaysforward = int(getargs.forward)
pre_biorhythm = Image.new(
    "RGB", (((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210))
biorhythm_img = ImageDraw.Draw(pre_biorhythm)
biorhythm_img.rectangle([(0, 0), (((numdaysbackward + numdaysforward) - 1)
                        * int(getargs.scalex), 210)], fill=(255, 255, 255))
drawColorLine(biorhythm_img, 0, 105, ((numdaysbackward +
              numdaysforward) - 1) * int(getargs.scalex), 105, (0, 0, 0))
drawColorLine(biorhythm_img, ((numdaysbackward + numdaysforward) * int(getargs.scalex)) / 2,
              0, ((numdaysbackward + numdaysforward) * int(getargs.scalex)) / 2, 210, (0, 0, 0))
startloop = 0
endloop = numdaysbackward + numdaysforward
while(startloop < endloop):
    if(startloop == (numdaysbackward - 1)):
        startloop = startloop + 1
    drawColorLine(biorhythm_img, (startloop + 1) * int(getargs.scalex),
                  0, (startloop + 1) * int(getargs.scalex), 5, (0, 0, 0))
    drawColorLine(biorhythm_img, (startloop + 1) * int(getargs.scalex),
                  205, (startloop + 1) * int(getargs.scalex), 210, (0, 0, 0))
    startloop = startloop + 1
startloop = 0
endloop = 19
while(startloop < endloop):
    if(startloop == 6):
        startloop = startloop + 1
    drawColorLine(biorhythm_img, 0, (startloop + 1) *
                  15, 5, (startloop + 1) * 15, (0, 0, 0))
    drawColorLine(biorhythm_img, (((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex)) - 5, (startloop + 1)
                  * 15, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), (startloop + 1) * 15, (0, 0, 0))
    startloop = startloop + 1
if(not getargs.cdate == None):
    try:
        curdayinfo = time.strptime(getargs.cdate, "%m/%d/%y")
    except ValueError:
        curdayinfo = time.strptime(getargs.cdate, "%m/%d/%Y")
    currentdate = datetime.date(curdayinfo[0], curdayinfo[1], curdayinfo[2])
if(getargs.cdate == None):
    currentdaytime = datetime.datetime.now()
    currentdate = datetime.date(
        currentdaytime.year, currentdaytime.month, currentdaytime.day)
birthdate = datetime.date(bdayinfo[0], bdayinfo[1], bdayinfo[2])
startdate = currentdate - datetime.timedelta(days=numdaysbackward)
enddate = currentdate + datetime.timedelta(days=numdaysforward)
curdate = startdate
curnum = 1
if(getargs.verbose == True):
    if(getargs.verbosetype == "csv"):
        biorhythmone = ["number", "date"]
        biorhythmone = biorhythmone + list(getargs.show)
        print(", ".join(biorhythmone))
curyear = str(curdate.year)
curmonth = str(curdate.month)
if(len(curmonth) == 1):
    curmonth = "0"+curmonth
curday = str(curdate.day)
if(len(curmonth) == 1):
    curday = "0"+curmonth
endyear = str(enddate.year)
endmonth = str(enddate.month)
if(len(endmonth) == 1):
    endmonth = "0"+endmonth
endday = str(enddate.day)
if(len(endday) == 1):
    endday = "0"+endday
while(int(curyear+curmonth+curday) < int(endyear+endmonth+endday)):
    birthdays = abs((curdate-birthdate).days)
    if(getargs.verbose == True):
        if(getargs.verbosetype == "text"):
            print("number: "+str(curnum))
    curpos = (curnum-1) * int(getargs.scalex)
    if(getargs.verbose == True):
        if(getargs.verbosetype == "text"):
            print("date: "+str(curdate.month)+"/" +
                  str(curdate.day)+"/"+str(curdate.year))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo = [str(curnum), str(curdate.month) +
                            "/"+str(curdate.day)+"/"+str(curdate.year)]
    emotional = CalcRoundRhythm(birthdays, 28)
    if(curnum == 1 and "emotional" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (emotional + 104),
                      curpos, (emotional + 104), (51, 128, 51))
    if(curnum > 1 and "emotional" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldemotional + 104),
                      curpos, (emotional + 104), (51, 128, 51))
    if(getargs.verbose == True and "emotional" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("emotional: "+str(emotional))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(emotional))
    oldemotional = emotional
    physical = CalcRoundRhythm(birthdays, 23)
    if(curnum == 1 and "physical" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (physical + 104),
                      curpos, (physical + 104), (153, 51, 51))
    if(curnum > 1 and "physical" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldphysical + 104),
                      curpos, (physical + 104), (153, 51, 51))
    if(getargs.verbose == True and "physical" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("physical: "+str(physical))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(physical))
    oldphysical = physical
    intellectual = CalcRoundRhythm(birthdays, 33)
    if(curnum == 1 and "intellectual" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (intellectual + 104),
                      curpos, (intellectual + 104), (51, 51, 170))
    if(curnum > 1 and "intellectual" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldintellectual + 104),
                      curpos, (intellectual + 104), (51, 51, 170))
    if(getargs.verbose == True and "intellectual" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("intellectual: "+str(intellectual))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(intellectual))
    oldintellectual = intellectual
    average = decimal.Decimal(
        (physical + emotional + intellectual) / 3).quantize(decimal.Decimal(1.0))
    if(curnum == 1 and "average" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (average + 104),
                      curpos, (average + 104), (0, 0, 0))
    if(curnum > 1 and "average" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldaverage + 104),
                      curpos, (average + 104), (0, 0, 0))
    if(getargs.verbose == True and "average" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("average: "+str(average))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(average))
    oldaverage = average
    spiritual = CalcRoundRhythm(birthdays, 53)
    if(curnum == 1 and "spiritual" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (spiritual + 104),
                      curpos, (spiritual + 104), (89, 51, 189))
    if(curnum > 1 and "spiritual" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldspiritual + 104),
                      curpos, (spiritual + 104), (89, 51, 189))
    if(getargs.verbose == True and "spiritual" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("spiritual: "+str(spiritual))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(spiritual))
    oldspiritual = spiritual
    intuition = CalcRoundRhythm(birthdays, 38)
    if(curnum == 1 and "intuition" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (intuition + 104),
                      curpos, (intuition + 104), (100, 60, 51))
    if(curnum > 1 and "intuition" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldintuition + 104),
                      curpos, (intuition + 104), (100, 60, 51))
    if(getargs.verbose == True and "intuition" in getargs.show):
        print("intuition: "+str(intuition))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(intuition))
    oldintuition = intuition
    awareness = CalcRoundRhythm(birthdays, 48)
    if(curnum == 1 and "awareness" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (awareness + 104),
                      curpos, (awareness + 104), (51, 138, 144))
    if(curnum > 1 and "awareness" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldawareness + 104),
                      curpos, (awareness + 104), (51, 138, 144))
    if(getargs.verbose == True and "awareness" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("awareness: "+str(awareness))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(awareness))
    oldawareness = awareness
    aesthetic = CalcRoundRhythm(birthdays, 43)
    if(curnum == 1 and "aesthetic" in getargs.show):
        drawColorLine(biorhythm_img, curpos, (aesthetic + 104),
                      curpos, (aesthetic + 104), (171, 51, 141))
    if(curnum > 1 and "aesthetic" in getargs.show):
        drawColorLine(biorhythm_img, oldpos, (oldaesthetic + 104),
                      curpos, (aesthetic + 104), (171, 51, 141))
    if(getargs.verbose == True and "aesthetic" in getargs.show):
        if(getargs.verbosetype == "text"):
            print("aesthetic: "+str(aesthetic))
        if(getargs.verbosetype == "csv"):
            biorhythmtwo.append(str(aesthetic))
    oldaesthetic = aesthetic
    oldpos = curpos
    if(getargs.verbose == True):
        if(getargs.verbosetype == "text"):
            print("")
        if(getargs.verbosetype == "csv"):
            print(", ".join(biorhythmtwo))
    curdate = curdate + datetime.timedelta(days=1)
    curyear = str(curdate.year)
    curmonth = str(curdate.month)
    if(len(curmonth) == 1):
        curmonth = "0"+curmonth
    curday = str(curdate.day)
    if(len(curmonth) == 1):
        curday = "0"+curmonth
    curnum = curnum + 1
if(getargs.display == True):
    pre_biorhythm.show()
if(not getargs.output == None):
    pre_biorhythm.save(getargs.output)
