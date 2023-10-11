import pulp

# Create a linear programming problem
lp_problem = pulp.LpProblem("Optimal_Production", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable("Rods", lowBound=0, cat=pulp.LpContinuous)
y = pulp.LpVariable("Screws", lowBound=0, cat=pulp.LpContinuous)
z = pulp.LpVariable("Rotors", lowBound=0, cat=pulp.LpContinuous)
a = pulp.LpVariable("Iron_Plates", lowBound=0, cat=pulp.LpContinuous)
b = pulp.LpVariable("Reinforced_Plates", lowBound=0, cat=pulp.LpContinuous)
y_from_rods = pulp.LpVariable("Screws_from_Rods", lowBound=0, cat=pulp.LpContinuous)
z_from_rods = pulp.LpVariable("Rotors_from_Rods", lowBound=0, cat=pulp.LpContinuous)

# Define the objective function (maximize total value)
lp_problem += 20 * x + 2 * y, "Total_Value"

# Define the constraints
lp_problem += x + y + 23 * z + 30 * a + 60 * b + y_from_rods + z_from_rods <= 120, "Iron_Constraint"
lp_problem += y_from_rods <= 10 * x, "Screws_from_Rods_Constraint"
lp_problem += z_from_rods <= 20 * x, "Rotors_from_Rods_Constraint"

# Solve the linear programming problem
lp_problem.solve()

# Print the results
print("Status:", pulp.LpStatus[lp_problem.status])
print("Rods produced:", x.varValue)
print("Screws produced:", y.varValue)
print("Rotors produced:", z.varValue)
print("Iron Plates produced:", a.varValue)
print("Reinforced Plates produced:", b.varValue)
print("Screws from Rods produced:", y_from_rods.varValue)
print("Rotors from Rods produced:", z_from_rods.varValue)
print("Total Value:", pulp.value(lp_problem.objective))