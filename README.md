
# 기후변화와 식물의학 — 실습 패키지

이 패키지는 제안한 커리큘럼을 바로 실행할 수 있도록 **주차별 노트북**, **예시 데이터**, **과제 템플릿**을 제공합니다.

## 구성
- `notebooks/` — Jupyter 노트북
- `data/` — 예시 데이터 (`sample_weather_2022.csv`, `news_samples_labeled.csv`, `occurrences_sdm_toy.csv`, `soil_meta_disease.csv`, `toy_genotypes_snv.csv`)
- `docs/assignment_templates/` — 캡스톤 기획서/중간점검/최종보고 템플릿
- `utils/` — 공용 함수 `utils.py`

## 사용법
1. Python 3.11 환경을 추천합니다. 아래 중 하나로 설치하세요.
   - `pip install -r requirements.txt`
   - 또는 `conda env create -f environment.yml`
2. JupyterLab/Notebook을 실행하고 `notebooks/` 폴더의 각 주차 노트북을 순서대로 열어 실습을 진행합니다.
3. 모든 그래프는 **matplotlib**를 사용하며, 색상은 지정하지 않았습니다(수업 규정 준수).

## 데이터 개요
- `sample_weather_2022.csv`: 2022년 일자료(평균기온, 강수, 상대습도, 엽면수분 시뮬레이션) — 지표 생성/경보지수 실습
- `news_samples_labeled.csv`: 기사 텍스트 40건과 병 발생 시그널 라벨 — 텍스트 마이닝/융합지수 실습
- `occurrences_sdm_toy.csv`: 위도/경도/존재-부재와 간단한 기후 특성 — SDM 입문 실습
- `soil_meta_disease.csv`: 토양 변수와 병 발생률 — 상관/회귀 실습
- `toy_genotypes_snv.csv`: 소형 유전형 행렬 — PCA 개념 시연

## 라이선스
교육용 예시 데이터로 자유롭게 사용/수정 가능합니다.
