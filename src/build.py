from pybuilder.core import use_plugin, init, task, depends

use_plugin("python.core")  # Core plugin for Python projects
use_plugin("pytest")  # Pytest plugin for running pytest tests

# Define the project name and version
name = "trisquare"
version = "1.0"

# Specify the project's source directory (where your Python code is located)
default_task = "run_custom_tests"

@init
def set_properties(project):

    # Define source directories
    project.set_property("source_directory", "")

@task
@depends("prepare")
def run_custom_tests(logger):
    logger.info("Running custom tests with pytest on Windows...")
    pytest_command = "pytest"
    logger.info(f"Running command: {pytest_command}")   

    import subprocess
    subprocess.run(pytest_command, shell=True, check=True)


