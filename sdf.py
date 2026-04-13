import plotly.graph_objects as go

baseline = 1.45
increased = baseline * 1.10

fig = go.Figure(data=[
    go.Bar(
        x=["Baseline", "10% Increase"],
        y=[baseline, increased],
        marker_color=["steelblue", "darkorange"],
        width=0.4,
    )
])

fig.update_layout(
    title="Sinuosity: 10% Increase",
    xaxis=dict(title=None),
    yaxis=dict(range=[0, increased * 1.15], showgrid=False),
    template="plotly_dark",
)

fig.write_html("index.html")
