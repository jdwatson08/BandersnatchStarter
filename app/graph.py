from altair import Chart, Tooltip, themes
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    del df[df.columns[0]]
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}", height=500, width=500, padding=20
    ).mark_point(size=100).encode(x=x,
                                  y=y,
                                  color=target,
                                  tooltip=Tooltip(df.columns.to_list())
                                  )
    themes.enable('dark')
    graph = graph.configure_title(fontSize=24)

    return graph
