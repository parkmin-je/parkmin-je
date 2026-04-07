# 박민제 (Park Min-je)

Java 백엔드 개발자 취준생입니다.  
분산 시스템과 클라우드 인프라에 관심이 많고, 실무 패턴을 직접 구현하며 공부하고 있습니다.

---

## 기술 스택

**백엔드**  
Java 21 · Spring Boot 3 · Spring Cloud (Gateway) · JPA/QueryDSL · Kafka · Redis · gRPC · Elasticsearch

**인프라**  
Docker · Docker Compose · GCP Compute Engine · GitHub Actions · Vercel

**프론트엔드**  
Next.js 15 · React · TypeScript · Tailwind CSS

**테스트**  
JUnit 5 · Testcontainers · ArchUnit · Spring Cloud Contract · Playwright · k6

---

## 주요 프로젝트

### 🛒 LiveMart — MSA 이커머스 플랫폼
> Java 21 + Spring Boot 3.3 + Next.js 15 기반 MSA 포트폴리오 프로젝트  
> **[🌐 라이브 데모](https://livemart-parkmin-jes-projects.vercel.app)** · **[⚙️ API 서버](http://34.64.189.54:8888/actuator/health)** · **[📦 GitHub](https://github.com/parkmin-je/livemart-msa-ecommerce)**

**구현 내용:**
- **Saga Choreography + Transactional Outbox** — 주문→결제→재고 분산 트랜잭션 (이벤트 유실 0)
- **gRPC 서비스 간 통신** — order↔product 상품 검증 (HTTP/2 + Protobuf 멀티플렉싱)
- **Redis Pub/Sub 분산 SSE** — 수평 확장 가능한 실시간 알림
- **결제 금액 서버 검증** — CVSS 9.3 취약점 발견 후 FeignClient 서버 재조회로 수정
- **Redisson 분산 락** — 재고 Race Condition 방지
- **Spring AI 1.0 + OpenRouter** — LLM 연동 AI 판매자 에이전트
- **7개 마이크로서비스 GCP VM 운영 중** (Docker Compose + Upstash Redis + Neon PostgreSQL)

**기술:** Java 21 · Spring Boot 3.3.6 · Spring Cloud Gateway · Kafka · Redis · Elasticsearch · gRPC · Redisson · Resilience4j · Next.js 15 · Docker

---

### 🏓 탁구 대회 관리 시스템
Spring Boot 3 + Thymeleaf + WebSocket 기반 탁구 대회 관리 플랫폼

### 🍓 라즈베리파이 IoT 대시보드
Flask + MariaDB + Chart.js로 구현한 IoT 센서 데이터 시각화

---

## 학습 기록

- 알고리즘 풀이 — Java 알고리즘 문제 풀이
- Linux 학습 일지 — Linux 명령어 및 시스템 학습

---

## 연락처

[![GitHub](https://img.shields.io/badge/GitHub-parkmin--je-181717?logo=github)](https://github.com/parkmin-je)
