# Solve a multiple knapsack problem using a MIP solver.
from ortools.linear_solver import pywraplp
import input_conv


def get_data():
    data1 = input_conv.prepare_input()
    print(data1)


def get_data1():
    topic, time = input_conv.manipulated_input()
    if len(topic) == len(time):
        print(topic)
        print(time)


def main():
    topic, time = input_conv.manipulated_input()
    data = {}
    data['time'] = time
    data['topic'] = topic
    assert len(data['time']) == len(data['topic'])
    data['num_items'] = len(data['time'])
    data['all_items'] = range(data['num_items'])

    data['bin_capacities'] = [36, 48, 36, 48]
    data['num_bins'] = len(data['bin_capacities'])
    data['all_bins'] = range(data['num_bins'])

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if solver is None:
        print('SCIP solver unavailable.')
        return

    # Variables.
    # x[i, b] = 1 if item i is packed in bin b.
    x = {}
    for i in data['all_items']:
        for b in data['all_bins']:
            x[i, b] = solver.BoolVar(f'x_{i}_{b}')

    # Constraints.
    # Each item is assigned to at most one bin.
    for i in data['all_items']:
        solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)

    # The amount packed in each bin cannot exceed its capacity.
    for b in data['all_bins']:
        solver.Add(
            sum(x[i, b] * data['time'][i]
                for i in data['all_items']) <= data['bin_capacities'][b])

    # Objective.
    # Maximize total value of packed items.
    objective = solver.Objective()
    for i in data['all_items']:
        for b in data['all_bins']:
            objective.SetCoefficient(x[i, b], data['time'][i])
    objective.SetMaximization()

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        total_time = 0
        for b in data['all_bins']:
            if b == 0:
                print(f'Track 1 - morning')
            elif b == 1:
                print(f'Track 1 - afternoon ')
            elif b == 2:
                print(f'Track 2 - morning')
            elif b == 3:
                print(f'Track 2 - afternoon')
            bin_time = 0
            for i in data['all_items']:
                if x[i, b].solution_value() > 0:
                    print(
                        f"Talk {i+1} time: {input_conv.conv_lightning_to_min(data['time'][i])} Topic: {data['topic'][i]}"
                    )
                    bin_time += data['time'][i]
            print(f'Track time: {input_conv.conv_lightning_to_min(bin_time)}\n')
            total_time += bin_time
        print(f'Total time of this Track: {input_conv.conv_lightning_to_min(total_time)}')
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
    # get_data()
    # get_data1()
