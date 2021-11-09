from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from command_options import get_cmd_options
from ot_exporters import Exporter


def get_tracer():
    cmd_options = get_cmd_options()
    EXPORTER = cmd_options.exporter

    trace.set_tracer_provider(
        TracerProvider(resource=Resource.create({"service.name": "service-flask"}))
    )

    tracer_provider = trace.get_tracer_provider()

    exporter = Exporter()

    tracer_provider.add_span_processor(
        BatchSpanProcessor(exporter.get_exporter(EXPORTER))
    )

    tracer = trace.get_tracer(__name__)

    return tracer
