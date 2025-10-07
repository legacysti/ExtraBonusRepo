from fasthtml.common import *

app = FastHTML()
rt = app.route


@rt("/")
def home():
    return Main(
        Div(
            Button("Click me", onclick="alert('Hello, there, everyone!')"),
            style="background:#F54927;display:grid;place-items:center;min-height:40vh",
        )
    )


serve()
