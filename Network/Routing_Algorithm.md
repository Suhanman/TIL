# 📡 라우팅 알고리즘

---

## 🔗 Link State

- 라우터가 네트워크 전체 토폴로지를 파악하여 최적의 경로를 계산한다.
- 전체 라우터 네트워크 토폴로지를 파악하고 있어서 장애 발생 시에 대체 경로를 빠르게 찾을 수 있다.
- 네트워크 정보 변경 시 변경된 정보만 즉시 전파되어 효율성과 수렴 속도가 높아진다
- 전체 토폴로지를 파악하고 경로 연산을 해야하므로 많은 리소스를 소모한다.

### LSDB (Link State DataBase)
- Link State 라우터가 수집한 네트워크 정보를 저장하는 데이터베이스
- 같은 영역의 모든 라우터는 동일한 LSDB를 가져 일관적인 경로 선택이 가능하다

### SPF (Shortest Path First)
- LSDB에서 최적 경로를 찾기 위한 알고리즘
- 자기 자신으로부터 목적지 네트워크 비용이 가장 낮은 경로를 계산한다
- 제일 좋은 최적 경로로 계산된 경로가 라우팅 테이블에 등록된다.

---

## 🌐 OSPF (Open Shortest Path First)

- **Link State 알고리즘**
- 네트워크 전체 상태 정보를 기반으로 최적의 경로를 계산한다
- 벤더사 종류에 상관없이 모든 라우터에서 사용 가능
- Area를 통하여 계층화된 라우팅 정보 관리가 가능하다
- VLSM을 완벽히 지원하여 IP 주소 효율성이 높다
- 현재 가장 많이 사용되는 **IGP (Interior Gateway Protocol)**

---

### 📊 OSPF Cost 값

더 효율적인 경로를 선택하기 위한 기준

| 대역폭 | Cost (기준 대역폭 10Mbps) | Alternative-Cost (기준 대역폭 10Gbps) |
|--------|--------------------------|---------------------------------------|
| 56kbps | 1,785 | 182,809 |
| 64kbps | 1,562 | 159,958 |
| 128kbps | 781 | 79,929 |
| T1 (1.544Mbps) | 64 | 6,475 |
| E1 (2.048Mbps) | 48 | 4,882 |
| Ethernet (10Mbps) | 10 | 1,000 |
| FastEthernet (100Mbps) | 1 | 100 |
| GigabitEthernet (1Gbps) | 1 | 10 |
| 10-GigabitEthernet (10Gbps) | 1 | 1 |

---

### 🗂️ Area

- 대규모 네트워크 환경에서 라우팅 정보를 효율적으로 관리하기 위하여 Area로 영역을 나누어 라우팅 정보를 관리한다.
- 동일 Area 내의 라우터들은 모두 동일한 LSDB를 유지한다.

#### 백본 영역 (Area 0)
- OSPF에서의 중심이 되는 Area
- Area들을 연결하여 다른 Area 간의 라우팅 정보를 중계한다
- 기본적으로 다른 Area 간의 라우팅 정보는 차단되지만 백본 영역 (Area 0)의 중계를 받아서 라우팅 정보를 교환할 수 있다

#### ABR (Area Border Router)
- Area와 Area의 경계에 위치하는 라우터
- ABR은 자신이 연결된 각 Area의 LSDB를 모두 가지고 있으며, 해당 Area들의 경로 정보를 요약하여 다른 Area로 전달한다

---

### 🏆 DR / BDR

#### DR (Designated Router)
- OSPF에 의하여 관리되는 특정 네트워크 내의 중앙 관리자 라우터
- 네트워크 내부의 모든 라우터들의 링크 상태를 수집하고 이를 정리하여 각 라우터들에게 재전파
- 라우터들은 네트워크 내의 모든 라우터들과 통신하지 않고 DR과만 통신하며 네트워크 정보를 관리한다

#### BDR (Backup Designated Router)
- DR의 백업 라우터
- DR이 다운될 경우 BDR이 DR의 역할을 즉시 대체한다

