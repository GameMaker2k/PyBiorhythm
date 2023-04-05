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

from __future__ import division, absolute_import, print_function;
import sys, imp, os, re, time, datetime, math, cmath, decimal, argparse;
if(__name__ == "__main__"):
 sys.tracebacklimit = 0;
__version_info__ = (1, 2, 8, "RC 1");
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

imageoutlib = "cairosvg";

def check_for_cairo():
 # PIL Support Check
 cairosupport = True;
 try:
  imp.find_module('cairo');
  cairosupport = True;
 except ImportError:
  cairosupport = False
 return cairosupport;

def check_for_pil():
 # PIL Support Check
 pilsupport = True;
 try:
  imp.find_module('PIL');
  pilsupport = True;
 except ImportError:
  try:
   imp.find_module('Image');
   pilsupport = True;
  except ImportError:
   try:
    from PIL import Image, ImageDraw, ImageFont;
    pilsupport = True;
   except ImportError:
    pilsupport = False;
   return pilsupport;
 return pilsupport;

def check_for_pillow():
 pilsupport = check_for_pil();
 if(not pilsupport):
  return pilsupport;
 if(pilsupport):
  from PIL import Image;
  try:
   pil_ver = Image.PILLOW_VERSION;
   pil_is_pillow = True;
  except AttributeError:
   try:
    pil_ver = Image.__version__;
    pil_is_pillow = True;
   except AttributeError:
    pil_is_pillow = False;
   except NameError:
    pil_is_pillow = False;
  except NameError:
   try:
    pil_ver = Image.__version__;
    pil_is_pillow = True;
   except AttributeError:
    pil_is_pillow = False;
   except NameError:
    pil_is_pillow = False;
 return pil_is_pillow;

def check_pil_is_pillow():
 pilsupport = False;
 if(check_for_pil()):
  pilsupport = True;
 pil_is_pillow = False;
 if(pilsupport is True and check_for_pillow() is True):
  pil_is_pillow = True;
 if(pilsupport is False or (pilsupport is True and check_for_pillow() is False)):
  pil_is_pillow = False;
 return pil_is_pillow;

def check_if_pil_is_pillow():
 pil_is_pillow = check_pil_is_pillow();
 return pil_is_pillow;

def check_for_pil_only():
 pilsupport = False;
 if(check_for_pil()):
  pilsupport = True;
 pil_is_not_pillow = False;
 if((pilsupport is True and check_for_pillow() is True) or pilsupport is False):
  pil_is_not_pillow = False;
 if(pilsupport is True and check_for_pillow() is False):
  pil_is_not_pillow = True;
 return pil_is_pillow;

def check_only_for_pil():
 pil_is_not_pillow = check_pil_is_pillow();
 return pil_is_not_pillow;

def check_pil_is_not_pillow():
 pil_is_not_pillow = check_pil_is_pillow();
 return pil_is_not_pillow;

def check_if_pil_is_not_pillow():
 pil_is_not_pillow = check_pil_is_pillow();
 return pil_is_not_pillow;

def get_pil_version(infotype=None):
 pilsupport = check_for_pil();
 if(not pilsupport):
  return pilsupport;
 if(pilsupport):
  from PIL import Image;
  try:
   pillow_ver = Image.PILLOW_VERSION;
   pillow_ver = pillow_ver.split(".");
   pillow_ver = [int(x) for x in pillow_ver];
   pil_is_pillow = True;
  except AttributeError:
   pillow_ver = None;
   pil_is_pillow = False;
  except NameError:
   pillow_ver = None;
   pil_is_pillow = False;
  try:
   pil_ver = Image.VERSION;
   pil_ver = pil_ver.split(".");
   pil_ver = [int(x) for x in pil_ver];
  except AttributeError:
   pil_ver = None;
  except NameError:
   pil_ver = None;
  if(pillow_ver is None and pil_ver is not None):
   pil_info = {'pil_ver': pil_ver, 'pil_is_pillow': pil_is_pillow};
   return pil_info.get(infotype, pil_info);
  if(pillow_ver is not None and pil_ver is not None):
   pil_info = {'pil_ver': pil_ver, 'pillow_ver': pillow_ver, 'pil_is_pillow': pil_is_pillow};
   return pil_info.get(infotype, pil_info);
  if(pillow_ver is not None and pil_ver is None):
   pil_info = {'pillow_ver': pillow_ver, 'pil_is_pillow': pil_is_pillow};
   return pil_info.get(infotype, pil_info);

