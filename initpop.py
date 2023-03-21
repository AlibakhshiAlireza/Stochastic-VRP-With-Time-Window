from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np
from reader import *
def create_data_model(instance):
    """Stores the data for the problem."""
    data = {}
    data['time_matrix'] = np.loadtxt("Problem/"+instance+"I.txt",dtype=int,delimiter=",")
    a = reader(instance)
    data['time_windows'] = []
    for i in a[2]:
        data['time_windows'].append((a[2][i][0],a[2][i][1]))
    data['num_vehicles'] = a[0]
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution,instance):
    """Prints solution on console."""
    time_dimension = routing.GetDimensionOrDie('Time')
    total_time = 0
    with open('initsols/'+instance+'SAVINGS.txt', 'w') as f:
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = ""
            while not routing.IsEnd(index):
                time_var = time_dimension.CumulVar(index)
                plan_output += '{0}-'.format(
                    manager.IndexToNode(index), solution.Min(time_var),
                    solution.Max(time_var))
                index = solution.Value(routing.NextVar(index))
            time_var = time_dimension.CumulVar(index)
            plan_output += '{0}'.format(manager.IndexToNode(index),
                                                        solution.Min(time_var),
                                                        solution.Max(time_var))
            if plan_output == "0-0":
                pass
            else:
                f.write(plan_output[2:-1])
            total_time += solution.Min(time_var)
    with open('initsols/'+instance+'SAVINGS.txt', 'r') as f:
        temp = f.read()
        temp = temp[:-1]
    with open('initsols/'+instance+'SAVINGS.txt', 'w') as f:
        f.write(temp)
    


def main(instance):
    """Solve the VRP with time windows."""
    # Instantiate the data problem.
    data = create_data_model(instance)

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['time_matrix']),data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def time_callback(from_index, to_index):
        """Returns the travel time between the two nodes."""
        # Convert from routing variable Index to time matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['time_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Time Windows constraint.
    time = 'Time'
    routing.AddDimension(
        transit_callback_index,
        30000,  # allow waiting time
        30000,  # maximum time per vehicle
        False,  # Don't force start cumul to zero.
        time)
    time_dimension = routing.GetDimensionOrDie(time)
    # Add time window constraints for each location except depot.
    for location_idx, time_window in enumerate(data['time_windows']):
        if location_idx == data['depot']:
            continue
        index = manager.NodeToIndex(location_idx)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    # Add time window constraints for each vehicle start node.
    depot_idx = data['depot']
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        time_dimension.CumulVar(index).SetRange(
            data['time_windows'][depot_idx][0],
            data['time_windows'][depot_idx][1])

    # Instantiate route start and end times to produce feasible times.
    for i in range(data['num_vehicles']):
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(
            time_dimension.CumulVar(routing.End(i)))

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.SAVINGS)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution,instance)
    with open('initsols/'+instance+'SAVINGS.txt', 'r') as f:
        temp = f.read()
        a = temp.split('-')
    p = [int(x) for x in a]
    return p

if __name__ == '__main__':
    main(instance='C7')
    a = np.loadtxt("initsols/C7SAVINGS.txt",dtype=int,delimiter="-")
    print(len(a))
