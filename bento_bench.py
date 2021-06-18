import matplotlib.pyplot as plt

def parse_elapsed_secs(s):
	secs = 0.0
	secs += float(s.split(":")[0]) * 60
	secs += float(s.split(":")[1].split(".")[0])
	secs += float("0." + s.split(":")[1].split(".")[1])
	return secs

def bar_plot(ax, data, l, yerr=None, colors=None, total_width=0.8, single_width=1):
    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            yerrr = None
            if yerr is not None:
                yerrr = yerr[name][x]
            bar = ax.bar(x + x_offset, y, yerr=yerrr, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])
    
    if l is not None:
        ax.legend(bars, l)