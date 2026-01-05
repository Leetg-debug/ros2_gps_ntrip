# ROS 2 GNSS RTK Integration (u-blox ZED-F9P)

이 레포지토리는 **u-blox ZED-F9P GNSS RTK 수신기**를 ROS 2 (Jazzy 기준) 환경에서 사용하기 위해

- GNSS 드라이버 (`ublox_gps`)
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
