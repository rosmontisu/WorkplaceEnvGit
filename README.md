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