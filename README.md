<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:EEFF00,100:a82da8&height=200&section=header&text=Backend%20Developer&fontSize=60&animation=fadeIn&fontAlignY=38&desc=Learning%20MSA%20and%20Distributed%20Systems&descAlignY=51&descAlign=50" />

</div>

<div align="center">

### 👋 안녕하세요! 박민제입니다

**MSA 아키텍처**와 **분산 시스템**을 학습하고 구현하는 백엔드 개발자입니다.
Spring Boot, Kafka, Redis를 활용한 마이크로서비스 개발에 집중하고 있습니다.

[![GitHub followers](https://img.shields.io/github/followers/parkmin-je?style=social)](https://github.com/parkmin-je)
[![GitHub stars](https://img.shields.io/github/stars/parkmin-je?style=social)](https://github.com/parkmin-je)

</div>

---

## 🎯 학습 목표

- **MSA 패턴 심화**: Saga Pattern, CQRS, Event Sourcing
- **분산 시스템**: 분산 락, 분산 트랜잭션, 동시성 제어
- **메시지 큐**: Kafka를 활용한 이벤트 기반 아키텍처
- **DevOps**: Docker, Kubernetes, CI/CD 파이프라인

---

## 🏆 주요 프로젝트

### 💼 Backend Systems

#### 🛒 [LiveMart MSA E-commerce](https://github.com/parkmin-je/livemart-msa-ecommerce)
```
마이크로서비스 아키텍처 학습을 위한 전자상거래 플랫폼
```
**핵심 구현:**
- **Saga Pattern**: 분산 트랜잭션 및 보상 로직 (Order → Payment → Inventory)
- **분산 락**: Redis Redisson을 활용한 재고 동시성 제어
- **이벤트 기반**: Kafka를 통한 서비스 간 비동기 통신
- **MSA 인프라**: Eureka, API Gateway, Config Server

**기술 스택:**
- Core: Java 21, Spring Boot 3.4, Spring Cloud
- Messaging: Apache Kafka
- Cache: Redis (Standalone)
- Database: PostgreSQL (서비스별 독립 DB)
- Container: Docker, Kubernetes + Helm

**학습 성과:**
- MSA 구조에서의 데이터 일관성 처리 방법 이해
- 분산 환경에서의 동시성 제어 구현 경험
- 이벤트 기반 아키텍처의 장단점 학습

---

### 🤖 IoT & Embedded

#### 🔧 [Raspberry Pi IoT Server](https://github.com/parkmin-je/raspberry-pi-project)
```
라즈베리파이 기반 웹 서버 및 GPIO 제어
```
**구현 내용:**
- Flask 웹 애플리케이션 (회원가입/로그인)
- Lighttpd 웹 서버 설정
- CGI를 통한 Python 스크립트 실행
- GPIO 센서 제어 인터페이스

**기술 스택:** Python (Flask), Lighttpd, Linux, GPIO

---

## 🛠️ 기술 스택

### Core (실무 수준으로 활용 가능)
![Java](https://img.shields.io/badge/Java_21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)

### Familiar (구현 경험 있음)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

### Learning (현재 학습 중)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

---

## 📊 GitHub Stats

<div align="center">

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=parkmin-je&theme=github_dark)

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=parkmin-je&theme=github_dark" width="400"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=parkmin-je&theme=github_dark" width="400"/>

</div>

---

## 💡 학습 중인 기술

<div align="center">

| Backend Architecture | DevOps | Distributed Systems |
|:---:|:---:|:---:|
| Saga Pattern | Kubernetes | 분산 락 (Redisson) |
| CQRS | Docker Compose | 이벤트 소싱 |
| API Gateway | CI/CD Pipeline | 메시지 큐 (Kafka) |
| Service Discovery | Helm Charts | 동시성 제어 |

</div>

---

## 🌱 최근 학습 내용

- **분산 트랜잭션**: Saga Pattern의 Orchestration vs Choreography 비교 학습
- **동시성 제어**: Redis 분산 락을 활용한 재고 관리 구현
- **이벤트 기반 설계**: Kafka를 통한 서비스 간 느슨한 결합 구현
- **MSA 패턴**: Circuit Breaker, Service Mesh 개념 학습

---

## 📖 학습 과정에서 해결한 문제들

### 1. Redis Cluster vs Standalone
**문제**: 로컬 개발 환경에서 Cluster 설정으로 인한 연결 실패
**해결**: 환경별 설정 분리, Standalone 모드로 전환
**학습**: 개발/프로덕션 환경 차이 이해

### 2. Saga Pattern 보상 트랜잭션
**문제**: 분산 환경에서 트랜잭션 롤백 처리
**해결**: Order Service를 Orchestrator로 두고 보상 로직 구현
**학습**: 분산 시스템에서의 데이터 일관성 유지 방법

### 3. Feign Client API 통합
**문제**: 서비스 간 API 호출 시 경로 및 DTO 불일치
**해결**: API 버전 관리 컨벤션 정립, DTO 매핑 레이어 추가
**학습**: 마이크로서비스 간 계약 설계의 중요성

---

## 🎯 다음 학습 계획

- [ ] Elasticsearch를 활용한 상품 검색 기능 고도화
- [ ] Zipkin을 통한 분산 추적 구현
- [ ] Spring WebFlux 반응형 프로그래밍 학습
- [ ] 통합 테스트 자동화 (Testcontainers)
- [ ] Kubernetes StatefulSet 및 Operator Pattern

---

## 📫 Contact

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parkmin-je)

</div>

---

## 🐍 Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake.svg">
</picture>

</div>

---

<div align="center">

**"학습하고, 구현하고, 이해합니다"**

*2024-2026 백엔드 개발자 학습 여정*

</div>
