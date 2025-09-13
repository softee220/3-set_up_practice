# 3-setup_practice
3기 1주차 git, conda 가상환경, env환경변수 세팅, api 호출

## 제출 방법

1. 자신의 깃허브 아이디로 브랜치 만든 다음에 개인 폴더 만들어주세요.
2. 작업 하시고 커밋 후 오리진으로 푸시해주시면 됩니다.
3. main 으로 풀리퀘 날려주시면 됩니다. merge 는 하시면 안돼요! 풀리퀘 제목 : 3기_1주차_[이름]

### 예시

```bash
git clone git@github.com:HateSlop/3-set_up_practice.git  # 클론
cd 3-set_up_practice # 프로젝트 루트로 이동
git checkout -b '본인 브랜치명' # 브랜치 생성 (본인의 브랜치, 폴더 등 생성)
mkdir '본인 폴더명' # 개인 폴더 만들기
cd '본인 폴더명' # 개인 폴더로 이동
# 작업을 진행해주세요
git add . # 작업 후 add
git commit -m "[feat] ~~" # 커밋
git push origin '본인 브랜치명' # 오리진에 푸시
```

### 폴더구조

```bash
.
├── README.md # 프로젝트 설명 리드미 (수정X)
└── '본인 폴더명' #(개인 폴더)
    └── example.py # python 코드 파일(임의의 api key 출력)
    └── .gitignore # gitignore파일(.env와 가상환경파일을 숨김처리)
    └── print.png # 이미지파일(example.py를 실행했을때 .env에서 api key를 불러와서 출력, 가상환경이 실행중이어야 함)
```
### .env예시
```bash
실제 키 넣지 마시고
someting_key = "key ~ " 자유롭게 넣으시면 됩니다.
```
## 커밋 컨벤션

feat: 새로운 기능 추가  
fix: 버그 수정  
docs: 문서 수정  
style: 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우  
refactor: 코드 리팩토링  
test: 테스트 코드, 리팩토링 테스트 코드 추가  
chore: 빌드 업무 수정, 패키지 매니저 수정, production code와 무관한 부분들 (.gitignore, build.gradle 같은)  
comment: 주석 추가 및 변경  
remove: 파일, 폴더 삭제  
rename: 파일, 폴더명 수정