#### DR/BDR 선출 기준

| 우선순위 | 기준 | 설명 |
|----------|------|------|
| 1순위 | 우선순위 (Priority) | 가장 높은 우선순위 값을 가진 라우터가 DR이 된다. 관리자 임의로 0~255 값까지 설정 가능 |
| 2순위 | Router ID | 우선순위가 동일할 시, Router ID 값이 가장 높은 라우터가 DR로 선출된다 |

---

### 📨 LSA (Link State Advertisement)

- OSPF에서 라우터들이 링크 상태를 교환하기 위하여 사용하는 메시지
- 라우터 ID, 링크 비용, 네트워크 정보 등이 포함된다

| 유형 | 이름 | 생성자 | 설명 |
|------|------|--------|------|
| LSA-1 | Router LSA | 모든 라우터 | 라우터 자신의 링크 상태 광고 |
| LSA-2 | Network LSA | DR | Multi-Access 네트워크의 라우터 목록 광고 |
| LSA-3 | Summary LSA | ABR | 한 Area의 경로를 다른 Area로 광고 |
| LSA-4 | Summary LSA (ASBR) | ABR | ASBR의 위치를 다른 Area로 광고 |
| LSA-5 | External LSA | ASBR | OSPF 외부 경로 광고 |

---

### 📦 OSPF의 Packet

라우터 간의 서로 정보 교환을 위하여 5종류의 패킷을 교환한다

| 타입 번호 | 이름 | 설명 |
|-----------|------|------|
| 1 | Hello | 이웃(Neighbor)을 찾고 관계를 유지한다. |
| 2 | DBD (DD) | LSDB(데이터베이스)의 요약 목록을 교환한다. |
| 3 | LSR | DBD를 보고 자신에게 없는 정보(LSA)를 요청한다 |
| 4 | LSU | LSR에 대한 응답, LSA 정보를 전송한다. |
| 5 | LSAck | 확인 응답. |

---

### ⌨️ OSPF 설정 명령어

```
Router(config)# router ospf 1
```
> OSPF 라우팅 프로세스 시작 / OSPF 설정 모드 진입

```
Router(config-router)# auto-cost reference-bandwidth 10000
```
> 기준 대역폭 값 변경 (10Gbps)

```
Router(config-router)# router-id 1.1.1.1
```
> 라우터 ID 수동 설정

```
Router(config-router)# network [network id] [wildcard Mask] area [Area ID]
```
> 광고할 네트워크 대역 지정

#### WildCard Mask
IP 주소의 특정 부분을 일치시키거나 무시하기 위해 사용되는 값

| 비트값 | 의미 |
|--------|------|
| `0` | 일치해야 하는 값 |
| `1` | 무시해도 되는 값 |

**예시** (`ping 10.0.0.123` 기준)

```
서브넷 마스크  : 255.255.255.0   →  1111 1111. 1111 1111. 1111 1111. 0000 0000
와일드카드 마스크 : 0.0.0.255    →  0000 0000. 0000 0000. 0000 0000. 1111 1111
```

### 🔍 OSPF 확인 명령어

| 명령어 | 설명 |
|--------|------|
| `show ip route` | 라우팅 테이블 출력 |
| `show ip protocol` | 현재 사용중인 라우팅 프로토콜 정보 출력 |
| `show ip ospf neighbor` | 이웃 관계 테이블 출력 |
| `show ip ospf interface` | 각 인터페이스별 OSPF 정보 출력 |

---

## ⚡ Advance Distance Vector

- Distance Vector의 단점을 보완, 발전시킨 라우팅 프로토콜
- 홉 카운트만에 의존하는 것이 아닌 대역폭, 지연시간, 신뢰도 등을 종합적으로 평가해 메트릭 값으로 사용한다.
- 일정한 시간을 주기로 정보를 전송하지 않고, 변경사항이 발생하는 즉시 필요한 만큼의 정보만 전송한다.

---

## 🔧 EIGRP

