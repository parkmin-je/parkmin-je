<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=200&section=header&text=Backend%20Developer&fontSize=60&animation=fadeIn&fontAlignY=38&desc=MSA%20%7C%20Distributed%20Systems%20%7C%20Event-Driven%20Architecture&descAlignY=51&descAlign=50" />

</div>

<div align="center">

### 박민제 | Backend Engineer

분산 시스템의 복잡한 문제를 직접 구현하고 검증하는 백엔드 엔지니어입니다.
Saga Pattern, Outbox Pattern, CQRS를 프로덕션 코드 수준으로 구현했습니다.

[![GitHub followers](https://img.shields.io/github/followers/parkmin-je?style=social)](https://github.com/parkmin-je)
[![GitHub stars](https://img.shields.io/github/stars/parkmin-je?style=social)](https://github.com/parkmin-je)

</div>

---

## 주요 프로젝트

### [LiveMart MSA E-commerce](https://github.com/parkmin-je/livemart-msa-ecommerce)

8개 마이크로서비스로 구성된 분산 전자상거래 플랫폼. 분산 트랜잭션, 이벤트 기반 아키텍처, 동시성 제어를 실제로 구현하고 검증했습니다.

**해결한 핵심 기술 문제:**

**① 분산 트랜잭션 정합성** — Choreography Saga Pattern
주문 생성 시 Order → Payment → Inventory 3개 서비스에 걸친 데이터 정합성 문제.
각 서비스가 Kafka 이벤트를 소비하고 보상 트랜잭션을 실행하는 Choreography 방식으로 구현.
서비스 간 강결합 없이 Eventually Consistent 상태를 달성.

**② 이벤트 유실 방지** — Transactional Outbox Pattern
Kafka 전송과 DB 쓰기를 단일 트랜잭션으로 묶어 메시지 유실 zero 보장.
DB에 Outbox 테이블 저장 → Scheduler가 Kafka로 전달 → 확인 후 완료 처리.
5회 재시도 후 영구 실패 시 수동 개입을 위한 알림 로그 기록.

**③ 중복 주문 방지** — Idempotency Key
클라이언트가 `Idempotency-Key` 헤더 전송 시 Redis에 24시간 멱등성 키 저장.
네트워크 타임아웃으로 인한 재전송에도 중복 주문이 생성되지 않음.

**④ 재고 동시성 제어** — Redisson 분산 락 + DB 비관적 락 이중 방어
다중 인스턴스 환경에서 동일 상품에 대한 동시 주문 처리.
Redisson 분산 락으로 인스턴스 간 레이스 컨디션 방지, JPA 비관적 락으로 DB 레벨 보장.

**⑤ 외부 서비스 장애 격리** — Resilience4j Circuit Breaker
Payment Service 장애 시 Feign Client가 Circuit Breaker fallback으로 즉시 전환.
지수 백오프(1s → 2s → 4s) 재시도 후 `payment-events.DLT`로 이동하는 DLQ 설정.

**아키텍처:**
```
Client → API Gateway (Rate Limiting, JWT Auth)
       ├── Order Service    (Saga Orchestrator, Outbox, Idempotency)
       ├── Payment Service  (Resilience4j CB, Idempotency)
       ├── Inventory Service (Redisson 분산 락, 비관적 락)
       ├── Product Service  (Elasticsearch, gRPC)
       ├── User Service     (OAuth2, MFA)
       ├── Notification     (Kafka Consumer, 비동기)
       └── AI Service       (추천, 동적 가격)

Kafka: order-events, payment-events, inventory-events + *.DLT (DLQ)
Config: Spring Cloud Config Server
Discovery: Eureka
Infra: Docker Compose / Kubernetes + Helm
```

**기술 스택:**
`Java 21` `Spring Boot 3.4` `Spring Cloud` `Apache Kafka` `Redis` `PostgreSQL` `Elasticsearch` `Docker` `Kubernetes` `Helm` `GitHub Actions`

---

### [Raspberry Pi IoT Server](https://github.com/parkmin-je/raspberry-pi-project)

라즈베리파이 기반 IoT 플랫폼. Flask 웹 서버, GPIO 센서 제어, Lighttpd + CGI 파이프라인을 Linux 환경에서 직접 구축했습니다.

`Python` `Flask` `SQLAlchemy` `Lighttpd` `Linux` `GPIO`

---

## 기술 스택

**Core**
![Java](https://img.shields.io/badge/Java_21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)

**Infrastructure & Observability**
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

---

## 기술적 의사결정

주요 기술 선택 근거는 [ADR 문서](https://github.com/parkmin-je/livemart-msa-ecommerce/tree/main/docs/adr)에 기록했습니다.

| ADR | 결정 | 핵심 트레이드오프 |
|-----|------|-----------------|
| ADR-001 | Choreography Saga | 서비스 자율성 ↑ vs 이벤트 추적 복잡도 ↑ |
| ADR-002 | Transactional Outbox | 메시지 유실 zero vs 스케줄러 오버헤드 |
| ADR-003 | gRPC (상품 조회) | 저지연 내부 통신 vs 프로토콜 복잡도 |
| ADR-004 | Redis 캐싱 전략 | 응답속도 ↑ vs Cache Invalidation 복잡도 |

---

## GitHub Stats

<div align="center">

![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=parkmin-je&theme=github_dark)

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=parkmin-je&theme=github_dark" width="400"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=parkmin-je&theme=github_dark" width="400"/>

</div>

---

## Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/parkmin-je/parkmin-je/output/github-snake.svg">
</picture>

</div>

---

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/parkmin-je)

</div>
