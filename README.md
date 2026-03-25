# 박민제 (Park Min-je)

Java 백엔드 개발자 취준생입니다.  
분산 시스템과 클라우드 인프라에 관심이 많고, 실무 패턴을 직접 구현하며 공부하고 있습니다.

---

## 기술 스택

**백엔드**  
Java 21 · Spring Boot 3 · Spring Cloud (Eureka, Gateway) · JPA · Kafka · Redis · gRPC · Elasticsearch

**인프라**  
Docker · Kubernetes · GitHub Actions · AWS (EKS, RDS, ElastiCache) · Terraform · Helm · ArgoCD

**프론트엔드**  
Next.js 15 · React · TypeScript · Tailwind CSS

**테스트**  
JUnit 5 · Testcontainers · ArchUnit · Spring Cloud Contract · k6

---

## 주요 프로젝트

### [LiveMart — MSA 이커머스 플랫폼](https://github.com/parkmin-je/livemart-msa-ecommerce)
Java 21 + Spring Boot 3.4 기반 MSA 포트폴리오 프로젝트

실무에서 자주 쓰이는 분산 시스템 패턴을 직접 구현하며 공부했습니다.
- Saga Choreography + Transactional Outbox (주문→결제→재고 분산 트랜잭션)
- gRPC 서비스 간 통신 (order↔product, Protobuf + HTTP/2)
- Redis Pub/Sub 기반 수평 확장 가능한 실시간 알림 (SSE)
- Kafka DLQ + ExponentialBackOff 재시도 (장애 격리)
- Spring AI 1.0 + OpenRouter LLM 연동
- Prometheus + Grafana + OpenTelemetry 모니터링

### [탁구 대회 관리 시스템](https://github.com/parkmin-je/table-tennis-tournament)
Spring Boot 3 + Thymeleaf + WebSocket 기반 탁구 대회 관리 플랫폼

### [라즈베리파이 IoT 대시보드](https://github.com/parkmin-je/raspberry-pi-project)
Flask + MariaDB + Chart.js로 구현한 IoT 센서 데이터 시각화

---

## 학습 기록

- [알고리즘 풀이](https://github.com/parkmin-je/algorithm-practice) — Java 알고리즘 문제 풀이
- [Linux 학습 일지](https://github.com/parkmin-je/linux_diary) — Linux 명령어 및 시스템 학습
