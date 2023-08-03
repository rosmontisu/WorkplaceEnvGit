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


현재 코드 작동 방식
1. adb client device의 정보를 가진 객체 adbdevice 생성
2. 현재 에뮬레이터의 스크린을 캡쳐
3. 서치 이미지를 스크린 이미지에서 탐색
4. 서치 이미지의 위치 좌표를 추출
5. 좌표 클릭

카페에서 애들 어떻게 찾을거임?   
- 선물 선택 전과 후 이미지를 비교한다.
- 선물 선택 상태에서 채도를 극단적으로 조정하여 하얀색 말풍선의 좌표를 찾는다
정도 생각하는중

gui환경은 뭐로?
- c#공부할겸 wpf로 할까 생각중
- 일렉트론 등의 웹 환경도 끌리긴 하지만 adb건드는 프로그램이라 웹에서는 구현을 못하니까
  
게임 스케쥴이랑 데이터 수집하는 서버는?
- 고민중..

사용한 주요 라이브러리 정리
- ppadb
- win32api
- numpy
- matplotlib
- pyautogui
- paddleOcr, easyOcr
- openCv
