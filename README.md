# Naver 자동 로그인 및 검색 자동화(연습)

## 소개
이 스크립트는 `Playwright`를 사용하여 Naver에 자동 로그인하고 `Line` 계정을 통해 로그인합니다. 로그인에 성공하면 `peter-0512`을 검색하고 블로그 페이지로 이동한 후 50초 후에 브라우저를 종료합니다.

## 환경 요구 사항
1. Python 설치 (권장: Python 3.8 이상)
2. Playwright 설치
3. dotenv 설치 (`.env` 파일을 읽기 위해 필요함)

## 설치 방법

### 1. Playwright 설치
```bash
pip install playwright
playwright install
```

### 2. dotenv 설치
```bash
pip install python-dotenv
```

### 3. `.env` 파일 설정
프로젝트 디렉토리에 `.env` 파일을 생성하고 `LINE_EMAIL` 및 `LINE_PASSWORD`를 입력합니다.
```env
LINE_EMAIL=당신의 Line 계정
LINE_PASSWORD=당신의 Line 비밀번호
```

## 사용 방법

1. 스크립트 실행
```bash
python script.py
```

2. 스크립트 실행 흐름
   - 브라우저 실행
   - Naver 로그인 페이지로 이동
   - `Line` 로그인 버튼 클릭
   - `Line` 계정 및 비밀번호 입력
   - 로그인 성공 후 Naver로 리디렉션
   - `Naver Blog` 접속
   - `peter-0512` 검색
   - `peter-0512` 클릭하여 블로그 방문
   - 50초 대기 후 브라우저 종료
   - `naver_blog_category.png` 스크린샷 저장

## 주요 기능 및 기술적 세부사항
- **사람과 유사한 동작 모방**
  - `slow_mo=100`을 사용하여 속도를 늦춤
  - 랜덤 대기 (`random.randint(500, 1500)`)를 통해 인간처럼 입력 모방
  - `page.mouse.move()`를 사용하여 마우스 랜덤 이동

- **로그인 방식**
  - 환경 변수 (`dotenv`)를 통해 `LINE` 로그인 정보 저장
  - 자동으로 계정 및 비밀번호 입력 후 로그인 버튼 클릭
  - 추가 인증이 필요한 경우 수동 인증 요청

- **검색 및 탐색**
  - `Naver Blog` 접속
  - 검색창에 `peter-0512` 입력
  - `블로그` 카테고리 선택 후 검색 결과 클릭
  - 페이지 로딩 후 스크린샷 저장

## 주의 사항
- `Line` 로그인 시 추가 인증이 필요할 수 있음 (수동 인증 필요)
- `.env` 파일이 존재하고 올바른 계정 정보를 포함하고 있는지 확인
- `Playwright` 및 `dotenv` 설치 후 실행할 것
- `headless=False` 설정을 통해 브라우저 조작 확인 가능

## 발생 가능한 오류 및 해결 방법
| 오류 메시지 | 원인 | 해결 방법 |
|------------|-----|---------|
| `TimeoutError` | 로그인 인증 시간 초과 | 수동으로 인증 완료 후 Enter 키 입력 |
| `Element not found` | Naver UI 변경 또는 선택자 오류 | Naver 로그인 및 검색 페이지 구조 확인 |
| `Invalid credentials` | 계정 또는 비밀번호 오류 | `.env` 파일의 계정 정보 확인 |
| `Playwright not installed` | Playwright 미설치 | `pip install playwright && playwright install` 실행 |

## 결론
이 스크립트는 Naver 자동화 작업(로그인, 검색, 블로그 방문 등)에 적합합니다. `Playwright`를 활용하여 인간의 행동을 모방함으로써 성공률을 높일 수 있습니다.

