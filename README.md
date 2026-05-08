# 박민제

Java 백엔드 개발자 취준생입니다.

---

## 기술 스택

**백엔드**  
Java 21 · Spring Boot 3 · Spring Cloud Gateway · JPA · Kafka · Redis · gRPC · Elasticsearch

**인프라**  
Docker · Docker Compose · GCP Compute Engine · GitHub Actions

**프론트엔드**  
Next.js 15 · React · TypeScript · Tailwind CSS

**테스트**  
JUnit 5 · Testcontainers · Playwright

---

## 프로젝트

### 🛒 LiveMart — MSA 이커머스
> Java 21 + Spring Boot 3.3 + Next.js 15  
> [라이브 데모](https://livemart-parkmin-jes-projects.vercel.app) · [GitHub](https://github.com/parkmin-je/livemart-msa-ecommerce)

- Saga Choreography + Transactional Outbox 패턴으로 주문→결제→재고 분산 트랜잭션 구현
- order↔product 서비스 간 gRPC 통신
- Redis Pub/Sub 기반 다중 인스턴스 SSE 알림
- Redisson 분산 락으로 재고 동시성 제어
- Spring AI + OpenRouter LLM 연동
- 7개 마이크로서비스 GCP VM 배포

**기술:** Java 21 · Spring Boot 3.3 · Spring Cloud Gateway · Kafka · Redis · Elasticsearch · gRPC · Redisson · Next.js 15

---

### 🤖 AMR Control Tower — 로봇 관제 대시보드
> Java 21 + Spring Boot 3.2 + ROS2  
> [GitHub](https://github.com/parkmin-je/amr-control-tower)

- ROS2 rosbridge WebSocket으로 로봇 상태 수집 (odom / scan / map / tf)
- SLAM 맵·LiDAR 시각화 Canvas 렌더링
- Nav2 목표 전송, WASD 수동 제어, E-Stop
- WASD Watchdog — 브라우저 종료 시 1.5초 후 자동 정지
- 로봇 오프라인 감지 — 5초 무응답 시 OFFLINE 상태 전환
- Spring Security RBAC (VIEWER / OPERATOR / ADMIN)
- Kafka 이벤트 파이프라인, Redis 세션, Flyway 마이그레이션
- Docker Compose 풀스택, Prometheus + Grafana 모니터링

**기술:** Java 21 · Spring Boot 3.2 · ROS2 · Kafka · Redis · Spring Security · Docker

---

### 📈 실시간 주식 거래 시스템
> [GitHub](https://github.com/parkmin-je/real-time-stock-trading)

- 업비트 WebSocket API로 BTC/ETH 실시간 시세 수신
- Kafka 시세 이벤트 파이프라인
- Redis Pub/Sub → STOMP WebSocket 브로드캐스트
- JWT 인증, 주문/계좌/포트폴리오 API

**기술:** Spring Boot 3 · Kafka · Redis · WebSocket · JWT

---

### 🏓 탁구 대회 관리 시스템
> [GitHub](https://github.com/parkmin-je/table-tennis-tournament)

실제 탁구 동호회 요청으로 만든 대회 관리 시스템.

- 토너먼트 대진표 자동 생성 (Bye 처리)
- WebSocket STOMP 실시간 경기 결과 업데이트
- IP별 로그인 실패 횟수 추적, Brute-Force 방어

**기술:** Java 21 · Spring Boot 3.5 · WebSocket · Spring Security · MariaDB

---

### 💼 포트폴리오 관리
> [GitHub](https://github.com/parkmin-je/portfolio)

- Apache Tika 파일 MIME 타입 검증
- OWASP HTML Sanitizer XSS 방어
- Audit Log, Excel 내보내기 (Apache POI)
- Spring Security: BCrypt, CSRF, 동시 세션 제어

**기술:** Java 21 · Spring Boot 3 · Spring Security · Thymeleaf · MariaDB

---

### 🌡️ Raspberry Pi SNS
> [GitHub](https://github.com/parkmin-je/raspberry-pi-project)

- Lighttpd + CGI + Flask 서버 직접 구성
- 팔로우/언팔로우, 해시태그, DM 기능

**기술:** Python · Flask · SQLite · Lighttpd

---

## 연락처

[![GitHub](https://img.shields.io/badge/GitHub-parkmin--je-181717?logo=github)](https://github.com/parkmin-je)
