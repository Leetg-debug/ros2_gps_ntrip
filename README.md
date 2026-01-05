# ROS 2 GNSS RTK Integration (u-blox ZED-F9P)

이 레포지토리는 **u-blox ZED-F9P GNSS RTK 수신기**를 ROS 2 (Jazzy 기준) 환경에서 사용하기 위해

- GNSS 드라이버 (`ublox_gps`)v
- NTRIP 클라이언트 (`ntrip_client`)
- GNSS + RTCM 통합 런처 (`combined_rtk`)

를 하나의 워크스페이스에서 구성하고 실행하는 방법을 정리한 가이드입니다.

참고 자료  
- https://www.ardusimple.kr/how-to-integrate-u-blox-zed-f9p-gnss-rtk-receiver-into-ros-2-jazzy/

---

## 📁 디렉토리 구조

```bash
ublox_ws/
├── ublox_gps/        # GNSS 드라이버 (u-blox ZED-F9P)
├── ntrip_client/    # NTRIP RTCM 보정 데이터 수신
└── combined_rtk/    # GNSS + RTCM 통합 런처

---

# 1️⃣ ublox_gps (GNSS Driver)

**역할**
- `ublox_gps` 와 `ntrip_client`를 하나의 Launch 파일로 통합 실행
- RTK 구성 시 반복 실행을 단일 launch로 단순화

**실행**
```bash
ros2 launch combined_rtk combined_nodes.launch.py

---

## 2️⃣ ntrip_client (RTCM Correction)

**역할**
- NTRIP Caster에 접속
- RTCM 보정 데이터를 실시간으로 수신
- GNSS 수신기로 보정 데이터 전달

**실행**
```bash
ros2 launch ntrip_client ntrip_client_launch.py

---

## 3️⃣ combined_rtk (GNSS + RTCM 통합 실행)

**Repository**  
https://github.com/Leetg-debug/ros2_gps_ntrip

**역할**
- `ublox_gps` 와 `ntrip_client`를 하나의 Launch 파일로 통합 실행
- RTK 구성 시 반복 실행을 단일 launch로 단순화

**실행**
```bash
ros2 launch combined_rtk combined_nodes.launch.py

---

## 🧭 토픽 요약

| 토픽 이름 | 타입 | 설명 |
|----------|------|------|
| `/ublox_gps_node/fix` | `sensor_msgs/NavSatFix` | RTK 포함 최종 GNSS 위치 |
| `/fix` | `sensor_msgs/NavSatFix` | GNSS 위치 데이터 |
| `/rtcm` | `rtcm_msgs/Message` | RTK 보정 데이터 |
| `/ntrip/diagrams` | package dependent | NTRIP 연결 상태 |


각 패키지는 원본 레포지토리의 라이선스를 따릅니다.
