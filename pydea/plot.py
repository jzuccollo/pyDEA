# Useful plot types.

import matplotlib.pyplot as plt
import seaborn as sns


def dist_small_multiples(df, figsize=(20, 20)):
    """
    Small multiples plots of the distribution of a dataframe's variables.
    """
    import math

    sns.set_style("white")

    num_plots = len(df.columns)
    n = int(math.ceil(math.sqrt(num_plots)))

    fig = plt.figure(figsize=figsize)
    axes = [plt.subplot(n, n, i) for i in range(1, num_plots + 1)]

    i = 0
    for k, v in df.iteritems():
        ax = axes[i]
        sns.kdeplot(v, shade=True, ax=ax, legend=False)
        sns.rugplot(v, ax=ax, c=sns.color_palette("husl", 3)[0])
        [label.set_visible(False) for label in ax.get_yticklabels()]
        ax.xaxis.set_ticks([v.min(), v.max()])
        ax.set_title(k)
        i += 1
    sns.despine(left=True, trim=True, fig=fig)
    plt.tight_layout()
    return fig, axes


def size_plot(df, figsize=(15, 6)):
    """
    Violin plot of the magnitude of the variables.
    """

    fig, axs = plt.subplots(figsize=figsize)

    med = df.median()
    med.sort(ascending=False)
    sns.violinplot(df[med.index], ax=axs, color="coolwarm_r")
    axs.set_xlabel("Expenditure")
    axs.set_title("Distribution by column")
    sns.despine(offset=10, ax=axs)
    plt.xticks(rotation=45, ha='right')
    return fig, axs