def get_pillow_version(infotype=None):
 pilsupport = check_for_pil();
 if(not pilsupport):
  return pilsupport;
 if(pilsupport):
  from PIL import Image;
  try:
   pillow_ver = Image.PILLOW_VERSION;
   pillow_ver = pillow_ver.split(".");
   pillow_ver = [int(x) for x in pillow_ver];
   pil_is_pillow = True;
  except AttributeError:
   try:
    pillow_ver = Image.__version__;
    pil_is_pillow = True;
   except AttributeError:
    pillow_ver = None;
    pil_is_pillow = False;
   except NameError:
    pillow_ver = None;
    pil_is_pillow = False;
  except NameError:
   try:
    pillow_ver = Image.__version__;
    pil_is_pillow = True;
   except AttributeError:
    pillow_ver = None;
    pil_is_pillow = False;
   except NameError:
    pillow_ver = None;
    pil_is_pillow = False;
  if(pillow_ver is None):
   return False;
  if(pillow_ver is not None):
   pillow_info = {'pillow_ver': pillow_ver, 'pil_is_pillow': pil_is_pillow};
   return pillow_info.get(infotype, pillow_info);

pilsupport = check_for_pil();
cairosupport = check_for_cairo();
imageoutlib = imageoutlib.lower();
if(not pilsupport and imageoutlib=="pillow"):
 imageoutlib = "cairo";
if(not cairosupport and (imageoutlib=="cairo" or imageoutlib=="cairosvg")):
 imageoutlib = "pillow";
if(not cairosupport and imageoutlib=="cairosvg"):
 imageoutlib = "pillow";
if(imageoutlib!="pillow" and imageoutlib!="cairo" and imageoutlib!="cairosvg"):
 imageoutlib = "pillow";
if(pilsupport and imageoutlib=="pillow"):
 from PIL import Image, ImageDraw, ImageFont;
if(cairosupport and (imageoutlib=="cairo" or imageoutlib=="cairosvg")):
 import cairo;

if(pilsupport and imageoutlib=="pillow"):
 def drawColorLine( ctx, x1, y1, x2, y2, color ):
  ctx.line((x1, y1, x2, y2), fill = color);
  return True; 
 def drawColorRectangle( ctx, x1, y1, x2, y2, color ):
  ctx.rectangle([(x1, y1), (x2, y2)], fill = color);
  return True;
 def drawColorRectangleAlt( ctx, x1, y1, x2, y2, color ):
  ctx.rectangle([(x1, y1), (x2, y2)], outline = color);
  return True;
