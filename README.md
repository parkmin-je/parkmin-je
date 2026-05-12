# 박민제

GCP에서 8개 마이크로서비스를 직접 배포·운영 중인 Java 백엔드 개발자입니다.  
분산 트랜잭션·Race Condition·결제 보안 취약점 등 운영 환경의 실제 문제를 아키텍처 수준에서 해결해왔습니다.

---

## 기술 스택

**백엔드**  
Java 21 · Spring Boot 3 · Spring Cloud Gateway · JPA · Kafka · Redis · gRPC · Elasticsearch

**인프라**  
Docker · Docker Compose · GCP Compute Engine · GitHub Actions

**프론트엔드**  
Next.js 15 · React · TypeScript · Tailwind CSS

**테스트**  
JUnit 5 · Testcontainers · Playwright · k6

---

## 프로젝트

### 🛒 LiveMart — MSA 이커머스
> Java 21 + Spring Boot 3.4 + Next.js 15  
> [라이브 데모](https://livemart-parkmin-jes-projects.vercel.app) · [GitHub](https://github.com/parkmin-je/livemart-msa-ecommerce)

- Saga Choreography + Transactional Outbox — Kafka 장애 시나리오 500 VU 테스트에서 이벤트 유실 **0건** (k6 실측)
- Cache-Aside 적용으로 상품 조회 응답시간 **1,240ms → 72ms** 단축 (k6 p99 실측)
- Burp Suite로 결제 취약점 직접 발견 → 서버 측 금액 재검증으로 수정
- Redis Pub/Sub으로 다중 인스턴스 SSE 분산 브로드캐스트
- Redisson 분산 락으로 500 VU 동시 주문 재고 Race Condition **0건**
- 8개 마이크로서비스 GCP VM 배포 · Vercel 프론트엔드 운영 중

**기술:** Java 21 · Spring Boot 3.4 · Spring Cloud Gateway · Kafka · Redis · Elasticsearch · gRPC · Redisson · Next.js 15

---

### 🤖 AMR Control Tower — 로봇 관제 대시보드
> Java 21 + Spring Boot 3.2 + ROS2  
> [GitHub](https://github.com/parkmin-je/amr-control-tower)

- Ubuntu VM에 ROS2 Humble 환경 직접 구성 후 rosbridge WebSocket으로 Spring Boot 연동
- slam_toolbox OccupancyGrid → PNG Canvas 실시간 렌더링 + `/tf` 변환으로 로봇 위치 오버레이
- RBAC 3단계 (VIEWER / OPERATOR / ADMIN), E-Stop, Nav2 목표 전송
- Kafka 이벤트 파이프라인, Flyway 마이그레이션, Docker Compose 풀스택

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

실제 안산 탁구 동호회 요청으로 만든 대회 관리 시스템 (100명 규모 실사용).

- N+1 쿼리 최적화 — 쿼리 50개 → 2개, 응답시간 **3초 → 0.5초**
- 토너먼트 대진표 자동 생성 (Bye 처리)
- WebSocket STOMP 실시간 경기 결과 업데이트
- IP별 로그인 실패 추적, Brute-Force 방어

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

📧 alswp6@naver.com  
[![GitHub](https://img.shields.io/badge/GitHub-parkmin--je-181717?logo=github)](https://github.com/parkmin-je)
