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
1️⃣ ublox_gps (GNSS Driver)

Repository
https://github.com/KumarRobotics/ublox

역할

u-blox ZED-F9P GNSS 수신기와 시리얼 통신

위도, 경도, 고도 및 RTK Fix 결과를 ROS 토픽으로 퍼블리시

실행
ros2 launch ublox_gps ublox_gps_node-launch.py

주요 토픽
토픽 이름	설명
/ublox_gps_node/fix	GNSS 최종 위치 결과 (위도·경도·고도, RTK 상태 포함)
/fix	GNSS 위치 데이터 (sensor_msgs/NavSatFix)
2️⃣ ntrip_client (RTCM Correction)

Repository
https://github.com/LORD-MicroStrain/ntrip_client

역할

NTRIP Caster에 접속

RTCM 보정 데이터를 실시간으로 수신

GNSS 수신기로 보정 데이터 전달

실행
ros2 launch ntrip_client ntrip_client_launch.py

주요 토픽
토픽 이름	설명
/rtcm	RTK 보정 데이터 (위치 데이터 아님, GNSS 입력용)
/ntrip/diagrams	NTRIP 연결 상태 (패키지별 상이)
3️⃣ combined_rtk (GNSS + RTCM 통합 실행)

Repository
https://github.com/Leetg-debug/ros2_gps_ntrip

역할

ublox_gps 와 ntrip_client를 하나의 Launch 파일로 통합 실행

RTK 구성 시 반복 실행을 단일 launch로 단순화

실행
ros2 launch combined_rtk combined_nodes.launch.py

📡 전체 데이터 흐름
NTRIP Caster
     │
     ▼
[ntrip_client]
     │  RTCM (/rtcm)
     ▼
[u-blox ZED-F9P]
     │  GNSS Raw + RTCM 적용
     ▼
[ublox_gps]
     │
     ▼
/fix , /ublox_gps_node/fix

🧭 토픽 요약
토픽 이름	타입	설명
/ublox_gps_node/fix	sensor_msgs/NavSatFix	RTK 포함 최종 GNSS 위치
/fix	sensor_msgs/NavSatFix	GNSS 위치 데이터
/rtcm	rtcm_msgs/Message	RTK 보정 데이터
/ntrip/diagrams	package dependent	NTRIP 연결 상태
✅ 사용 시 체크리스트

ZED-F9P 시리얼 포트 및 baudrate 설정 확인

NTRIP caster 주소 / 포트 / mountpoint 확인

RTCM 입력이 ZED-F9P로 정상 전달되는지 확인

/ublox_gps_node/fix 에서 RTK FIX / FLOAT 상태 확인

📌 참고 사항

ROS 2 Jazzy 기준

RTK FIX까지 수 분 소요 가능 (환경 의존)

실외, 하늘 시야 확보 필수

📄 License

각 패키지는 원본 레포지토리의 라이선스를 따릅니다.