elif(cairosupport and (imageoutlib=="cairo" or imageoutlib=="cairosvg")):
 def snapCoords( ctx, x, y ):
  (xd, yd) = ctx.user_to_device(x, y);
  return ( round(x) + 0.5, round(y) + 0.5 );
 def drawLine( ctx, x1, y1, x2, y2 ):
  point1 = snapCoords( ctx, x1, y1 );
  point2 = snapCoords( ctx, x2, y2 );
  ctx.move_to( point1[0], point1[1] );
  ctx.line_to( point2[0], point2[1] );
  ctx.set_line_width( 1.0 );
  ctx.stroke();
  return True;
 def drawRectangle( ctx, x1, y1, x2, y2 ):
  point1 = snapCoords( ctx, x1, y1 );
  point2 = snapCoords( ctx, x2, y2 );
  ctx.move_to( point1[0], point1[1] );
  ctx.rectangle( point1[0], point1[1], point2[0], point2[1] )
  ctx.set_line_width( 1.0 );
  ctx.stroke();
  return True;
 def drawColorRectangle( ctx, x1, y1, x2, y2, color ):
  ctx.set_source_rgb(color[0], color[1], color[2]);
  drawRectangle(ctx, x1, y1, x2, y2);
  ctx.close_path();
  return True;
 def drawColorLine( ctx, x1, y1, x2, y2, color ):
  ctx.set_source_rgb(color[0], color[1], color[2]);
  drawLine(ctx, x1, y1, x2, y2);
  ctx.close_path();
  return True;

def CalcRhythm(daysAlive, period, multi = 100):
 return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi) * multi);
def CalcRhythmAlt(daysAlive, period):
 return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi));
def CalcRoundRhythm(daysAlive, period, multi = 100):
 return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi) * multi).quantize(decimal.Decimal(1.0));
def CalcRoundRhythmAlt(daysAlive, period, multi = 100):
 return decimal.Decimal(1 - math.sin((daysAlive % period) / period * 2 * math.pi)).quantize(decimal.Decimal(1.0));
def csv(value):
 return map(str, value.split(","))
parser = argparse.ArgumentParser(conflict_handler = "resolve", add_help = True);
parser.add_argument("birthday", help = "enter your birthday in MM/DD/YYYY format");
parser.add_argument("-c", "--cdate", default = None, help = "enter center date");
parser.add_argument("-b", "--backward", default = 15, help = "number of days to show before center date");
parser.add_argument("-f", "--forward", default = 15, help = "number of days to show affter center date");
parser.add_argument("-x", "--scalex", default = 10, help = "number of pixels per periods");
parser.add_argument("-s", "--show", default = "emotional,physical,intellectual", type=csv, help = "show theses on chart in csv format");
parser.add_argument("-v", "--version", action = "version", version = __version__);
parser.add_argument("-V", "--verbose", action = "store_true", help = "print various debugging information");
parser.add_argument("-T", "--verbosetype", default = "text", help = "debugging information type");
parser.add_argument("-o", "--output", default = None, help = "input name of output image");
parser.add_argument("-d", "--display", action = "store_true", help = "display image");
getargs = parser.parse_args();
if(getargs.verbosetype=="string"):
 getargs.verbosetype = "text";
if(getargs.verbosetype!="text" and getargs.verbosetype!="csv"):
 getargs.verbosetype = "text";
try:
 bdayinfo = time.strptime(getargs.birthday, "%m/%d/%y");
except ValueError:
 bdayinfo = time.strptime(getargs.birthday, "%m/%d/%Y");
