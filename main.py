import argparse
import os

import album_arter
import mp3_converter

def main():
    parser = argparse.ArgumentParser(description='Put wav folder')
    parser.add_argument('folder_path', help='Put wav folder path or mp3 folder path')
    parser.add_argument('-a','--art', help='Put on album art path',dest="art_path")
    parser.add_argument('-t','--tag', help='Put on tagging information path',dest="tag_path")

    args = parser.parse_args()
    #
    # if args.art_path:
    #     ar = album_arter.AlbumArter()
    #     #mp3로 바꾸고
    #     mp3_path= mp3_converter.convert_wav_to_mp3(args.folder_path)
    #     #앨범아트 넣기
    #     ar.add_album_art(mp3_path,args.art_path)

    if args.tag_path:
        ar = album_arter.AlbumArter()
        mp3_path = os.path.join(args.folder_path, "mp3")
        print(args.folder_path)
        print(mp3_path)
        ar.add_album_tag(mp3_path,args.tag_path)

if __name__ == '__main__':
    main()
