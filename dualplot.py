# Import pyplot
import matplotlib.pyplot as plt

# Function to plot a line chart on each of the two y-axes
def line_line(x, y1, y2, color_1='C0', color_2='C1', title=None,
              x_label=None, y1_label=None, y2_label=None,
              y1_legend=None, y2_legend=None, y1_lim=None, y2_lim=None,
              export_figure=False, export_as='fig.png'):
    fig, ax1 = plt.subplots()
    ax1.plot(range(len(x)), y1, color=color_1, lw=3, label=y1_legend)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(labels=x, rotation=45)
    if type(y1_lim) is tuple:
        ax1.set_ylim(bottom=y1_lim[0], top=y1_lim[1])
    ax2 = ax1.twinx()
    ax2.plot(y2, color=color_2, lw=3, label=y2_legend)
    ax2.set_ylabel(y2_label, rotation=270, labelpad=13)
    if type(y2_lim) is tuple:
        ax2.set_ylim(bottom=y2_lim[0], top=y2_lim[1])
    if (type(y1_legend) is str) or (type(y2_legend) is str):
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.title(title)
    if export_figure:
      plt.savefig(export_as, dpi=300, bbox_inches='tight')
    plt.show()

# Function to plot a bar chart on the primary y-axis and a line chart on the secondary y-axis
def bar_line(x, y1, y2, color_1='C0', color_2='C1', title=None,
             x_label=None, y1_label=None, y2_label=None,
             y1_legend=None, y2_legend=None, y1_lim=None, y2_lim=None,
             export_figure=False, export_as='fig.png'):
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(x)), y1, color='C0', label=y1_legend)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(labels=x, rotation=45)
    if type(y1_lim) is tuple:
        ax1.set_ylim(bottom=y1_lim[0], top=y1_lim[1])
    ax2 = ax1.twinx()
    ax2.plot(y2, color='C1', lw=3, label=y2_legend)
    ax2.set_ylabel(y2_label, rotation=270, labelpad=13)
    if type(y2_lim) is tuple:
        ax2.set_ylim(bottom=y2_lim[0], top=y2_lim[1])
    if (type(y1_legend) is str) or (type(y2_legend) is str):
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.title(title)
    if export_figure:
        plt.savefig(export_as, dpi=300, bbox_inches='tight')
    plt.show()
