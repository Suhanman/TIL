# 스위치 기술

---

## 🔀 VLAN (Virtual LAN)

- 하나의 스위치에 연결된 장치들을 논리적으로 여러 개의 네트워크로 분리 할 수 있게 해주는 기술
- VLAN을 사용하면 브로드캐스트 도메인을 분리하여 한 대의 스위치를 여러 대의 스위치처럼 사용할 수 있다
- 스위치 내부에서 VLAN이 나뉘면 **VLAN 간 트래픽은 차단**된다

### 주요 명령어

| 명령어 | 설명 |
|:-------|:-----|
| `show vlan` | 장치에 설정된 VLAN 확인 |
| `(config)# vlan [VLAN ID]` | VLAN 생성 |
| `(config-vlan)# name [이름]` | VLAN 이름 지정 |

### 포트에 VLAN 할당 (Access 모드)

```
(config-if)# switchport mode access
(config-if)# switchport access vlan [vlan ID]
```

---

## 🔗 VLAN Trunk 모드

- 하나의 포트에서 **여러 개의 VLAN 트래픽**을 처리 할 수 있다

### 트렁크 모드 설정

> 인터페이스 내에서 설정

```
(config-if)# switchport mode trunk
```

### 특정 VLAN만 허용

```
(config-if)# switchport trunk allowed vlan (add) id
```
