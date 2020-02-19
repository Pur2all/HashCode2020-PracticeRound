import time


def solve(max_slices, different_type, pizzas_info):
    solution = (0, 0)
    pizza_with_max_slices_value = max(pizzas_info.values())
    combination_lower_bound = max_slices // pizza_with_max_slices_value
    pizzas_list = list(pizzas_info.keys())

    for i in range(len(pizzas_list)-1, combination_lower_bound, -1):
        current_sum = 0
        current_solution_list = []

        for j in range(i, -1, -1):
            current_pizza = pizzas_list[j]
            current_sum += pizzas_info[current_pizza]
        
            if current_sum == max_slices:
                return current_solution_list + [current_pizza]

            if current_sum < max_slices:
                current_solution_list += [current_pizza]
                if solution[1] < current_sum:
                    solution = current_solution_list, current_sum
            else:
                current_sum -= pizzas_info[current_pizza]

    return solution[0]


def process(input_file_name):
    with open(input_file_name) as input_file:
        file_lines = input_file.read().splitlines()
        max_slices, different_type = [int(x) for x in file_lines[0].split()]
        pizzas = {pizza: int(slices) for pizza, slices in enumerate(file_lines[1].split())}

    solution = solve(max_slices, different_type, pizzas)

    output_file_name = input_file_name.replace(".in", ".out").replace("input", "output")
    with open(output_file_name, "w") as output_file:
        output_file.write(str(len(solution)) + "\n")
        output_file.write(" ".join(str(pizza) for pizza in sorted(solution)))


input_files = ["input\\" + name + ".in" for name in ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]]

init_time = time.time()

for input_file in input_files:
    start_time = time.time()
    process(input_file)
    print(f"{input_file} processed in {time.time() - start_time} seconds")

print(f"All files processed in {time.time() - init_time} seconds")
