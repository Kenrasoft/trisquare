from pybuilder.core import use_plugin, init, task, depends
from pybuilder.plugins.python.coverage_plugin import coverage
from subprocess import check_call

use_plugin("python.core")  # Core plugin for Python projects
use_plugin("pytest")  # Pytest plugin for running pytest tests
use_plugin("python.coverage")

min_coverage = 80
# Define the project name and version
name = "trisquare"
version = "1.0"

# Specify the project's source directory (where your Python code is located)
default_task = "run_custom_tests","run_tests_with_coverage"

@init
def initialize(project):
    # Configure your project settings
    pass

@init
def set_properties(project):

    # Define source directories
    project.set_property("source_directory", "")

@task
@depends("prepare")
def run_custom_tests(logger):
    logger.info("Running custom tests with pytest...")
    pytest_command = "pytest"
    logger.info(f"Running command: {pytest_command}")   

    import subprocess
    subprocess.run(pytest_command, shell=True, check=True)


@task
@depends("prepare")
def run_tests_with_coverage(project,logger):
    # Configure the coverage settings
    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", min_coverage)
    project.set_property("coverage_branch_threshold_warn", min_coverage)
    project.set_property("coverage_allow_non_imported_modules", False)

# @task
# @depends("prepare")
# def build_docs(project, logger):
#     logger.info("Building documentation...")
#     try:
#         check_call(["sphinx-build", "-b", "html", "docs", "docs/build"])
#         logger.info("Documentation built successfully.")
#     except Exception as e:
#         logger.error(f"Failed to build documentation: {str(e)}")
#         exit(1)