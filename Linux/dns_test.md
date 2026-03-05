DNS 를 다음과 같이 구성하시오.
(방화벽 활성화 상태로 진행 )

주 DNS 서버 : 192.168.108.10
보조 DNS 서버 : 192.168.108.20

www.itbank.com -> 192.168.108.20

* 주 DNS 서버 종료 후 보조 DNS서버로 질의 확인

* ipconfig /flushdns


# ufw enable
# ufw allow 22/tcp
# ufw allow 53/udp
# ufw allow 53/tcp
- 방화벽 설정

# apt install -y bind9
- 

# vi /etc/bind/named.conf.default-zones
==================
zone "itbank.com" {
type master;
file "/etc/bind/itbank.com.zone";
allow-update { 192.168.108.20; };
};

===================


# vi /etc/bind/itbank.com.zone
===================
$TTL    604800
@       IN      SOA     itbank.com. mail.itbank.com. (
0       ; Serial
604800  ; Refresh
86400   ; Retry
2419200 ; Expire
604800 ) ; Negative Cache TTL


        IN      NS      itbank.com.
        IN      A       192.168.108.10

www     IN      A       192.168.108.20
===================


* 보조 DNS 설정
# apt install -y bind9
- 패키지 설정


# vi /etc/bind/named.conf.default-zones
===================
zone "itbank.com" {
type slave;
file "itbank.com.zone";
masters { 192.168.108.10; };
};
===================

# systemctl restart bind9
- 데몬 재실행

# ls -l /var/cache/bind/
- 파일 확인
