# py amazfit tool for GTS2
An python port of valeronm's amazfitbiptools(v.1.0.3.1) with some hacks for verge lite/gtr.

Added support of GTR2 and GTS2 by bigdigital (GTS2 Mini is in progress)

All credit goes to Валерий Миронов(https://bitbucket.org/valeronm/amazfitbiptools/src/master/)

## what is...
* can pack/unpack .bin file for amazfit verge lite/gtr(original watchfaces)

## what isn't...
* 100% compatibility with amazfit_bip_tool
* 100% compatibility with .json structures of bip

## requirements
* python3(tested on 3.7.4)
* pillow(tested on 6.1.0)

## usage
* for verge lite
  * see scripts folder
    * to unpack
      * python main.py WATCH_FACE_FILE.bin
    * to pack
      * python main.py WATCH_FACE_FILE.json
    * to convert from extracted GTR watchface(experimental BIP support also)
      * python convert.py EXTRACTED_WATCH_FACE_FOLDER
  * for windows users(experimental) : USE AT YOUR OWN RISK
    * copy & unzip amazfit_verge_lite_tools_WIN32.zip from release/win32
      * to pack
        * drag & drop WATCH_FACE_FILE.json into main/main.exe
      * to unpack
        * drag & drop WATCH_FACE_FILE.bin into main/main.exe
      * to convert from extracted GTR watchface(experimental BIP support also)
        * drag & drop EXTRACTED_WATCH_FACE_FOLDER into convert/convert.exe
* for GTR (support 47 and 42 version)
  * to unpack 47mm version
    * python main.py --gtr 47 --file WATCH_FACE_FILE.bin
  * to pack 47mm version
    * python main.py --gtr 47 --file WATCH_FACE_FILE.json
  * for windows users(experimental) : USE AT YOUR OWN RISK
    * copy & unzip amazfit_gtr_tools_WIN32.7z from release/win32
      * to pack
        * drag & drop WATCH_FACE_FILE.json into main_gtr/main.exe
      * to unpack
        * drag & drop WATCH_FACE_FILE.bin into main_gtr/main.exe

* for GTR2
  * to unpack 
    * python main.py --gtr2 47 --file WATCH_FACE_FILE.bin
  * to pack 
    * python main.py --gtr2 47 --file WATCH_FACE_FILE.json
    
* for GTS2
  * to unpack 
    * python main.py --gts2 --file WATCH_FACE_FILE.bin
  * to pack 
    * python main.py --gts2 --file WATCH_FACE_FILE.json

Can also unpack and pack watcface resources without parsing header parameters (useful if watchface has some uknnown parapeters)
 * to unpack 
    * python main.py --gtr2 --to_raw 47 --file WATCH_FACE_FILE.bin
  * to pack 
    * python main.py --gtr2 --from_raw 47 --file WATCH_FACE_FOLDER , where WATCH_FACE_FOLDER is the folder which should contain raw_header.bin file and set of resource images

Also this project contain a GTR2_Packer.exe tool which allow to compress and decompress bin files.
usage: gtr-packer
 -cmp <filename>    Compress
 -cmp2 <filename>   Compress gtr2 format
 -unc <filename>    Decompress
 -unc2 <filename>   Decompress gtr2 format

## known issues in json
### Date/Weekday/ImageCount (GTR)
* Unlike verge lite, Date/Weekday/ImagesCount should be 21 instead of 7

```
  "Date": {
    "WeekDay": {
      "X": 242,
      "Y": 122,
      "ImageIndex": 128,
      "ImagesCount": 21
    }
  },
```
### lock icons (only works for GTR)
```
  "Status": {
    "Lock": {
```
### bluetooth icons (not working?)
```
  "Status": {
    "Bluetooth": {
```

### analog hands' releative position (only works for GTR)

## why python instead of C#
just for fun!
