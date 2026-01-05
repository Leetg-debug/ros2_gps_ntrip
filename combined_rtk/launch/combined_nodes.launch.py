from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable

def generate_launch_description():
    # ---------------------------------------------
    # Node configuration for ublox_gps
    # ---------------------------------------------
    ublox_node = Node(
        package='ublox_gps',                  # ROS 2 package containing the ublox GPS driver
        executable='ublox_gps_node',          # Executable name for the ublox GPS node
        name='ublox_gps_node',                # Name assigned to the node
        output='screen',                      # Output log to screen
        parameters=[{                         # Node parameters defined inline
            'debug': 0,                       # Debug level (0 = none)
            'device': '/dev/ttyACM0',  # Serial port where GPS is connected
            'frame_id': 'gps',                # Frame ID to tag published GPS messages
            'uart1': {
                'baudrate': 9600              # Baudrate for UART1
            },
            'tmode3': 1,                      # Survey-in mode (TMODE3 = 1)
            'sv_in': {                        # Survey-in configuration
                'reset': True,                # Reset survey-in every startup
                'min_dur': 300,               # Minimum duration for survey-in (seconds)
                'acc_lim': 3.0                # Accuracy limit for survey-in (meters)
            },
            'inf': {
                'all': True                   # Enable all INF messages on console
            },
            'publish': {
                'all': True,                  # Publish all available messages
                'aid': {
                    'hui': False              # Do not publish aiding HUI messages
                },
                'nav': {
                    'posecef': False          # Do not publish NAV-POSECEF messages
                }
            }
        }]
    )

    # ---------------------------------------------
    # Environment variable to control NTRIP client debug
    # ---------------------------------------------
    set_debug_env = SetEnvironmentVariable(
        name='NTRIP_CLIENT_DEBUG',  # Name of the environment variable
        value='false'               # Disable debug output
    )

    # ---------------------------------------------
    # Node configuration for NTRIP client
    # ---------------------------------------------
    ntrip_node = Node(
        package='ntrip_client',              # ROS 2 package containing the NTRIP client
        executable='ntrip_ros.py',           # Python script for the NTRIP client
        name='ntrip_client',                 # Name assigned to the node
        output='screen',                     # Output log to screen
        parameters=[{                        # Parameters required for NTRIP connection
            'host': 'gnss.eseoul.go.kr',  # NTRIP caster hostname
            'port': 2101,                            # NTRIP port (integer)
            'mountpoint': 'GANS-RTCM23',               # Mountpoint on the NTRIP caster
            'ntrip_version': 'None',                 # Optional NTRIP version
            'authenticate': True,                    # Use authentication (username/password)
            'username': 'seoul',  # Auth username
            'password': 'seoul',              # Auth password
            'ssl': False,                            # SSL not used
            'cert': 'None',                          # No client certificate
            'key': 'None',                           # No client key
            'ca_cert': 'None',                       # No custom CA certificate
            'rtcm_frame_id': 'odom',                 # Frame ID for published RTCM messages
            'nmea_max_length': 128,                  # Max NMEA sentence length
            'nmea_min_length': 3,                    # Min NMEA sentence length
            'rtcm_message_package': 'rtcm_msgs',     # Use the rtcm_msgs message format
            'reconnect_attempt_max': 10,             # Max reconnect attempts before giving up
            'reconnect_attempt_wait_seconds': 5,     # Wait time between reconnects
            'rtcm_timeout_seconds': 4                # Max time without RTCM before reconnect
        }],
        remappings=[
            ('/fix', '/ublox_gps_node/fix')  # Remap /fix topic to /ublox_gps_node/fix
        ]
    )

    # Return the full launch description with all configured actions
    return LaunchDescription([
        set_debug_env,  # Set environment variable for NTRIP debug
        ublox_node,     # Launch ublox GPS node
        ntrip_node      # Launch NTRIP client node
    ])
