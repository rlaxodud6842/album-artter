# album-artter

**Album-artter**는 앨범커버, 앨범 가수, 앨범 이름, 년도, 총 트랙수 일괄적으로 삽입시켜주는 프로그램 입니다.

## 설치방법
+ 파이썬 3.7이상이 요구됩니다.
+ 가상환경 설정
     *`python3 -m venv venv` or `python -m venv venv`
+ 가상환경 활성화
   Windows: `./venv/Scripts/activate` or `cd ./venv/Scripts` AND `activate`
+ requirements 설치
    * `pip install -r requirements.txt`
 
## 노래 설정
+ `songs` 폴더내에 일괄 태깅할 음원들을 넣어주세요.
  ```
  └─songs
        Songs1.wav
        Songs2.wav
        Songs3.wav
  ```

## 태그 설정
+ tag.txt를 확인해서 EX를 참고해서 다음과 같이 수정해주세요.
+ ```
  1. Album title
   2. Album Artist
   3. Total Track Numbers
   4. YEAR
  ```
  1과같은 숫자는 없어도 되며, 순서만 지켜주면 됩니다.
## 앨범커버 설정
+ 앨범 커버는 `cover.png` 나 `cover.jpg`로 설정해주세요.

## 실행방법
  * 사용법: `python ./album-artter/main.py <path/songs> -a <path/cover.jpg> -t <path/tag.txt>`
  * main을 잘 찾아서 실행시켜주세요

## 프로젝트 구조    
```
│  cover.png
│  tag.txt
│
├─album-artter
│      album_arter.py
│      main.py
│      mp3_converter.py
│      __init__.py
│
└─songs
        Songs1.wav
        Songs2.wav
        Songs3.wav
```
