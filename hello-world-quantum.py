from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice


# Create a simple circuit
circuit = Circuit().h(0).measure(0)

# Use local simulator (no cost)
device = LocalSimulator()
# device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")

# Run the circuit
result = device.run(circuit, shots=100).result()

# Print results
print(result.measurement_counts)