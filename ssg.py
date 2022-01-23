import typer
from ssg.site import Site
import ssg


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest,"parsers":[ssg.parsers.ResourceParser()]}
    Site(**config).build()


typer.run(main)