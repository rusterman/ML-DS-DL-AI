import numpy as np
import matplotlib.pyplot as plt


# 1) Define base function f(x) = x^2
def f(x):
    """Compute x squared."""
    return x ** 2


# 2) Create domain of x values
x = np.linspace(-5, 5, 400)
print("x: ", x)

# 3) Compute transformed functions with explanatory comments
y_original = f(x)  # Original function
y_shift_up3 = f(x) + 3  # Shift up by 3 units
y_shift_right2 = f(x - 2)  # Shift right by 2 units
y_vert_stretch_1_5 = 1.5 * f(x)  # Vertical stretch by factor of 1.5
y_horiz_compress_2 = f(2 * x)  # Horizontal compression by factor of 2
y_reflect_x = -f(x)  # Reflection across x-axis
y_reflect_y = f(-x)  # Reflection across y-axis
y_combined = 2 * f(x + 1) + 1  # Combined: vertical scale 2, shift left 1, up 1

# 4) Purpose: Build a figure containing a 2×4 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
axes = axes.flatten()

plots = [
    (y_original, "Original: f(x) = x^2"),
    (y_shift_up3, "Shift Up 3: f(x) + 3"),
    (y_shift_right2, "Shift Right 2: f(x - 2)"),
    (y_vert_stretch_1_5, "Vertical Stretch 1.5: 1.5·f(x)"),
    (y_horiz_compress_2, "Horizontal Compress 2: f(2x)"),
    (y_reflect_x, "Reflect X-axis: -f(x)"),
    (y_reflect_y, "Reflect Y-axis: f(-x)"),
    (y_combined, "Combined: 2·f(x + 1) + 1")
]

for ax, (y, title) in zip(axes, plots):
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)

fig.tight_layout()
plt.show()