Cisco에서 개발한 라우팅 프로토콜. 초기에는 Cisco 장비들만 사용 가능하였지만 현대에는 일부 기술이 공개되어 다른 벤더사의 장비도 사용할 수 있다.

- 기존 Distance Vector 프로토콜의 단점을 보완하기 위하여 등장하였다.
- Distance Vector와 Link State의 특징이 혼합되어 **하이브리드 프로토콜**로 분류된다
- **Dual 알고리즘**을 사용하여 라우팅 정보 및 경로를 관리한다
- **Classless Protocol**로 서브네팅을 인식한다.

---

### 🧮 Dual 알고리즘 (Diffusing Update Algorithm)

- EIGRP에서 경로 정보를 관리하는 핵심 알고리즘
- Successor(최적경로), Feasible Successor(대체 경로)를 계산하여 테이블에 저장

#### Successor (최적경로)
- 목적지까지 가는 Metric(비용)이 가장 낮은 경로
- 라우팅 테이블에 저장되어 라우팅에 사용된다

#### Feasible Successor (대체 경로)
- Successor 경로에 장애가 발생하였을 때 즉시 대체할 수 있는 경로
- Feasibility Condition (FC) 조건을 만족하는 경로

#### Feasibility Condition
라우팅 루프를 방지하는 대체 경로를 찾기 위한 기준

> **RD < FD** 를 만족해야한다.

| 용어 | 전체명 | 설명 |
|------|--------|------|
| **FD** | Feasible Distance | 라우터가 목적지까지 가기 위한 최적 경로의 비용값 |
| **RD** | Reported Distance | 이웃 라우터가 목적지까지의 가기 위한 경로값 |

#### 불균등 부하 분산 (Unequal Load Balancing)
Feasible Condition을 만족하는 경로가 하나 이상 있을 경우, 트래픽을 분산하여 전송한다.

---

### 📦 EIGRP 패킷

| 번호 | 이름 | 설명 |
|------|------|------|
| 1 | Hello | 인접 라우터와 이웃 관계를 설정하고 유지하는 데 사용하는 패킷. 이웃관계를 맺고 주기적으로 Hello 패킷을 주고 받으며, 일정 시간동안 패킷을 주고 받지 못하면 이웃 관계를 끊는다. |
| 2 | Update | 자신의 경로 정보에 변경 사항이 있을 때, 정보를 전파하기 위한 패킷 |
| 3 | Query | 새로운 경로 정보를 찾을 때 인접 라우터에게 정보를 요청하는 패킷 |
| 4 | Reply | Query 패킷에 대한 응답, 요청 받은 경로에 대한 정보를 전달한다 |
| 5 | ACK | Update, Query, Reply 패킷에 대한 수신 응답 |

---

### 🗃️ EIGRP 테이블

| 테이블 | 설명 |
|--------|------|
| **Neighbor Table** | 인접한 이웃 라우터에 대한 정보를 저장하는 테이블 |
| **Topology Table** | 모든 경로 정보를 저장하는 테이블. Dual 알고리즘에 의하여 계산된 최적 경로, 대체 경로 정보가 포함된다 |
| **Routing Table** | 실제 데이터 전달에 사용되는 최적의 경로를 전달한 테이블 |

---

### ⌨️ EIGRP 명령어

```
Router(config)# router eigrp [AS 번호]
```
> EIGRP 라우팅 프로세스 시작 / EIGRP 설정 모드 진입  
> ⚠️ AS 번호가 동일해야 다른 라우터와의 이웃관계를 맺는다

```
no auto-summary
```
> 네트워크 자동 요약 방지 / Classless 설정

```
network [네트워크 ID] [와일드카드 마스크]
```

### 🔍 EIGRP 확인 명령어

| 명령어 | 설명 |
|--------|------|
| `show ip route` | 라우팅 테이블 확인 |
| `show ip eigrp topology` | 토폴로지 테이블 확인 |
| `show ip eigrp neighbors` | 이웃관계 테이블 확인 |
