def barline(x, y1, y2, title=None, y1_lim=None, y2_lim=None, x_label=None, y1_label=None, y2_label=None,
            y1_legend=None, y2_legend=None, export_figure=False, export_path=None, export_name='fig'):
    import matplotlib.pyplot as plt
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(x)), y1, color='C0', label=y1_legend)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(labels=x, rotation=45)
    if type(y1_lim) is tuple:
        ax1.set_ylim(bottom=y1_lim[0], top=y1_lim[1])
    ax2 = ax1.twinx()
    ax2.plot(y2, color='C1', lw=4, label=y2_label)
    ax2.set_ylabel(y2_legend, rotation=270, labelpad=13)
    if type(y2_lim) is tuple:
        ax2.set_ylim(bottom=y2_lim[0], top=y2_lim[1])
    if (type(y1_legend) is str) or (type(y2_legend) is str):
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.title(title)
    if export_figure:
        if export_path == str:
            plt.savefig(export_path + export_name + '.png', dpi=300, bbox_inches='tight')
        else:
            plt.savefig(export_name + '.png', dpi=300, bbox_inches='tight')
    plt.show()
