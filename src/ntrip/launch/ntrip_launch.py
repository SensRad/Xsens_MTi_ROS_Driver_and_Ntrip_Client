import launch
from launch_ros.actions import Node


def generate_launch_description():
    return launch.LaunchDescription(
        [
            Node(
                package="ntrip",
                executable="ntrip",
                name="ntrip_client",
                output="screen",
                parameters=[
                    {"ip": "3.143.243.81"},  # Change to the IP address of Your NTRIP service
                    {"port": 2101},  # Change to your port number, WGS84
                    {"user": "<mail-address>"},  # Change to your username
                    {"passwd": ""},  # Change to your password
                    {"mountpoint": "Ekekullen"},  # Change to your mountpoint
                    {
                        "report_interval": 5
                    },  # the report interval to the NTRIP Caster, default is 1 sec
                ],
            ),
        ]
    )
