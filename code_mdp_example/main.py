import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import time

plt.rcParams["font.family"] = "Times New Roman"


class ABSPT:
    def __init__(self, times, color):
        self.nodes = [0, 1, 2, 3]
        self.times = times
        self.color = color
        self.first = [0, 1, 2, 0, 1]
        self.second = [1, 3, 3, 2, 2]


def plot(abspt_list, file_name):
    fig, ax = plt.subplots(figsize=(20, 7), facecolor="w")

    # https://www.pythonpool.com/matplotlib-aspect-ratio/
    axes = plt.gca()
    axes.set_aspect(0.6)

    ax.xaxis.set_major_locator(MultipleLocator(1.000))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(1.000))
    # ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.xaxis.set_minor_formatter("{x:.1f}")

    ax.tick_params(which='major', width=1.0, length=10, labelsize=10)
    ax.tick_params(which='minor', width=1.0, length=5, labelsize=7,
                   labelcolor='0.25')

    plt.tick_params(axis='x', which='major',
                    labelsize=10, labelbottom=True,
                    bottom=True, top=True, labeltop=True)
    plt.tick_params(axis='x', which='minor',
                    labelsize=10, labelbottom=True,
                    bottom=True, top=True, labeltop=True)

    ax.grid(linestyle="-", linewidth=.6, color='gray', zorder=-10, which="major")
    ax.grid(linestyle="-.", linewidth=.5, color='gray', zorder=-10, which="minor")

    ax.set_xlim(-0.1, 5.2)
    ax.set_ylim(-0.1, 3.2)

    # ax.spines.left.set_position(("outward", 5))
    # ax.spines.bottom.set_position(("outward", 5))
    # ax.spines.right.set_position(("outward", 5))
    # ax.spines.top.set_position(("outward", 5))

    ax.set_xlabel("Time", fontsize=10, fontfamily="Times New Roman")
    ax.set_ylabel("Node", fontsize=10, fontfamily="Times New Roman")

    # PLOTTING
    for abspt in abspt_list:
        for x, y in zip(abspt.times, abspt.nodes):
            ax.scatter(x, y, color=abspt.color, zorder=10)
        for f, s in zip(abspt.first, abspt.second):
            x = abspt.times[f]
            y = abspt.nodes[f]
            dx = abspt.times[s] - x
            dy = abspt.nodes[s] - y
            ax.arrow(x=x, y=y, dx=dx, dy=dy, head_width=0.05, head_length=0.05, color=abspt.color,
                     length_includes_head=True, zorder=10)

    plt.tight_layout()

    # plt.savefig("fig.png", bbox_inches='tight', dpi=100)
    file_name1 = file_name + ".svg"
    plt.savefig(file_name1, bbox_inches='tight')

    file_name2 = file_name + ".pdf"
    plt.savefig(file_name2, bbox_inches='tight')


if __name__ == "__main__":
    st = time.time()

    abspt_2_5674 = ABSPT(times=[0, 1.34, 1.761273, 2.5674], color="blue")
    abspt_2_83 = ABSPT(times=[0.509705, 1.503106, 2, 2.83], color="green")
    abspt_3_0826 = ABSPT(times=[1, 1.66, 2.239054, 3.0826], color="#ffd1ff")
    abspt_3_63 = ABSPT(times=[1.708333, 2, 2.757098, 3.63], color="orange")
    abspt_3_886667 = ABSPT(times=[1.983964, 2.132303, 3, 3.886667], color="red")
    abspt_3_9016 = ABSPT(times=[2, 2.14, 3.013481, 3.9016], color="black")
    abspt_4_994333 = ABSPT(times=[2.793688, 2.830508, 4, 4.994333], color="red")
    abspt_5 = ABSPT(times=[2.804665, 2.840059, 4.005635, 5], color="#00ffff")

    # ITERATION 1
    file_name = "fig1"
    abspt_list = [abspt_2_5674, abspt_5]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 2
    file_name = "fig2"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 3
    file_name = "fig3"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 4
    file_name = "fig4"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 5
    file_name = "fig5"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 6
    file_name = "fig6"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63, abspt_3_886667]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 7
    file_name = "fig7"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63, abspt_3_886667]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 8
    file_name = "fig8"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63, abspt_3_886667, abspt_4_994333]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 9
    file_name = "fig9"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63, abspt_3_886667, abspt_4_994333]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 10
    file_name = "fig10"
    abspt_list = [abspt_2_5674, abspt_5, abspt_3_0826, abspt_3_9016, abspt_3_63, abspt_3_886667, abspt_4_994333,
                  abspt_2_83]
    plot(abspt_list=abspt_list, file_name=file_name)

    # ITERATION 11
    file_name = "fig11"
    abspt_list = [abspt_2_5674,
                  abspt_2_83,
                  abspt_3_0826,
                  abspt_3_63,
                  abspt_3_886667,
                  abspt_3_9016,
                  abspt_4_994333,
                  abspt_5]
    plot(abspt_list=abspt_list, file_name=file_name)

    print(f"Elapsed time = {time.time() - st} sec.")

# abspt_2_5674
# abspt_2_83
# abspt_3_0826
# abspt_3_63
# abspt_3_886667
# abspt_3_9016
# abspt_4_994333
# abspt_5
