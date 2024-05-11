# album-artter

**Album-artter**는 앨범커버, 앨범 가수, 앨범 이름, 년도, 총 트랙수 일괄적으로 삽입시켜주는 프로그램 입니다.

## 설치방법
+ 파이썬 3.7이상이 요구됩니다.
+ 가상환경 설정
     `python3 -m venv venv` or `python -m venv venv`
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
+ tag.json를 확인해서 각 값에 원하는 입력을 해주세요.
+ ```
    {
    "Album title" : "Test Title",
    "Album Artist": "Test Example",
    "Total Track Numbers" : 7,
    "Year": 2024
    }
  ```
+ 데이터 타입을 지켜주세요!
## 앨범커버 설정
+ 앨범 커버는 `cover.png` 나 `cover.jpg`로 설정해주세요.

## 실행방법
  * 사용법: `python ./album-artter/main.py <path/songs> -a <path/cover.jpg> -t <path/tag.txt>`
  * 예시: `python ./album-artter/main.py ./songs -a ./cover.jpg -t ./tag.json`
  * main을 잘 찾아서 실행시켜주세요

## 프로젝트 구조    
```
│  cover.png
│  tag.json
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


## TODO
+ 노래 타이틀 앨범스플리터에 국한되지 않고, 적절히 파싱되게 하기.
+ 최적화, 모듈화