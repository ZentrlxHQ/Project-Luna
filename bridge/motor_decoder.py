"""
bridge/motor_decoder.py
Reads motor-neuron spike output from the ventral nerve cord region of
the sim and converts it into servo PWM commands over serial.
"""
import argparse


def run(port: str, channel_map_path: str):
    print(f"Listening for VNC motor spikes, driving servos on {port} "
          f"using channel map {channel_map_path}")
    # TODO: open serial connection, subscribe to motor neuron spike
    # stream, translate to PWM per bridge/channel_map.yaml


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", required=True)
    parser.add_argument("--channel-map", required=True)
    args = parser.parse_args()
    run(args.port, args.channel_map)
