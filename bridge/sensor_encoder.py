"""
bridge/sensor_encoder.py
Encodes camera frames + IMU readings into spike trains that feed the
optic lobe and mechanosensory input channels of the connectome sim.
"""


class SensorEncoder:
    def __init__(self, channel_map):
        self.channel_map = channel_map

    def encode_frame(self, frame):
        """Convert a camera frame into photoreceptor-channel spikes."""
        raise NotImplementedError

    def encode_imu(self, accel, gyro):
        """Convert IMU readings into campaniform-sensilla-style spikes."""
        raise NotImplementedError
