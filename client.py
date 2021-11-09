import requests

from tracer import get_tracer

if __name__ == "__main__":
    tracer = get_tracer()

    with tracer.start_as_current_span("client") as spanmain:
        spanmain.set_attribute("name", "client")

        with tracer.start_as_current_span("client-server") as span:
            span.set_attribute("name", "client-server")
            requested = requests.get(
                "http://localhost:8000/currencies/usd",
            )

            assert requested.status_code == 200
