with open("input.txt", "r") as file:
    grid = [line.strip() for line in file if line.strip()]



rows = len(grid)
cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

accessible_count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue

        neighbor_rolls = 0

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "@":
                    neighbor_rolls += 1

        if neighbor_rolls < 4:
            accessible_count += 1

print("Accessible rolls of paper:", accessible_count)
