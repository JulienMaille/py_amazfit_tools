import os
import logging

from watchFaceParser.config import Config


if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--vergelite', action='store_true', help='force VergeLite watchface')
    parser.add_argument('--gtr', type=int, choices=[42,47], help='force GTR watchface')
    parser.add_argument('--gtr2', type=int, choices=[42,47], help='force GTR2 watchface')
    parser.add_argument('--gts', action='store_true', help='force GTS watchface')
    parser.add_argument('--gts2', action='store_true', help='force GTS2 watchface')
    parser.add_argument('--gts2mini', action='store_true', help='force GTS2 mini watchface')
    parser.add_argument('--trexpro', action='store_true', help='force TRexPro watchface')
    parser.add_argument('--oldformat', action='store_true', help='force old json format for GTS2 or GTR2')
    parser.add_argument('--trex', action='store_true', help='force T-REX watchface')
    parser.add_argument('--x', action='store_true', help='force AmazfitX watchface')
    parser.add_argument('--file', nargs='+', help='''watchface.bin - unpacks watchface images and config
    watchface.json - packs config and referenced images to bin file''')
    parser.add_argument('--to_raw', action='store_true', help='save raw header and resources')
    parser.add_argument('--from_raw', action='store_true', help='generate bin from raw folder')
    parser.add_argument('--border_alignment', action='store_true', help='draw border around aligned objects in preview')
    args = parser.parse_args()

    Config.setVergeLiteMode(args.vergelite)
    Config.setGts2MiniMode(args.gts2mini)
    Config.setGtrMode(args.gtr)
    Config.setGtrMode2(args.gtr2, args.oldformat)
    Config.setGtsMode(args.gts)
    Config.setGts2Mode(args.gts2, args.oldformat)
    Config.setTrexMode(args.trex)
    Config.setTrexProMode(args.trexpro, args.oldformat)
    Config.setAmazfitXMode(args.x)

    Config.setToRaw(args.to_raw)
    Config.setFromRaw(args.from_raw)

    Config.setBorderAlignment(args.border_alignment)

    for inputFileName in args.file:
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exist." % (inputFileName, ))
            continue
        if isDirectory:
            if Config.isFromRaw():
                import program
                program.Parser.packRawWatchFace(inputFileName)
                print("Done")
            else:
                print("Not supported yet.")
            sys.exit(1)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            import program
            if inputFileExtension == '.bin':
                if Config.isToRaw(): 
                    program.Parser.unpackRawWatchFace(inputFileName)
                else:
                    program.Parser.unpackWatchFace(inputFileName)
            elif inputFileExtension == '.json':
                program.Parser.packWatchFace(inputFileName)
            else:
                print("The app doesn't support file with extension %s." % (inputFileExtension, ))
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e, ))
            import traceback
            traceback.print_stack()
            logging.exception(e)

