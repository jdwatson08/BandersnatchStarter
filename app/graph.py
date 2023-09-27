from altair import Chart, Tooltip, themes
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """This method makes a chart from a data set it is given. It takes as its parameter a dataframe, 2 features from the
    dataframe, and a target to use for comparison.
    """
    del df[df.columns[0]]
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}", height=500, width=500, padding=20
    ).mark_point(size=20).encode(x=x,
                                 y=y,
                                 color=target,
                                 tooltip=Tooltip(df.columns.to_list())
                                 )
    themes.enable('dark')
    graph = graph.configure_title(fontSize=24)

    return graph
