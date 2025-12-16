# ================================
# LOAD INPUT FROM input.txt
# ================================

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file if line.strip()]

rows = len(grid)
cols = len(grid[0])

# 8 directions (including diagonals)
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

total_removed = 0

# ================================
# REPEAT UNTIL NOTHING CAN BE REMOVED
# ================================

while True:
    to_remove = []

    # Step 1: find all accessible rolls
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
                to_remove.append((r, c))

    # Step 2: stop if nothing can be removed
    if not to_remove:
        break

    # Step 3: remove them
    for r, c in to_remove:
        grid[r][c] = "."

    total_removed += len(to_remove)

# ================================
# FINAL ANSWER
# ================================

print("Total rolls of paper removed:", total_removed)
