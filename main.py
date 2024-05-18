import salabim as sim
import numpy as np

# Ensure the environment is not in yieldless mode
sim.yieldless(False)

# Distribution parameters (examples, adjust as needed)
monthly_order_arrival_rate = 100  # average number of orders per month

# Materials and their processing profiles
material_profiles = {
    'ND-22m': {'profile': '143.xxx', 'speed': 22},
    'FX-20m': {'profile': '18.xx', 'speed': 20},
    'FX-16m': {'profile': '37.xxx', 'speed': 16}
}

# Correct probabilities for the materials
order_types_prob = [0.5, 0.3, 0.2]  # Adjust the probabilities to match the materials

# Mapping of materials to machines
material_to_machine = {
    'ND-22m': ['104', '105'],
    'FX-20m': ['104', '105'],
    'FX-16m': ['105']  # This material can only be processed on machine 105
}


def interarrival_time():
    # Generate interarrival times based on a monthly rate
    # Convert monthly rate to an hourly rate (assuming 30 days in a month, 24 hours per day)
    hourly_rate = monthly_order_arrival_rate / (30 * 24)
    return np.random.exponential(1 / hourly_rate)


class OrderGenerator(sim.Component):
    def process(self):
        while True:
            Order()
            yield self.hold(interarrival_time())


class Order(sim.Component):
    orders_queue = None  # Initialize orders_queue as None

    def setup(self):
        if Order.orders_queue is None:  # Create the queue when the first order is created
            Order.orders_queue = sim.Queue('orders_queue')
        self.material = np.random.choice(list(material_profiles.keys()), p=order_types_prob)
        self.profile = material_profiles[self.material]['profile']
        print(f"Order created: Material - {self.material}, Profile - {self.profile}")
        Order.orders_queue.add(self)  # Add the order to the queue


    def process(self):
        while True:
            if len(Order.orders_queue) == 0:
                yield self.passivate()  # If the queue is empty, passivate the order

            # Select the appropriate machine
            for machine_name in ['104', '105']:
                if machine_name in material_to_machine[self.material] and env.machines[machine_name].is_free():
                    machine = env.machines[machine_name]  # Get the machine object
                    break
            else:
                yield self.passivate()  # If no machine is free, passivate the order

            Order.orders_queue.remove(self)  # Remove the order from the queue

            # Request the machine for processing
            yield self.request(machine)

            # Adjust processing speed based on the machine
            speed = material_profiles[self.material]['speed']
            if machine_name == '104':
                speed *= 2  # Double the speed for machine 104

            # Calculate and hold processing time
            processing_time_value = np.random.normal(10, 2) * (1 / speed)
            yield self.hold(processing_time_value)

            # Release the machine after processing
            self.release(machine)
            machine.products_made += 1

            yield self.passivate()  # Passivate the order after processing



class Machine(sim.Resource):
    def __init__(self, machine_name, capacity):
        super().__init__(capacity=capacity)
        self.machine_name = machine_name
        self.products_made = 0  # Track the number of products made by this machine

    def is_free(self):
        return len(self.requesters()) == 0


# Set up the environment
env = sim.Environment(trace=True)

# Create machines
env.machines = {
    '104': Machine(machine_name='104', capacity=1),
    '105': Machine(machine_name='105', capacity=1)
}

# Create the order generator
OrderGenerator()

# Run the simulation
env.run(till=1000)  # Run for 1000 time units

# Output statistics
for order in Order.orders_queue:
    print(f"Order Material: {order.material}, Profile: {order.profile}")


for machine_name, machine in env.machines.items():
    print(f"Machine {machine_name} produced {machine.products_made} products.")
