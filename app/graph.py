from altair import Chart, Tooltip, themes
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    del df[df.columns[0]]
    graph1 = Chart(
        df,
        title=f"{y} by {x} for {target}", height=400, width=300
    ).mark_point(size=100).encode(x=x,
                                  y=y,
                                  color=target,
                                  tooltip=Tooltip(df.columns.to_list())
                                  )
    themes.enable('dark')

    graph2 = Chart(
        df,
        title=f"{y} by {x} for {target}", height=400, width=300
    ).mark_bar(size=100).encode(x=x,
                                y=y,
                                tooltip=Tooltip(df.columns.to_list())
                                )
    themes.enable('dark')
    con = graph1 | graph2
    return con
