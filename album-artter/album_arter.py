import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TRCK, TALB, APIC, TYER
import json

class AlbumArter:
    def add_album_tag(self,songs_path,tag_path):
        with open(tag_path) as f:
            data = json.load(f)
            album_title = data['Album title']
            artist = data['Album Artist']
            total_tracks = data['Total Track Numbers']
            year = str(data['Year'])

        idx = 1
        for root, _, files in os.walk(songs_path):
            for file in files:
                try:
                    # MP3 파일 경로
                    mp3_file_path = os.path.join(root, file)

                    # MP3 파일 로드
                    audio_file = MP3(mp3_file_path, ID3=ID3)

                    # 태그 추가
                    audio_file.tags.add(TIT2(encoding=3, text=file[1:-4])) #제목에 .mp3 지우고, 앞에 숫자 지우기
                    audio_file.tags.add(TPE1(encoding=3, text=artist))
                    audio_file.tags.add(TALB(encoding=3, text=album_title))
                    audio_file.tags.add(TRCK(encoding=3, text=f"{idx}/{total_tracks}"))
                    audio_file.tags.add(TYER(encoding=3, text=year))

                    # 저장
                    audio_file.save()

                    print(f"Tags added to {mp3_file_path}")

                    idx += 1
                except Exception as e:
                    print(f"Error adding tags to {mp3_file_path}: {e}")

    def add_album_art(self, songs_path, image_path):
        for (root, _, files) in os.walk(songs_path):
            for file in files:
                try:
                    # mp3 load
                    audio_file_path = os.path.join(root, file)
                    audio_file = MP3(audio_file_path, ID3=ID3)
                    # image load
                    with open(image_path, 'rb') as f:
                        image_data = f.read()
                    # load org ID3 tag
                    if 'APIC:' in audio_file.tags:
                        audio_file.tags['APIC:'].data = image_data
                    else:
                        # create new ID3 tag
                        audio_file.tags.add(
                            APIC(
                                encoding=0,  # UTF-8
                                mime='image/jpeg',
                                type=3,
                                data=image_data
                            )
                        )
                    audio_file.save()
                except Exception as e:
                    print("error: ", e)
