# 메모장   
훈련소땜에 대충 만들어두는 프로젝트   
git pull origin - merge o   
git fetch origin - merge x

>remote: Support for password authentication was removed on August 13, 2021.
>
>remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote->repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
>
>fatal: Authentication failed for 'https://github.com/rosmontisu/WorkplaceEnvGit.git/'

Developer setting -> personal access tokens   
repo -> generate token   

이후로는 평소대로 git config 해두면 되는데 password 대신 token 사용

```
git config --global user.name 'rosmontisu'     
git config --global user.password 'my-token'
```

https://mkblog.co.kr/android-adb-input-command/
adb shell input 커맨드 참조한 곳


## 현재 코드 작동 방식
1. adb client device의 정보를 가진 객체 adbdevice 생성
2. 현재 에뮬레이터의 스크린을 캡쳐
   - adb shell screencap 방식
   - win32api 로 핸들 가져오는 방식(후킹)
4. cv/ocr로 스크린에서 탐색 후 좌표 추출
5. 해당 좌표로 adb를 통해 입력(클릭)
   - adb touch - o
   - android miniTouch - test
   - h/w input - consider 
   - pyautogui - consider 


## 구현 아이디어
1. 카페에서 애들 어떻게 찾을거임?   
   - 선물 선택 상태에서 말풍선 찾기
   - 처음 입장시 뜨는 방문 학생 목록으로 sd대조해서 찾기
   - 처음에 뜨는 특유의 연출로 좌표 서치
정도 생각하는중

2. 업무 태우는건 뭐로?
   - 진행중인 이벤트랑 동기화 시켜서 ap를 태우는 방식으로 생각중
   - 스케쥴 관련 api 있으면 그걸로 긁어와서 루틴 수정하는 방식
   - 없으면..

3. gui환경은 뭐로?
   - window client - C# wpf
   - web - electron

4. 라이브러리
   - ppadb
   - openCV
   - pyautogui
   - PPOCR, easyOcr

