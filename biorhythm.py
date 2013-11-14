#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2013 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2013 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2013 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: biorhythm.py - Last Update: 11/13/2013 Ver. 1.0.0 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import sys, os, re, time, datetime, math, cmath, decimal, argparse;
from PIL import Image, ImageDraw, ImageFont;
if(__name__ == "__main__"):
 sys.tracebacklimit = 0;
__version_info__ = (1, 0, 0, "RC 1");
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def drawColorLine( ctx, x1, y1, x2, y2, color ):
 ctx.line((x1, y1, x2, y2), fill = color);
def drawColorRectangle( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], fill = color);
#def drawColorText( ctx, size, x, y, text, color ):
# font = ImageFont.truetype(os.path.dirname(__file__)+os.sep+"OCRB.otf", size);
# text = str(text);
# ctx.text((x, y), text, font = font, fill = color);
# del(font);
def drawColorRectangleAlt( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], outline = color);
def CalcRhythm(daysAlive, period):
 return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi) * 100).quantize(decimal.Decimal(1.0))

parser = argparse.ArgumentParser(conflict_handler = "resolve", add_help = True);
parser.add_argument("birthday", help = "enter your birthday in MM/DD/YYYY format");
parser.add_argument("-c", "--cdate", default = None, help = "enter center date");
parser.add_argument("-b", "--backward", default = 15, help = "number of days to show before center date");
parser.add_argument("-f", "--forward", default = 15, help = "number of days to show affter center date");
parser.add_argument("-v", "--version", action = "version", version = __version__);
parser.add_argument("-V", "--verbose", action = "store_true", help = "print various debugging information");
parser.add_argument("-o", "--output", default = None, help = "input name of output image");
parser.add_argument("-d", "--display", action = "store_true", help = "display image");
getargs = parser.parse_args();
try:
 bdayinfo = time.strptime(getargs.birthday, "%m/%d/%y");
except ValueError:
 bdayinfo = time.strptime(getargs.birthday, "%m/%d/%Y");
numdaysbackward = int(getargs.backward);
numdaysforward = int(getargs.forward);
pre_biorhythm = Image.new("RGB", (((numdaysbackward + numdaysforward) - 1) * 10, 202));
biorhythm_img = ImageDraw.Draw(pre_biorhythm);
biorhythm_img.rectangle([(0, 0), (((numdaysbackward + numdaysforward) - 1) * 10, 202)], fill = (255, 255, 255));
drawColorLine(biorhythm_img, 0, 100, ((numdaysbackward + numdaysforward) - 1) * 10, 100, (0, 0, 0));
drawColorLine(biorhythm_img, ((numdaysbackward + numdaysforward) * 10) / 2, 0, ((numdaysbackward + numdaysforward) * 10) / 2, 202, (0, 0, 0));
startloop = 0;
endloop = numdaysbackward + numdaysforward;
while(startloop<endloop):
 if(startloop==(numdaysbackward - 1)):
  startloop = startloop + 1;
 drawColorLine(biorhythm_img, (startloop + 1) * 10, 0, (startloop + 1) * 10, 5, (0, 0, 0));
 drawColorLine(biorhythm_img, (startloop + 1) * 10, 197, (startloop + 1) * 10, 202, (0, 0, 0));
 startloop = startloop + 1;
startloop = 0;
endloop = 19;
while(startloop<endloop):
 if(startloop==9):
  startloop = startloop + 1;
 drawColorLine(biorhythm_img, 0, (startloop + 1) * 10, 5, (startloop + 1) * 10, (0, 0, 0));
 drawColorLine(biorhythm_img, (((numdaysbackward + numdaysforward) - 1) * 10) - 5, (startloop + 1) * 10, ((numdaysbackward + numdaysforward) - 1) * 10, (startloop + 1) * 10, (0, 0, 0));
 startloop = startloop + 1;
if(not getargs.cdate==None):
 try:
  curdayinfo = time.strptime(getargs.cdate, "%m/%d/%y");
 except ValueError:
  curdayinfo = time.strptime(getargs.cdate, "%m/%d/%Y");
 currentdate = datetime.date(curdayinfo[0], curdayinfo[1], curdayinfo[2]);
if(getargs.cdate==None):
 currentdaytime = datetime.datetime.now();
 currentdate = datetime.date(currentdaytime.year, currentdaytime.month, currentdaytime.day);
birthdate = datetime.date(bdayinfo[0], bdayinfo[1], bdayinfo[2]);
startdate = currentdate - datetime.timedelta(days = numdaysbackward);
enddate = currentdate + datetime.timedelta(days = numdaysforward);
curdate = startdate;
curnum = 1;
if(getargs.verbose==True):
 print("birthday: "+str(birthdate.month)+"/"+str(birthdate.day)+"/"+str(birthdate.year));
 print("");
while(int(str(curdate.month)+str(curdate.day))<int(str(enddate.month)+str(enddate.day))):
 birthdays = abs((curdate-birthdate).days);
 if(getargs.verbose==True):
  print("number: "+str(curnum));
 curpos = (curnum-1) * 10;
 if(getargs.verbose==True):
  print("date: "+str(curdate.month)+"/"+str(curdate.day)+"/"+str(curdate.year));
 physical = CalcRhythm(birthdays, 23);
 if(curnum==1):
  drawColorLine(biorhythm_img, curpos, (physical + 100), curpos, (physical + 100), (0, 0, 255));
 if(curnum>1):
  drawColorLine(biorhythm_img, oldpos, (oldphysical + 100), curpos, (physical + 100), (0, 0, 255));
 if(getargs.verbose==True):
  print("physical: "+str(physical));
 oldphysical = physical;
 emotional = CalcRhythm(birthdays, 28);
 if(curnum==1):
  drawColorLine(biorhythm_img, curpos, (emotional + 100), curpos, (emotional + 100), (255, 0, 0));
 if(curnum>1):
  drawColorLine(biorhythm_img, oldpos, (oldemotional + 100), curpos, (emotional + 100), (255, 0, 0));
 if(getargs.verbose==True):
  print("emotional: "+str(emotional));
 oldemotional = emotional;
 intellectual = CalcRhythm(birthdays, 33);
 if(curnum==1):
  drawColorLine(biorhythm_img, curpos, (intellectual + 100), curpos, (intellectual + 100), (0, 255, 0));
 if(curnum>1):
  drawColorLine(biorhythm_img, oldpos, (oldintellectual + 100), curpos, (intellectual + 100), (0, 255, 0));
 if(getargs.verbose==True):
  print("intellectual: "+str(intellectual));
 oldintellectual = intellectual;
 spiritual = CalcRhythm(birthdays, 53);
 if(getargs.verbose==True):
  print("spiritual: "+str(spiritual));
 oldspiritual = spiritual;
 awareness = CalcRhythm(birthdays, 48);
 if(getargs.verbose==True):
  print("awareness: "+str(awareness));
 oldawareness = awareness;
 aesthetic = CalcRhythm(birthdays, 23);
 if(getargs.verbose==True):
  print("aesthetic: "+str(aesthetic));
 oldaesthetic = aesthetic;
 intuition = CalcRhythm(birthdays, 38);
 if(getargs.verbose==True):
  print("intuition: "+str(intuition));
 oldintuition = intuition;
 oldpos = curpos;
 if(getargs.verbose==True):
  print("");
 curdate = curdate + datetime.timedelta(days = 1);
 curnum = curnum + 1;
if(getargs.display==True):
 pre_biorhythm.show();
if(not getargs.output==None):
 pre_biorhythm.save(getargs.output);
