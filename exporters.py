from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.exporter.zipkin.json import ZipkinExporter
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

CONSOLE = "console"
JAEGER = "jaeger"
ZIPKIN = "zipkin"

EXPORTERS = (CONSOLE, JAEGER, ZIPKIN)


class Exporter:
    exporters = dict()

    def __init__(self):
        exporters = {
            CONSOLE: self._get_console_exporter(),
            JAEGER: self._get_jaeger_exporter(),
            ZIPKIN: self._get_zipkin_exporter(),
        }
        self.exporters.update(exporters)

    def get_exporter(self, exporter=CONSOLE):
        return self.exporters.get(exporter, CONSOLE)

    def _get_console_exporter(self):
        # Create ConsoleSpanExporter
        console_exporter = ConsoleSpanExporter()
        return console_exporter

    def _get_jaeger_exporter(self):
        # Create JaegerExporter
        jaeger_exporter = JaegerExporter(
            # configure agent
            agent_host_name="localhost",
            agent_port=6831,
            # optional: configure also collector
            # collector_endpoint='http://localhost:14268/api/traces?format=jaeger.thrift',
            # username=xxxx, # optional
            # password=xxxx, # optional
            # max_tag_value_length=None # optional
        )
        return jaeger_exporter

    def _get_zipkin_exporter(self):
        # Create a ZipkinExporter
        zipkin_exporter = ZipkinExporter(
            # version=Protocol.V2
            # optional:
            # endpoint="http://localhost:9411/api/v2/spans",
            # local_node_ipv4="192.168.0.1",
            # local_node_ipv6="2001:db8::c001",
            # local_node_port=31313,
            # max_tag_value_length=256
            # timeout=5 (in seconds)
        )
        return zipkin_exporter
