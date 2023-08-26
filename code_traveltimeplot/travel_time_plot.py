import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator


def plot_travel_time_function(from_node, to_node, arc_name, break_points, t1, t2):
    plt.rcParams["font.family"] = "Times New Roman"

    # fig, ax = plt.subplots(figsize=(4, 3), dpi=100, facecolor='w')
    fig, ax = plt.subplots(dpi=100, facecolor='w')

    ax.set_ylim(0, 3.1)
    ax.set_xlim(-0.1, 5)

    ax.set_xlabel("Time", fontsize=10)
    ax.set_ylabel("Travel time", fontsize=10)

    title_text = "paperVer: (" + str(from_node) + "," + str(to_node) + ") / cppCodeVer: (" \
                 + str(from_node - 1) + "," + str(to_node - 1) + ")"

    ax.set_title(title_text)

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.xaxis.set_major_locator(MultipleLocator(1.000))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(1.000))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    ax.xaxis.set_minor_formatter("{x:.2f}")
    ax.yaxis.set_minor_formatter("{x:.2f}")

    ax.tick_params(which="major", width=1.0, length=10, labelsize=14)
    ax.tick_params(which="minor", width=1.0, length=5, labelsize=8, rotation=45,
                   labelcolor='0.25')

    plt.grid(b=True, which='major', axis='both', color='gray', lw=.8)
    plt.grid(b=True, which='minor', axis='both', color='gray', linestyle="--", lw=.5)

    num_of_bps = len(break_points)
    for i, (t, tt) in enumerate(break_points):
        ax.scatter(t, tt, color="r", zorder=10, ec='k', s=8)
        if i != num_of_bps - 1:
            ax.plot([t, break_points[i + 1][0]], [tt, break_points[i + 1][1]], c="blue")

    ax.vlines(t1, 0, 3.1, color="red", linestyles="--", lw=.5)
    ax.vlines(t2, 0, 3.1, color="red", linestyles="--", lw=.5)

    text1 = ".\\travel_time_figures\\" + arc_name + ".pdf"
    text2 = ".\\travel_time_figures\\" + arc_name + ".png"
    plt.savefig(text1, bbox_inches='tight')
    plt.savefig(text2, bbox_inches='tight', dpi=300)

    plt.show()


if __name__ == "__main__":
    # fNode = 1
    # tNode = 2
    # arcName = "arc_1_2"
    # bps = [(0, 1.34), (1, 0.66), (2, 0.14), (3, 0.01), (4, 0.35), (5, 1.00)]
    # t1 = 0
    # t2 = 2.9

    # fNode = 1
    # tNode = 3
    # arcName = "arc_1_3"
    # bps = [(0, 2.85), (1, 2.95), (2, 3), (3, 2.98), (4, 2.90), (5, 2.76)]
    # t1 = 0
    # t2 = 2.9

    # fNode = 2
    # tNode = 3
    # arcName = "arc_2_3"
    # bps = [(0, 1.99), (1, 1.82), (2, 1.51), (3, 1.10), (4, 0.67), (5, 0.30)]
    # t1 = 1.34
    # t2 = 2.92

    # fNode = 2
    # tNode = 4
    # arcName = "arc_2_4"
    # bps = [(0, 1.29), (1, 1.02), (2, 1.63), (3, 2.57), (4, 3), (5, 2.54)]
    # t1 = 1.34
    # t2 = 2.92

    fNode = 3
    tNode = 4
    arcName = "arc_3_4"
    bps = [(0, 0.61), (1, 0.73), (2, 0.83), (5, 1.00)]
    t1 = 1.76
    t2 = 4.05

    plot_travel_time_function(from_node=fNode, to_node=tNode, arc_name=arcName, break_points=bps, t1=t1, t2=t2)
    print("DONE!!")
