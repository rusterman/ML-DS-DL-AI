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
'''
plt.subplots - First, it creates a "figure" with dimensions of 16x8 (16 rows x 8 columns) — let's call it "figure A".
               Then, it places 8 subplots, each measuring 2x4 (2 rows x 4 columns) inside figure A.
               Finally, it returns two objects: "fig" and "axes".
               "fig": The figure itself.
               "axes": An array consisting of the 8 subplots.
               
               fig (16x8):
               ┌─────────────────────────────────┐
               │  axes (2x4):                    │
               │  ┌──────┬──────┬──────┬──────┐  │
               │  │axes00│axes01│axes02│axes03│  │           
               │  ├──────┼──────┼──────┼──────┤  │
               │  │axes10│axes11│axes12│axes13│  │
               │  └──────┴──────┴──────┴──────┘  │ 
               └─────────────────────────────────┘
'''

axes = axes.flatten()
'''
axes - [[axes00, axes01, axes02, axes03],
         axes10, axes11, axes12, axes13]]

axes.flatten() - [axes00, axes01, axes02, axes03, axes10, axes11, axes12, axes13]
'''

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
'''
zip - combines the axes and plots arrays in this way:
      [(axes00, (y_original, "Original: f(x) = x^2")),
       (axes01, (y_shift_up3, "Shift Up 3: f(x) + 3")),
       ...]


for ax, (y, title) - it's actually just tuple unpacking:
                     ax = axesXY  (XY = 00, 01, 02 etc.)
    
    
                     Because each element of "plots" is in the form "(y, title)":
                     y = plotsXY (XY = 00, 10, 20 etc.)
                 title = plotsXY (XY = 01, 11, 21 etc.)
                 
                 
                     Ultimately, taking a single loop as an example, it works as follows:
                     ax = axes00
                     y = y_original
                     title = "Original: f(x) = x^2"


                     ax.plot(x, y): axes00.plot(x, y_original)
                     
                     Matplotlib takes these in pairs and connects the points with a line:
                     x	     y
                     -5.00	 25.00
                     -4.97	 24.75
                     -4.95	 24.50
                     ...	 ...
                     5	     25
                     
                     
                     ax.set_title(title): axes00.plot("Original: f(x) = x^2")
                     ax.set_xlabel("x"): axes00.set_xlabel("x")
                     ax.set_ylabel("y"): axes00.set_ylabel("y")
                     ax.grid(True): axes00.grid(True)
                     
                     
During the loop each subplot (ax) in the axes array is taken and paired with the corresponding (y, title) pair from the plots list.
Then, the y-plot is drawn on that subplot, the title is added, axis labels are set, and the grid is enabled.

NOTE: x does not change. 
      It remains the same throughout the entire loop.
      Only y and title change.
'''

fig.tight_layout()
plt.show()
