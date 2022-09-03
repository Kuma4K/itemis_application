# Solve a multiple knapsack problem using a MIP solver.
from ortools.linear_solver import pywraplp
import utils


def main():
    topic, time = utils.manipulated_input()
    data = {}
    data['time'] = time
    data['topic'] = topic
    assert len(data['time']) == len(data['topic'])
    data['num_items'] = len(data['time'])
    data['all_items'] = range(data['num_items'])

    data['bin_capacities'] = [180, 240, 180, 240]
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
            timestamp_in_min = 0
            if b == 0:
                print(f'> Track 1:')
                timestamp_in_min = 540
            elif b == 2:
                print(f'>\n> Track 2:')
                timestamp_in_min = 540
            elif b == 1 or 3:
                print(f'> 12:00PM Lunch')
                timestamp_in_min = 780
            bin_time = 0
            for i in data['all_items']:
                if x[i, b].solution_value() > 0:
                    print(
                        f"> {utils.ts_to_str(timestamp_in_min)} {data['topic'][i]}"
                    )
                    timestamp_in_min = utils.get_timestamp(timestamp_in_min, data['time'][i])
                    bin_time += data['time'][i]
            if b == 1 or 3:
                print(f'> {utils.ts_to_str(timestamp_in_min)} Networking Event')
            total_time += bin_time
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()
