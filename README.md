# 메모장    
훈련소땜에 대충 만들어두는 프로젝트   

https://mkblog.co.kr/android-adb-input-command/
adb shell input 커맨드 참조한 곳

## 현재 오토 코드 작동 방식
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

## 위의 구현 아이디어
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

4. 라이브러리
   - ppadb
   - openCV
   - pyautogui
   - PPOCR, easyOcr
  
## 고려중, 구현중 
- wpf환경 오픈소스인 vpet과 결합
- 언어모델은 어차피 gpt-3 llm생각중이던거 있으니까 발급해둔 api키로 vpet에 연결하면 좋을거 같음
  -> vpet에 정상적으로 연결됨. 나중에 내가 만드는 클라에서 어떻게 써먹을지 생각해보는걸로
- 서버는 centos8로 라즈베리파이에서 돌리는거 고려(클라우드도 좋지만 파이 한번 써보고 싶네)   
  -> 웹은 구글에서 centos7 클라우드로 돌리는 중. baa(임시)서버는 생각해봐야할듯?
- 아파치 서버로 웹 간단하게 열어놨음. open ai api랑 http로 통신하는거 테스트 용도로 사용할 예정. dns는 년 1.5만정도
- 디스코드 봇은 글리치 서버리스 클라우드로 하나 열어둠, 보이스 송수신은 제공해주는 api 확인해봐야할듯?

