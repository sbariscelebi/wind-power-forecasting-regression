import matplotlib.pyplot as plt

def save_plot(fig, title):
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    safe_title = title.replace(' ', '_').replace('-', '_')
    fig.savefig(f"{safe_title}.png", dpi=300)
    fig.savefig(f"{safe_title}.svg", format='svg')
    plt.close(fig)