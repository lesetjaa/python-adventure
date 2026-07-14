import pandas

data = pandas.read_csv("50_states.csv")

state_coords = {
    row.state: (row.x, row.y)
    for _, row in data.iterrows()
}

print(state_coords)
