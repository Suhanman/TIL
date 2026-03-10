# 라우터 구성요소

---

## 🖥️ CPU

- 라우팅 프로토콜을 실행하고 처리하며 패킷의 경로를 결정
- 라우터 성능에 직접적인 영향을 끼친다

---

## 💾 RAM

- 현재 사용중인 라우터의 구성 파일이 임시로 저장되는 장치
- 라우팅 테이블, 임시 데이터 등이 저장된다
- **휘발성 메모리** — 전원 공급이 중단되면 내부의 데이터가 모두 사라진다

---

## 🔋 NVRAM (비휘발성 RAM)

- 라우터의 구성 파일을 영구적으로 저장하기 위하여 사용하는 저장장치
- **비휘발성 메모리** — 전원 공급이 중단되어도 내부의 데이터가 유지된다
- 용량이 작기 때문에 대용량 데이터를 저장하지 않는다

---

## ⚡ Flash Memory

- 운영체제와 같은 대용량의 데이터가 저장된다
- **비휘발성 메모리**

---

## 📀 ROM (Read Only Memory)

- 하드웨어 부팅 시 초기화에 사용되는 프로그램들이 저장
- 시스템 복구 기능을 제공

---

## 📁 구성 파일

### 1. running-config

- 현재 사용중인 구성 파일
- **RAM**에 위치, 부팅 시에 초기화

### 2. startup-config

- 부팅 시 사용되는 구성 파일
- **NVRAM**에 위치, 영구적으로 보관

```
write / copy running-config startup-config   ← 구성파일 저장
```

---

## 📡 TFTP (Trivial File Transfer Protocol)

- 단순한 파일 전송 프로토콜
- 사용자 인증없이 파일을 저장하고 불러올 수 있다

### Running-config → TFTP 서버로 저장

```
Router#copy running-config tftp:
Address or name of remote host []? 10.0.0.10
Destination filename [Router-confg]?

Writing running-config...!!
[OK - 561 bytes]
561 bytes copied in 0 secs
```

### TFTP 서버 → Running-config로 불러오기

```
Router#copy tftp: running-config
Address or name of remote host []? 10.0.0.10
Source filename []? Router-confg
Destination filename [running-config]?

Accessing tftp://10.0.0.10/Router-confg....
Loading Router-confg from 10.0.0.10: !
[OK - 561 bytes]
```

---

## 🌐 Cisco IOS (Internetwork OS)

- Cisco 사의 장비에 사용되는 운영체제
- 대규모 트래픽, 복잡한 라우팅 등의 네트워크 작업을 안정적으로 처리하도록 설계
- 장비의 기능을 제대로 사용하기 위하여 여러 기본 설정들을 해주어야 한다

> 운영체제 파일명 예시: `c2800nm-advipservicesk9-mz.124-15.T1.bin`

### ROMMON 모드

- IOS가 없을 때 진입하게 되는 **시스템 진단 및 복구 모드**
- IOS가 없기 때문에 최소한의 기능으로만 동작한다

```
rommon 2 > IP_ADDRESS=10.0.0.123
rommon 3 > IP_SUBNET_MASK=255.255.255.0
rommon 4 > DEFAULT_GATEWAY=10.0.0.123
rommon 5 > TFTP_SERVER=10.0.0.10
rommon 6 > TFTP_FILE=c2800nm-advipservicesk9-mz.124-15.T1.bin
rommon 9 > tftpdnld
```

---

## 🔑 비밀번호 복구 작업

> 부팅 중 `Ctrl + C` → ROMMON 모드 진입

### 레지스터 값

장치 부팅 시 동작을 제어하는 요소

| 레지스터 값 | 동작 |
|:-----------:|:----:|
| `0x2102` | 정상 부팅 |
| `0x2142` | startup-config 무시 부팅 |

### 관련 명령어

```
copy running-config startup-config
copy startup-config running-config

(config)#config-register 0X2102    ← OS에서 레지스터 값의 변경
```
