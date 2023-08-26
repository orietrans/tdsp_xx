import time
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

plt.rcParams["font.family"] = "Times New Roman"


def plot_ordinary_travel_time_function(travel_times, file_name):
    # make the drawing panel
    fig, ax = plt.subplots(figsize=(7, 7), facecolor="w")

    # drawing panel configuration
    ax.xaxis.set_major_locator(MultipleLocator(1.000))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(1.000))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_formatter("{x:.2f}")
    ax.yaxis.set_minor_formatter("{x:.2f}")

    ax.tick_params(which='major', width=1.0, length=10, labelsize=10)
    ax.tick_params(which='minor', axis="x", width=1.0, length=5, labelsize=5,
                   labelcolor='0.25', rotation=90, top=True, labeltop=True)
    ax.tick_params(which='minor', axis="y", width=1.0, length=5, labelsize=5,
                   labelcolor='0.25')
    ax.tick_params(which="major", axis="x", top=True, labeltop=True)

    # ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

    ax.grid(which="major", linestyle="-", linewidth=.8, color='gray', zorder=-10)
    ax.grid(which="minor", linestyle="--", linewidth=.4, color='gray', zorder=-10)

    ax.plot(1, 1)

    ax.set_xlim(-0.05, 5.05)
    ax.set_ylim(-0.05, 5.05)

    ax.set_xlabel("departing time", fontsize=10)
    ax.set_ylabel("travel time duration", fontsize=10)

    # Start PLOTTING now!
    for i, t in enumerate(travel_times):
        ax.scatter(i, t, color="black", zorder=10, s=1)
        if i == len(travel_times) - 1:
            continue
        else:
            ax.plot([i, i + 1], [t, travel_times[i + 1]],
                    color="black", zorder=10, lw=.5)

    plt.savefig(file_name,
                bbox_inches='tight')


def plot_reversed_travel_time_function(travel_times, file_name):
    # make the drawing panel
    fig, ax = plt.subplots(figsize=(7, 7), facecolor="w")

    # drawing panel configuration
    ax.xaxis.set_major_locator(MultipleLocator(1.000))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(1.000))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_formatter("{x:.2f}")
    ax.yaxis.set_minor_formatter("{x:.2f}")

    ax.tick_params(which='major', width=1.0, length=10, labelsize=10)
    ax.tick_params(which='minor', axis="x", width=1.0, length=5, labelsize=5,
                   labelcolor='0.25', rotation=90, top=True, labeltop=True)
    ax.tick_params(which='minor', axis="y", width=1.0, length=5, labelsize=5,
                   labelcolor='0.25')
    ax.tick_params(which="major", axis="x", top=True, labeltop=True)

    # ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

    ax.grid(which="major", linestyle="-", linewidth=.8, color='gray', zorder=-10)
    ax.grid(which="minor", linestyle="--", linewidth=.4, color='gray', zorder=-10)

    ax.plot(1, 1)

    # ax.set_xlim(-0.05, 5.05)
    ax.set_xlim(1, 6.2)
    ax.set_ylim(-0.05, 5.05)

    ax.set_xlabel("arrival time", fontsize=10)
    ax.set_ylabel("travel time duration", fontsize=10)

    # Start PLOTTING now!
    arrival_times = [i + j for i, j in enumerate(travel_times)]

    for i in range(len(arrival_times)):
        ax.scatter(arrival_times[i], travel_times[i], color="black",
                   zorder=10, s=1)
        if i == len(arrival_times) - 1:
            continue
        else:
            ax.plot([arrival_times[i], arrival_times[i + 1]],
                    [travel_times[i], travel_times[i + 1]],
                    color="black", zorder=10, lw=.5)

    # for i, t in enumerate(travel_times):
    #     ax.scatter(i, t, color="black", zorder=10, s=1)
    #     if i == len(travel_times) - 1:
    #         continue
    #     else:
    #         ax.plot([i, i + 1], [t, travel_times[i + 1]],
    #                 color="black", zorder=10, lw=.5)

    plt.savefig(file_name,
                bbox_inches='tight')


if __name__ == "__main__":
    st = time.time()

    # I just feel that we really need to visualize how to obtain
    # reversed travel time function value
    # So, normally, the link travel time function takes departing time instant
    # as the input argument, and generates travel time duration as the output value
    # But in the backward shortest path finding process, we need to
    # find travel time duration given arrival time rather than departing time
    # In this code, I will do my best to show how to do it...

    travel_times = [1.34, 0.66, 0.14, 0.01, 0.35, 1]
    # file_name = "o1_ordinary_travel_Time_function.pdf"
    file_name = "o1_ordinary_travel_Time_function.svg"
    plot_ordinary_travel_time_function(travel_times=travel_times,
                                       file_name=file_name)

    # file_name = "o2_reversed_travel_Time_function.pdf"
    file_name = "o2_reversed_travel_Time_function.svg"
    plot_reversed_travel_time_function(travel_times=travel_times,
                                       file_name=file_name)

    print(f"Elapsed time = {time.time() - st} sec.")
