# git

현재 파일들을 안전한 상태로 관리, 과거 모습 그래도 복원가능

코드의 history 를 관리하는 도구. 개발된 과정과 역사를 기록하고 관리



## git 작업 흐름

1. add 커밋할 목록에 추가

2. commit 커밋(create a snapshot)만들기

3. push 현재까지의 역사(commits) 가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

   

 

## 명령어

$ git add helloworld.py

$ git commit -m

$ git config --global user.name "john"



### 리눅스 명령어

- pwd 홈 위치
- ls 위치 안에 파일들 목록
- clear == ctrl + l 화면창 깨끗하게
- touch 파일 만들때 ex)touch a.txt
- mkdir 폴더 만들때 ex)mkdir test
- rm 파일 지울때 ex) rm a.txt
- rm -r 폴더 지울때 ex) rm -r test\
- cd /  << 루트 최하단으로 감
- cd ~ 홈 디렉토리로 감
- cd .. 상위 폴더로 가기 (뒤로가기 버튼?)
- cd - 명령키 직전 위치로 이전

### git 명령어



- git config --global user.name suwonraison900206

- git config --global user.email suwonraison@gmail.com

- **`git status` 현재 디렉토리 git 상태를 확인할때 ** 중요합니당!

- `git commit -m "firstcommit"`

- `git log` commit 한 후 확인 할때, 이력을 볼때

- `git add .`  << 현재파일및 모든 디렉토리선택

- git init는 관리할 폴더에 최상위에 딱 한번만 사용한다.

- 파일 변경시 git add.  >> git commit -m "commit message"

- add, commit push는 추가 변경 있을때 계속

- 반드시 commit 이후에 매번 push 할 필요없다 commit은 

- `git push -u origin master` 이후에 push 명령어는 그냥 `git push` 라고만 해도 된다.

- 단 `git push origin master` 이렇게하면 계속 같은 명령어를 사용해야 한다.

- `git pull`

  ### 집에서 할때

- `git clone 가져올 자료 주소 ` 가져오면 마스터 상태 init 되어있다.

- 내용 수정하고 `git add .` 후 푸시

- 그 이후엔 `pull` 해서 이전 버전 가져온 후 진행

- "Talk is cheap, show me your code"

## jupyter







# TIL - 수업 외적인 공부(public)

구글링 해서 TIL 깔끔하게 하신분꺼 카피



# lectures - 수업내용 정리(private)





