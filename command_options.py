import argparse

from exporters import EXPORTERS


def get_cmd_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--exporter",
        help="Exporter to use. [console, jaeger, zipkin]",
        default="console",
    )

    args, unknown = parser.parse_known_args()

    if len(unknown) > 0:
        parser.print_help()
        exit()

    if not args.exporter in EXPORTERS:
        parser.print_help()
        exit()

    return args
