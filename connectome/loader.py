"""
connectome/loader.py
Loads the MaleCNS v1.0 connectome dataset (neurons + synapses) into an
in-memory graph the sim engine can consume.

The dataset itself is NOT bundled in this repo -- fetch it from the
Janelia / FlyWire connectomics resources and point --path at it.
"""
import argparse


def fetch(dataset_name: str, out_path: str = "connectome/malecns_v1.h5"):
    raise NotImplementedError(
        "Stub loader. Point this at the published MaleCNS v1.0 release "
        "and implement the fetch/parse logic for your data source."
    )


def load_graph(path: str):
    """Return (neurons, synapses) parsed from the connectome file."""
    raise NotImplementedError("Implement graph parsing for your data format.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", type=str, help="dataset name to fetch")
    parser.add_argument("--path", type=str, default="connectome/malecns_v1.h5")
    args = parser.parse_args()
    if args.fetch:
        fetch(args.fetch, args.path)
