import operator
import re


def parse_input():
    """Parses the input file to extract wires and gates data."""
    try:
        with open("./Day24/input.txt", "r") as file:
            data = file.read().strip()  # Remove extra spaces or newlines.
    except FileNotFoundError:
        raise FileNotFoundError("The input file 'input.txt' was not found.")
    
    # Splitting wires and gates sections
    wires_section, gates_section = data.split("\n\n")
    
    # Parsing wires as a dictionary of {wire_name: value}
    wires = re.findall(r"(\w\d+): (0|1)", wires_section)
    wires = {wire: int(value) for wire, value in wires}
    
    # Parsing gates as a dictionary of {output_wire: (input1, operation, input2)}
    gates = re.findall(r"(\w+) (AND|OR|XOR) (\w+) -> (\w+)", gates_section)
    gates = {output: (input1, operation, input2) for input1, operation, input2, output in gates}
    
    return wires, gates


def simulate_wires(wires, gates):
    """Simulates the circuit based on wires and gates."""
    OPS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}
    
    while gates:
        resolved = {}
        for output, (input1, op, input2) in gates.items():
            if input1 in wires and input2 in wires:
                wires[output] = OPS[op](wires[input1], wires[input2])
                resolved[output] = (input1, op, input2)
        
        # Remove resolved gates
        for output in resolved:
            gates.pop(output)
    
    return wires


def part_two(gates):
    """Identifies specific wires based on problem criteria."""
    specific_wires = []
    for wire, (input1, op, input2) in gates.items():
        print(f"Gate: {wire}, Inputs: {input1}, {input2}, Operation: {op}")
        if (
            (wire.startswith("z") and op != "XOR" and wire != "z45") or
            (
                op == "XOR" and
                all(not x.startswith(("x", "y", "z")) for x in (input1, input2, wire))
            )
        ):
            specific_wires.append(wire)
    return ",".join(sorted(specific_wires)) if specific_wires else "No matching wires found"




# Main Execution
if __name__ == "__main__":
    try:
        # Parse the input
        wires, gates = parse_input()
        
        # Simulate wires to resolve circuit
        wires = simulate_wires(wires, gates)
        
        # Print the final state of wires for debugging
        print("Final Wires State:", wires)
        
        # Solve Part 2
        result = part_two(gates)
        print(f"Part 2: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
