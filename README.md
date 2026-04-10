# 박민제 (Park Min-je)

Java 백엔드 개발자입니다.
분산 시스템과 클라우드 인프라를 직접 구현하고 운영합니다. MSA 패턴(Saga, Outbox, CQRS)을 실제로 적용하는 데 집중합니다.

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
> **[🌐 라이브 데모](https://livemart-parkmin-jes-projects.vercel.app)** · **[📦 GitHub](https://github.com/parkmin-je/livemart-msa-ecommerce)**

**구현 내용:**
- **Saga Choreography + Transactional Outbox** — 주문→결제→재고 분산 트랜잭션 (최소 1회 전달 보장)
- **gRPC 서비스 간 통신** — order↔product 상품 검증 (HTTP/2 + Protobuf)
- **Redis Pub/Sub 분산 SSE** — 다중 인스턴스 환경 실시간 알림
- **결제 금액 서버 검증** — 클라이언트 금액 조작 가능성을 직접 발견하고 FeignClient 서버 재조회로 수정
- **Redisson 분산 락** — 재고 Race Condition 방지
- **Spring AI 1.0 + OpenRouter** — LLM 연동 AI 판매자 에이전트
- **7개 마이크로서비스 GCP VM 운영 중** (Docker Compose + Upstash Redis + Neon PostgreSQL)

**기술:** Java 21 · Spring Boot 3.3 · Spring Cloud Gateway · Kafka · Redis · Elasticsearch · gRPC · Redisson · Resilience4j · Next.js 15 · Docker

---

### 📈 Real-Time Stock Trading System
> **[📦 GitHub](https://github.com/parkmin-je/real-time-stock-trading)**

업비트 WebSocket에서 실시간 시세를 수신해 Kafka로 이벤트화하고, Redis Pub/Sub → STOMP로 브로드캐스트하는 거래 백엔드.

**구현 내용:**
- 업비트 WebSocket API 연동 — BTC/ETH 실시간 시세 수신
- Kafka `market.price.updates` 토픽 파이프라인
- Redis Pub/Sub → STOMP WebSocket 브로드캐스트
- JWT 인증, 주문/계좌/포트폴리오 서비스

**기술:** Spring Boot 3 · Kafka · Redis · WebSocket (STOMP) · JWT · JPA

---

### 🏓 탁구 대회 관리 시스템
> **[📦 GitHub](https://github.com/parkmin-je/table-tennis-tournament)**

실제 안산 지역 탁구 동호회 요청으로 만든 대회 관리 플랫폼.

**구현 내용:**
- 토너먼트 대진표 자동 생성 (Bye 처리 포함)
- WebSocket STOMP 실시간 경기 결과 브로드캐스트
- LoginAttemptService — IP별 실패 횟수 추적, Brute-Force 방어

**기술:** Java 21 · Spring Boot 3.5 · WebSocket · Spring Security · MariaDB · Thymeleaf

---

### 🌡️ Raspberry Pi SNS 플랫폼
> **[📦 GitHub](https://github.com/parkmin-je/raspberry-pi-project)**

라즈베리파이에서 Lighttpd + CGI + Flask 서버 환경을 직접 구성하고 Twitter 유사 SNS 플랫폼을 구현한 프로젝트.

**구현 내용:**
- Lighttpd + CGI + Flask 서버 환경 직접 구성 (Linux)
- 팔로우/언팔로우, 해시태그, DM, 알림 등 SNS 기능
- Many-to-Many 팔로우 관계, 타임라인 쿼리
- Werkzeug 패스워드 해싱

**기술:** Python · Flask · SQLAlchemy · SQLite · Lighttpd

---

### 💼 포트폴리오 관리 플랫폼
> **[📦 GitHub](https://github.com/parkmin-je/portfolio)**

Spring Boot 기반 포트폴리오 관리 웹 애플리케이션.

**구현 내용:**
- 포트폴리오 CRUD + 카테고리 분류 + 파일 업로드
- Apache Tika 실제 MIME 타입 검증 (파일 위조 방어)
- OWASP HTML Sanitizer XSS 방어
- Audit Log 자동 기록, Excel 내보내기 (Apache POI)
- Spring Security: BCrypt, CSRF, 동시 세션 제어

**기술:** Java 21 · Spring Boot 3 · Spring Security · Thymeleaf · MariaDB

---

## 연락처

[![GitHub](https://img.shields.io/badge/GitHub-parkmin--je-181717?logo=github)](https://github.com/parkmin-je)
