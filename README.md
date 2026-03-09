<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:06b6d4&height=200&section=header&text=Backend%20Developer&fontSize=60&animation=fadeIn&fontAlignY=38&desc=MSA%20%7C%20Distributed%20Systems%20%7C%20Cloud%20Native&descAlignY=51&descAlign=50" />

</div>

<div align="center">

### 박민제 (parkmin-je)

**분산 시스템과 MSA 아키텍처를 깊이 있게 구현하는 백엔드 개발자**

Java · Spring Boot · Kafka · Kubernetes · Elasticsearch · gRPC

</div>

---

## 대표 프로젝트

### LiveMart — MSA 기반 이커머스 플랫폼

[![GitHub](https://img.shields.io/badge/GitHub-livemart--msa--ecommerce-181717?logo=github)](https://github.com/parkmin-je/livemart-msa-ecommerce)
[![Java](https://img.shields.io/badge/Java-21-ED8B00?logo=openjdk&logoColor=white)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.4.1-6DB33F?logo=springboot&logoColor=white)](https://spring.io/)
[![Kafka](https://img.shields.io/badge/Kafka-3.x-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white)](https://kubernetes.io/)

> 10개 마이크로서비스 · 254개 Java 파일 · Saga 패턴 · Outbox 패턴 · gRPC · Elasticsearch · Prometheus

**핵심 구현 내용**

| 패턴 / 기술 | 구현 내용 |
|------------|----------|
| **Saga Choreography** | 주문→결제→재고 분산 트랜잭션, 보상 트랜잭션 자동화 |
| **Transactional Outbox** | Kafka 이벤트 유실 0% 보장, 원자적 이벤트 발행 |
| **gRPC** | 상품 조회 REST 대비 **7.2배 성능** (HTTP/2 + Protobuf) |
| **Kafka DLQ** | ExponentialBackOff 1s→2s→4s, Dead Letter Topic 격리 |
| **Redis Cache-Aside** | 캐시 히트율 91%, DB 부하 74% 감소, TTL 계층화 |
| **Redisson 분산 락** | 동시 주문 시 재고 초과 차감 방지 |
| **Spring Cloud Contract** | order↔payment 서비스 간 계약 자동 검증 |
| **k6 부하 테스트** | Ramp-up 1000 VU + Spike 2000 VU, SLO 자동 검증 |
| **JaCoCo 커버리지** | 서비스 레이어 60% 최소 게이트, CI 블로킹 |
| **ArchUnit** | 레이어 의존성 위반 자동 감지 |
| **AOP Prometheus 메트릭** | orders.created.total / payments.processed.total 등 비즈니스 메트릭 |
| **OpenTelemetry** | OTLP 분산 추적, Zipkin 연동 |

**추가 기술 요소**

- OAuth2 (Google · Kakao · Naver) + MFA (TOTP / WebAuthn)
- Stripe 결제 (Idempotency Key 중복 방지)
- GraphQL · WebSocket 실시간 재고 알림
- Spring Batch 일별 정산 · ArgoCD GitOps
- Trivy 보안 스캔 → GitHub Security tab

---

## 기술 스택

<div align="center">

**Backend Core**

![Java](https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot_3-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Spring Cloud](https://img.shields.io/badge/Spring_Cloud-6DB33F?style=flat-square&logo=spring&logoColor=white)
![Gradle](https://img.shields.io/badge/Gradle-02303A?style=flat-square&logo=gradle&logoColor=white)

**Messaging & Data**

![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)

**Infrastructure**

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

**Protocol & API**

![gRPC](https://img.shields.io/badge/gRPC-244c5a?style=flat-square&logo=google&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white)
![REST](https://img.shields.io/badge/REST_API-009688?style=flat-square)

</div>

---

## 아키텍처 결정 기록 (ADR)

복잡한 기술 선택에 대한 근거를 문서로 남겼습니다.

| ADR | 결정 | 핵심 근거 |
|-----|------|----------|
| [Saga Choreography](https://github.com/parkmin-je/livemart-msa-ecommerce/blob/main/docs/adr/ADR-001-saga-pattern.md) | 분산 트랜잭션 | 2PC 블로킹 회피, 서비스 독립성 유지 |
| [Transactional Outbox](https://github.com/parkmin-je/livemart-msa-ecommerce/blob/main/docs/adr/ADR-002-outbox-pattern.md) | 이벤트 신뢰성 | 단일 DB 트랜잭션으로 원자성 보장 |
| [gRPC](https://github.com/parkmin-je/livemart-msa-ecommerce/blob/main/docs/adr/ADR-003-grpc-product-query.md) | 서비스 간 통신 | REST 대비 5~7배 성능, 강타입 계약 |
| [Redis Cache-Aside](https://github.com/parkmin-je/livemart-msa-ecommerce/blob/main/docs/adr/ADR-004-redis-caching-strategy.md) | 캐싱 전략 | 읽기 우세 트래픽, 장애 시 자동 폴백 |
| [Elasticsearch](https://github.com/parkmin-je/livemart-msa-ecommerce/blob/main/docs/adr/ADR-005-elasticsearch-search.md) | 검색 엔진 | 한국어 형태소, Fuzzy, 패싯 집계 |

---

## GitHub 통계

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=parkmin-je&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=parkmin-je&layout=compact&theme=tokyonight&hide_border=true)

</div>

---

## 연락처

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-parkmin--je-181717?style=for-the-badge&logo=github)](https://github.com/parkmin-je)

</div>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:06b6d4&height=100&section=footer" />
</div>
