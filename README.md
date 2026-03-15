<div align="center">

<h1>박민제 · Park Minje</h1>

<p><strong>백엔드 개발자 취준생</strong> · Java / Spring Boot / Kafka / Kubernetes</p>

<p>
  인천광역시 &nbsp;·&nbsp; 인하공업전문대학 졸업 &nbsp;·&nbsp; 방송통신대학교 재학 중
</p>

<p>
  인천일보 아카데미 국기과정 수료 (2025.04~2025.12) &nbsp;·&nbsp; 연희직업전문학교 스마트모빌리티 과정 수료중 (2025.12~)
</p>

<p>
  <a href="mailto:alswp6@naver.com">
    <img src="https://img.shields.io/badge/Email-alswp6%40naver.com-EA4335?style=flat-square&logo=gmail&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/parkmin-je/livemart-msa-ecommerce">
    <img src="https://img.shields.io/badge/Flagship_Project-LiveMart-007396?style=flat-square&logo=spring&logoColor=white"/>
  </a>
</p>

</div>

---

## 소개

안녕하세요. Java / Spring Boot 기반 백엔드 개발을 공부하며 취업을 준비하고 있는 박민제입니다.

직접 만들어보면서 배우는 스타일이라, MSA 아키텍처 패턴을 실제 코드로 구현한 포트폴리오 프로젝트를 진행 중입니다.
백엔드 외에도 Raspberry Pi와 ROS2를 활용한 IoT·로보틱스에도 관심이 있습니다.

---

## 진행 중인 프로젝트

### 🛒 LiveMart — MSA 기반 이커머스 플랫폼

> 분산 시스템 패턴을 직접 구현해보며 공부하는 포트폴리오 프로젝트입니다.
> 현재 개발 진행 중이며, 프로덕션 운영 환경이 아닌 학습·취업 준비 목적의 프로젝트입니다.

**왜 만들었나요?**

분산 트랜잭션, 이벤트 유실, 서비스 간 통신 지연 같은 MSA의 핵심 문제들을
책이나 강의가 아닌 코드로 직접 해결해보고 싶어서 시작했습니다.

**직접 구현해본 패턴들:**

| 문제 | 선택한 방법 | 이유 |
|---|---|---|
| 분산 트랜잭션 (주문→결제→재고) | Saga Choreography | 2PC 블로킹 없이 서비스 독립성 유지 |
| Kafka 이벤트 유실 방지 | Transactional Outbox | DB 저장과 이벤트 발행을 단일 트랜잭션으로 묶음 |
| 서비스 간 통신 | gRPC (Protobuf) | REST 대비 바이너리 직렬화로 페이로드 경량화 |
| 동시 주문 재고 처리 | Redisson 분산 락 | 동시성 문제로 인한 재고 초과 차감 방지 |
| Kafka 장애 격리 | DLQ + Exponential Backoff | 1s→2s→4s, 3회 재시도 후 DLT로 분리 |
| 읽기 부하 분산 | Redis Cache-Aside | 반복 조회 쿼리를 캐시로 처리 |
| 상품 검색 | Elasticsearch (nori 형태소) | 한국어 형태소 분석, 오타 허용 검색 |

**서비스 구성 (10개 서비스, 개발 진행 중):**

```
api-gateway           Spring Cloud Gateway · JWT 검증 · Rate Limiting · Circuit Breaker
order-service         주문 · Saga · 쿠폰 · 반품 · Spring Batch
product-service       상품 · Elasticsearch · gRPC 서버 · GraphQL · WebSocket
payment-service       Stripe 결제 · 환불 · DLQ 처리
user-service          회원 · JWT · OAuth2 (Google/Kakao/Naver) · MFA
analytics-service     판매 분석 · A/B 테스트
inventory-service     재고 관리 · 자동 발주
notification-service  이메일/알림 (Kafka 이벤트 기반)
eureka-server         서비스 레지스트리
config-server         중앙 설정 관리
```

**기술 스택:**

```
Backend     Java 21 · Spring Boot 3.4.1 · Spring Cloud 2024.0.0 · Gradle
Frontend    TypeScript · React
Messaging   Apache Kafka · Dead Letter Queue
Database    PostgreSQL · Redis · Elasticsearch 8
Auth        JWT · OAuth2 · MFA (TOTP/WebAuthn)
Payment     Stripe (Idempotency Key 기반 중복 방지)
Infra       Docker · Kubernetes · GitHub Actions · Helm · ArgoCD
IaC         Terraform (HCL)
Monitoring  Prometheus · Grafana · OpenTelemetry → Zipkin
Testing     JUnit 5 · Testcontainers · Spring Cloud Contract · k6 · JaCoCo
Dev Env     Windows 11 · WSL2 · IntelliJ IDEA 2025.3.2
```

**아키텍처 의사결정 기록 (ADR):**
[ADR-001 Saga](./docs/adr/ADR-001-saga-choreography.md) · [ADR-002 Outbox](./docs/adr/ADR-002-transactional-outbox.md) · [ADR-003 gRPC](./docs/adr/ADR-003-grpc-communication.md) · [ADR-004 Cache](./docs/adr/ADR-004-cache-aside.md) · [ADR-005 Elasticsearch](./docs/adr/ADR-005-elasticsearch.md)

---

### 🤖 AMR-Pilot — 자율이동로봇 시뮬레이션 (진행 중)

> ROS2 Humble + Gazebo로 자율주행 로봇을 공부하는 프로젝트입니다.

- [x] Gazebo 시뮬레이션 환경 구성
- [x] LiDAR 데이터 RViz2 시각화
- [ ] SLAM 기반 지도 생성
- [ ] Nav2 자율 경로 계획
- [ ] YOLO 객체 인식 연동

**스택:** ROS2 Humble · Gazebo · TurtleBot3 · SLAM Toolbox · Nav2 · Python/C++

---

### 🍓 Raspberry Pi IoT 대시보드

> DHT11 센서 데이터를 Flask + MariaDB로 수집하고 Chart.js로 시각화한 프로젝트입니다.

- 10초 간격 자동 수집, 30°C 초과 시 알림, 시간대별 트렌드 분석
- **스택:** Python · Flask · MariaDB · Chart.js · PyMySQL

---

### 📚 ROS Noetic Study

ROS Noetic 학습 기록 저장소입니다. 토픽 통신, 서비스 통신, TF 변환, Wall-follower 로봇 구현 등을 다룹니다.

---

## 기술 스택

**주로 사용하는 것:**

![Java](https://img.shields.io/badge/Java_21-007396?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux_WSL2-FCC624?style=flat-square&logo=linux&logoColor=black)

**공부하며 쓰는 것:**

![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![ROS2](https://img.shields.io/badge/ROS2_Humble-22314E?style=flat-square&logo=ros&logoColor=white)

---

## 지금까지의 흐름

```
2024           Arduino LED 제어, Linux 일기 → 개발 기초 다지기
2025.01        GitHub 시작
2025.04~12     인천일보 아카데미 국기과정 수료
               → Raspberry Pi 센서 대시보드, ROS Noetic, Linux 자동화 학습
2025.09~       LiveMart MSA 프로젝트 시작 (병행 개발)
2025.12.31~    연희직업전문학교 스마트모빌리티 과정 수료 중
               → ROS2 + Gazebo 자율이동로봇 시뮬레이션
2026.03        현재 — LiveMart 개발 중 · 백엔드 취업 준비 중
```

---

## 연락처

📧 alswp6@naver.com  
📍 인천광역시, 대한민국
