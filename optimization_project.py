import pulp

# Create a problem instance
model = pulp.LpProblem("Test_Problem", pulp.LpMaximize)

# Decision variables
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

# Objective Function: Maximize 3x + 2y
model += 3 * x + 2 * y, "Profit"

# Constraints
model += x + y <= 10
model += 2 * x + y <= 15

# Solve the problem
model.solve()

# Output results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal x: {x.varValue}")
print(f"Optimal y: {y.varValue}")
print(f"Maximum Profit: {pulp.value(model.objective)}")
