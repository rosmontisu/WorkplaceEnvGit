(function() {
    "use strict";
    var $body = document.querySelector('body'); // <body> 요소 선택
    // Methods/polyfills.
    // classList | (c) @remy | github.com/remy/polyfills | rem.mit-license.org
    !function() {
        function t(t) {
            this.el = t; // 요소 저장
            for (var n = t.className.replace(/^\s+|\s+$/g, "").split(/\s+/), i = 0; i < n.length; i++)
                e.call(this, n[i])
        }

        function n(t, n, i) {
            // 요소에 클래스 조작 기능 추가
            Object.defineProperty ? Object.defineProperty(t, n, {
                get: i
            }) : t.__defineGetter__(n, i)
        }

        if (!("undefined" == typeof window.Element || "classList" in document.documentElement)) {
            var i = Array.prototype, e = i.push, s = i.splice, o = i.join;
            t.prototype = {
                add: function (t) {
                    // 클래스 추가
                    this.contains(t) || (e.call(this, t), this.el.className = this.toString())
                },
                contains: function (t) {
                    // 클래스 포함 여부 확인
                    return -1 != this.el.className.indexOf(t)
                },
                item: function (t) {
                    // 클래스 목록에서 해당 인덱스의 클래스 반환
                    return this[t] || null
                },
                remove: function (t) {
                    // 클래스 제거
                    if (this.contains(t)) {
                        for (var n = 0; n < this.length && this[n] != t; n++) ;
                        s.call(this, n, 1), this.el.className = this.toString()
                    }
                },
                toString: function () {
                    // 클래스 목록을 문자열로 반환
                    return o.call(this, " ")
                },
                toggle: function (t) {
                    // 클래스 토글
                    return this.contains(t) ? this.remove(t) : this.add(t), this.contains(t)
                }
            }, window.DOMTokenList = t, n(Element.prototype, "classList", function () {
                return new t(this)
            })
        }
    }();

    // canUse
    window.canUse = function (p) {
        // 브라우저 기능 지원 여부 확인
        if (!window._canUse) window._canUse = document.createElement("div");
        var e = window._canUse.style, up = p.charAt(0).toUpperCase() + p.slice(1);
        return p in e || "Moz" + up in e || "Webkit" + up in e || "O" + up in e || "ms" + up in e
    };

    // window.addEventListener
    (function () {
        if ("addEventListener" in window) return;
        window.addEventListener = function (type, f) {
            window.attachEvent("on" + type, f)
        }
    })();

    // 페이지 로딩 시 초기 애니메이션 실행.
    window.addEventListener('load', function () {
        window.setTimeout(function () {
            $body.classList.remove('is-preload'); // 'is-preload' 클래스 제거하여 선 효과 제거
        }, 100);
    });

    // 이미지 슬라이드쇼 배경.
    (function () {

        // 설정.
        var settings = {

            // 이미지 (url: 정렬 형식) 형태로 지정.
            images: {
                'images/bg01.jpg': 'center',
                'images/bg02.jpg': 'center',
                'images/bg03.jpg': 'center'
            },

            // 딜레이.
            delay: 6000

        };

        // 변수들.
        var pos = 0, lastPos = 0,
            $wrapper, $bgs = [], $bg,
            k, v;

        // 배경을 감싸는 래퍼와 배경들 생성.
        $wrapper = document.createElement('div');
        $wrapper.id = 'bg';
        $body.appendChild($wrapper);

        for (k in settings.images) {

            // 배경 생성.
            $bg = document.createElement('div');
            $bg.style.backgroundImage = 'url("' + k + '")';
            $bg.style.backgroundPosition = settings.images[k];
            $wrapper.appendChild($bg);

            // 배열에 추가.
            $bgs.push($bg);

        }

        // 주요 루프.
        $bgs[pos].classList.add('visible');
        $bgs[pos].classList.add('top');

        // 하나의 배경만 있는 경우나 트랜지션을 지원하지 않는 경우 종료.
        if ($bgs.length == 1
            || !canUse('transition'))
            return;

        window.setInterval(function () {

            lastPos = pos;
            pos++;

            // 처음으로 돌아가기 위해 감쌀 경우.
            if (pos >= $bgs.length)
                pos = 0;

            // 가장 위의 이미지들 교체.
            $bgs[lastPos].classList.remove('top');
            $bgs[pos].classList.add('visible');
            $bgs[pos].classList.add('top');

            // 마지막 이미지를 일정 시간 후에 감춤.
            window.setTimeout(function () {
                $bgs[lastPos].classList.remove('visible');
            }, settings.delay / 2);

        }, settings.delay);

    })();

})();


// 입력 받는 부분 구현
(function() {

    // 변수들 설정.
    var $form = document.querySelectorAll('#signup-form')[0]; // 가입 양식을 선택
    var $submit = document.querySelectorAll('#signup-form input[type="submit"]')[0]; // 제출 버튼을 선택
    var $message; // 메시지를 표시할 요소



    // addEventListener가 지원되지 않으면 종료.
    if (!('addEventListener' in $form))
        return;

    // 메시지 생성.
    $message = document.createElement('span'); // 새로운 span 요소 생성
    $message.classList.add('message'); // 'message' 클래스 추가
    $form.appendChild($message); // 양식에 메시지 요소 추가

    // 전송관련 메시지 표시 함수 정의.
    $message._show = function(type, text) {

        $message.innerHTML = text; // 메시지 내용 설정
        $message.classList.add(type); // 주어진 타입(성공 또는 실패) 클래스 추가
        $message.classList.add('visible'); // 'visible' 클래스 추가하여 메시지 표시

		// "전송 완료" 일정시간 보여주기
        window.setTimeout(function() {
            $message._hide(); 
			// 일정 시간 후에 메시지 감추는 함수 호출
			
        }, 3000); // 3초 후에 메시지 감춤

    };

    // 메시지 감추는 함수 정의.
    $message._hide = function() {
        $message.classList.remove('visible'); // 'visible' 클래스 제거하여 메시지 감춤
    };

    // 양식 제출 이벤트 리스너 등록.
    $form.addEventListener('submit', function(event) {

        event.stopPropagation(); // 이벤트 전파 중지
        event.preventDefault(); // 기본 제출 동작 중지

        $message._hide(); // 메시지 감추는 함수 호출

        $submit.disabled = true; // 제출 버튼 비활성화 연출
        window.setTimeout(function() {
            
			const userText = document.getElementById('user_text').value; // id="user_text"인 요소 선택
			// 입력값 가져오기
			console.log("입력값:", userText);

            // 입력 텍스트 초기화
            $form.reset(); 

            // 제출 버튼 활성화 연출 (재활성화, 버튼 누르는 연출)
            $submit.disabled = false; 

            //$message._show('success', '전송 완료!'); // 성공 메시지, 서버 부분 미구현이라 주석처리
            $message._show('failure', 'userText' + ' 전송 실패..'); // 실패 메시지 표시

        }, 750); // 0.75초 후에 양식 초기화 및 메시지 표시

    });

})();
