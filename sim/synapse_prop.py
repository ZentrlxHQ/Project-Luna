"""
sim/synapse_prop.py
Spike propagation across the connectome's synaptic weight matrix.
"""


class SynapsePropagator:
    def __init__(self, synapse_graph):
        self.graph = synapse_graph

    def step(self, spikes):
        """Given a set of firing neuron IDs, return downstream spike
        contributions for the next tick."""
        raise NotImplementedError