numdaysbackward = int(getargs.backward);
numdaysforward = int(getargs.forward);
if(pilsupport and imageoutlib=="pillow"):
 pre_biorhythm = Image.new("RGB", (((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210));
 biorhythm_img = ImageDraw.Draw(pre_biorhythm);
 biorhythm_img.rectangle([(0, 0), (((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210)], fill = (255, 255, 255));
elif(cairosupport and imageoutlib=="cairosvg"):
 pre_biorhythm = cairo.SVGSurface(getargs.output, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210);
 biorhythm_img = cairo.Context (pre_biorhythm);
 biorhythm_img.set_antialias(cairo.ANTIALIAS_NONE);
 biorhythm_img.rectangle(0, 0, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210);
 biorhythm_img.set_source_rgb(255, 255, 255);
 biorhythm_img.fill();
elif(cairosupport and imageoutlib=="cairo"):
 pre_biorhythm = cairo.ImageSurface(cairo.FORMAT_RGB24, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210);
 biorhythm_img = cairo.Context (pre_biorhythm);
 biorhythm_img.set_antialias(cairo.ANTIALIAS_NONE);
 biorhythm_img.rectangle(0, 0, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 210);
 biorhythm_img.set_source_rgb(255, 255, 255);
 biorhythm_img.fill();
drawColorLine(biorhythm_img, 0, 105, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), 105, (0, 0, 0));
drawColorLine(biorhythm_img, ((numdaysbackward + numdaysforward) * int(getargs.scalex)) / 2, 0, ((numdaysbackward + numdaysforward) * int(getargs.scalex)) / 2, 210, (0, 0, 0));
startloop = 0;
endloop = numdaysbackward + numdaysforward;
while(startloop<endloop):
 if(startloop==(numdaysbackward - 1)):
  startloop = startloop + 1;
 drawColorLine(biorhythm_img, (startloop + 1) * int(getargs.scalex), 0, (startloop + 1) * int(getargs.scalex), 5, (0, 0, 0));
 drawColorLine(biorhythm_img, (startloop + 1) * int(getargs.scalex), 205, (startloop + 1) * int(getargs.scalex), 210, (0, 0, 0));
 startloop = startloop + 1;
startloop = 0;
endloop = 19;
while(startloop<endloop):
 if(startloop==6):
  startloop = startloop + 1;
 drawColorLine(biorhythm_img, 0, (startloop + 1) * 15, 5, (startloop + 1) * 15, (0, 0, 0));
 drawColorLine(biorhythm_img, (((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex)) - 5, (startloop + 1) * 15, ((numdaysbackward + numdaysforward) - 1) * int(getargs.scalex), (startloop + 1) * 15, (0, 0, 0));
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
 if(getargs.verbosetype=="csv"):
  biorhythmone = ["number", "date"];
  biorhythmone = biorhythmone + list(getargs.show);
  print(", ".join(biorhythmone));
curyear=str(curdate.year);
curmonth=str(curdate.month);
if(len(curmonth)==1):
 curmonth = "0"+curmonth;
curday=str(curdate.day);
if(len(curmonth)==1):
 curday = "0"+curmonth;
endyear=str(enddate.year);
endmonth=str(enddate.month);
if(len(endmonth)==1):
 endmonth = "0"+endmonth;
endday=str(enddate.day);
if(len(endday)==1):
 endday = "0"+endday;
while(int(curyear+curmonth+curday)<int(endyear+endmonth+endday)):
 birthdays = abs((curdate-birthdate).days);
 if(getargs.verbose==True):
  if(getargs.verbosetype=="text"):
   print("number: "+str(curnum));
 curpos = (curnum-1) * int(getargs.scalex);
 if(getargs.verbose==True):
  if(getargs.verbosetype=="text"):
   print("date: "+str(curdate.month)+"/"+str(curdate.day)+"/"+str(curdate.year));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo = [str(curnum), str(curdate.month)+"/"+str(curdate.day)+"/"+str(curdate.year)];
 emotional = CalcRoundRhythm(birthdays, 28);
 if(curnum==1 and "emotional" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (emotional + 104), curpos, (emotional + 104), (51, 128, 51));
 if(curnum>1 and "emotional" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldemotional + 104), curpos, (emotional + 104), (51, 128, 51));
 if(getargs.verbose==True and "emotional" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("emotional: "+str(emotional));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(emotional));
 oldemotional = emotional;
 physical = CalcRoundRhythm(birthdays, 23);
 if(curnum==1 and "physical" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (physical + 104), curpos, (physical + 104), (153, 51, 51));
 if(curnum>1 and "physical" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldphysical + 104), curpos, (physical + 104), (153, 51, 51));
 if(getargs.verbose==True and "physical" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("physical: "+str(physical));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(physical));
 oldphysical = physical;
 intellectual = CalcRoundRhythm(birthdays, 33);
 if(curnum==1 and "intellectual" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (intellectual + 104), curpos, (intellectual + 104), (51, 51, 170));
 if(curnum>1 and "intellectual" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldintellectual + 104), curpos, (intellectual + 104), (51, 51, 170));
 if(getargs.verbose==True and "intellectual" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("intellectual: "+str(intellectual));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(intellectual));
 oldintellectual = intellectual;
 average = decimal.Decimal((physical + emotional + intellectual) / 3).quantize(decimal.Decimal(1.0));
 if(curnum==1 and "average" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (average + 104), curpos, (average + 104), (0, 0, 0));
 if(curnum>1 and "average" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldaverage + 104), curpos, (average + 104), (0, 0, 0));
 if(getargs.verbose==True and "average" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("average: "+str(average));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(average));
 oldaverage = average;
 spiritual = CalcRoundRhythm(birthdays, 53);
 if(curnum==1 and "spiritual" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (spiritual + 104), curpos, (spiritual + 104), (89, 51, 189));
 if(curnum>1 and "spiritual" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldspiritual + 104), curpos, (spiritual + 104), (89, 51, 189));
 if(getargs.verbose==True and "spiritual" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("spiritual: "+str(spiritual));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(spiritual));
 oldspiritual = spiritual;
 intuition = CalcRoundRhythm(birthdays, 38);
 if(curnum==1 and "intuition" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (intuition + 104), curpos, (intuition + 104), (100, 60, 51));
 if(curnum>1 and "intuition" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldintuition + 104), curpos, (intuition + 104), (100, 60, 51));
 if(getargs.verbose==True and "intuition" in getargs.show):
  print("intuition: "+str(intuition));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(intuition));
 oldintuition = intuition;
 awareness = CalcRoundRhythm(birthdays, 48);
 if(curnum==1 and "awareness" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (awareness + 104), curpos, (awareness + 104), (51, 138, 144));
 if(curnum>1 and "awareness" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldawareness + 104), curpos, (awareness + 104), (51, 138, 144));
 if(getargs.verbose==True and "awareness" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("awareness: "+str(awareness));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(awareness));
 oldawareness = awareness;
 aesthetic = CalcRoundRhythm(birthdays, 43);
 if(curnum==1 and "aesthetic" in getargs.show):
  drawColorLine(biorhythm_img, curpos, (aesthetic + 104), curpos, (aesthetic + 104), (171, 51, 141));
 if(curnum>1 and "aesthetic" in getargs.show):
  drawColorLine(biorhythm_img, oldpos, (oldaesthetic + 104), curpos, (aesthetic + 104), (171, 51, 141));
 if(getargs.verbose==True and "aesthetic" in getargs.show):
  if(getargs.verbosetype=="text"):
   print("aesthetic: "+str(aesthetic));
  if(getargs.verbosetype=="csv"):
   biorhythmtwo.append(str(aesthetic));
 oldaesthetic = aesthetic;
 oldpos = curpos;
 if(getargs.verbose==True):
  if(getargs.verbosetype=="text"):
   print("");
  if(getargs.verbosetype=="csv"):
   print(", ".join(biorhythmtwo));
 curdate = curdate + datetime.timedelta(days = 1);
 curyear=str(curdate.year);
 curmonth=str(curdate.month);
 if(len(curmonth)==1):
  curmonth = "0"+curmonth;
 curday=str(curdate.day);
 if(len(curmonth)==1):
  curday = "0"+curmonth;
 curnum = curnum + 1;
if(getargs.display==True and pilsupport and imageoutlib=="pillow"):
 pre_biorhythm.show();
if(not getargs.output==None):
 if(pilsupport and imageoutlib=="pillow"):
  pre_biorhythm.save(getargs.output);
 elif(cairosupport and imageoutlib=="cairo"):
  pre_biorhythm.write_to_png(getargs.output);
 elif(cairosupport and imageoutlib=="cairosvg"):
  pre_biorhythm.flush();
  pre_biorhythm.finish();
