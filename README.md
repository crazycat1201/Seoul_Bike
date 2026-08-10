# 공공데이터 인사이트 분석 모음

한국 공공데이터를 정제·분석해 인사이트와 실행 가능한 개선 액션을 도출하는 프로젝트입니다. 데이터셋별로 폴더를 분리하고, 공통으로 재발생하는 정제 로직만 `common/`에 모아 재사용합니다.

## 데이터셋

| 데이터셋 | 노트북 | 시각화 리포트 | 내용 |
|---|---|---|---|
| [`datasets/seoul_bike/`](./datasets/seoul_bike/) | [`Seoul_Bike_Insight_Analysis.ipynb`](./datasets/seoul_bike/Seoul_Bike_Insight_Analysis.ipynb) | [`docs/seoul_bike_report.html`](./docs/seoul_bike_report.html) | 서울 공공자전거(따릉이) 신규가입자·외국인 대여 트렌드, 코로나 전후 비교, 대여소 핫스팟 |
| [`datasets/rail_parking/`](./datasets/rail_parking/) | [`Rail_Parking_Insight_Analysis.ipynb`](./datasets/rail_parking/Rail_Parking_Insight_Analysis.ipynb) | [`docs/rail_parking_report.html`](./docs/rail_parking_report.html) | 한국철도공사 역별 주차장 공급 규모·지역본부 간 격차 분석 |

시각화 리포트는 `docs/`에 정적 HTML로 저장되어 있습니다. GitHub은 저장소 화면에서 HTML을 코드로만 보여주므로, 실제 웹페이지로 열어보려면 **저장소 Settings → Pages → Source를 `main` 브랜치 / `docs` 폴더로 설정**하세요. 활성화하면 `https://crazycat1201.github.io/Seoul_Bike/`에서 [`docs/index.html`](./docs/index.html)을 통해 두 리포트에 바로 접근할 수 있습니다(설정 전까지는 파일을 내려받아 로컬에서 열면 됩니다).

### 실행 방법

```bash
pip install pandas numpy matplotlib openpyxl
cd datasets/<데이터셋 폴더>
jupyter notebook <노트북 파일>.ipynb
```

각 노트북은 자기 폴더의 `raw/` 하위 상대 경로만 사용하므로, 저장소를 클론한 뒤 바로 실행됩니다.

## 저장소 구조

```
datasets/
├── seoul_bike/
│   ├── raw/                          # 원본 데이터 (신규가입자·외국인 대여)
│   ├── legacy/                       # 초기 탐색용 노트북 (더 이상 유지되지 않음)
│   └── Seoul_Bike_Insight_Analysis.ipynb
└── rail_parking/
    ├── raw/                          # 원본 데이터 (역별 주차장 현황)
    └── Rail_Parking_Insight_Analysis.ipynb
common/
└── data_utils.py                     # 데이터셋 2개 이상에서 재사용되는 정제 유틸(인코딩 자동 감지 등)
```

## 새 데이터셋 추가하기

1. `datasets/<이름>/raw/`에 원본 파일을 넣습니다.
2. `datasets/<이름>/<이름>_Insight_Analysis.ipynb`를 만들고, 다음 5단 구조를 따릅니다: **①데이터 로드·정제(원자료 이슈 기록) → ②핵심 세그먼트별 트렌드 → ③가장 중요한 비교/대조 → ④데이터에 근거한 개선 액션 플랜(즉시/중기/장기) → ⑤데이터 한계 노트**.
3. 인코딩 자동 감지처럼 다른 데이터셋과 겹치는 정제 로직이 생기면 `common/data_utils.py`로 옮겨 재사용합니다. 데이터셋 하나에서만 쓰는 정제 로직은 해당 노트북에 그대로 둡니다(섣부른 추상화 지양).

공공데이터 CSV는 인코딩(UTF-8/CP949/EUC-KR)이 파일마다 다르고, 컬럼에 원자료 자체 오류(오탈자, 잘못된 카테고리 매핑 등)가 섞여 있는 경우가 많습니다. 각 노트북의 1절과 마지막 절에서 실제로 발견한 이슈와 처리 방식을 투명하게 기록하는 것을 원칙으로 합니다.
