"""
sim/realtime_scheduler.py
Keeps the spiking simulation on a real-time tick budget (~5ms) so the
sensor -> brain -> motor loop stays closed and responsive.
"""
import argparse
import time


def run(engine: str, target_hz: int):
    tick_budget = 1.0 / target_hz
    print(f"Running {engine} at target {target_hz}Hz "
          f"({tick_budget * 1000:.2f}ms/tick budget)")
    while True:
        start = time.time()
        # TODO: call into sim engine, step connectome, hand off to bridge
        elapsed = time.time() - start
        sleep_for = max(0.0, tick_budget - elapsed)
        time.sleep(sleep_for)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", default="lif_engine.cu")
    parser.add_argument("--target-hz", type=int, default=200)
    args = parser.parse_args()
    run(args.engine, args.target_hz)
