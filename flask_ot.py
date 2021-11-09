from flask_app import app
from opentelemetry.instrumentation.flask import FlaskInstrumentor

from tracer import get_tracer


def request_hook(span, environ):
    if span and span.is_recording():
        span.set_attribute("custom_environ", str(environ))


def response_hook(span, status, response_headers):
    if span and span.is_recording():
        span.set_attribute("custom_response_headers", str(response_headers))
        span.set_attribute("custom_response_status", str(status))


excluded_urls = "currencies/inr/.*,currencies/.*/inr"  # comma delimited regex

FlaskInstrumentor().instrument_app(
    app,
    request_hook=request_hook,
    response_hook=response_hook,
    excluded_urls=excluded_urls,
)


if __name__ == "__main__":
    tracer = get_tracer()

    app.run(port=8000)
