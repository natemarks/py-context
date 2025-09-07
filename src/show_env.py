import sys
import site
import pkg_resources


def print_python_info():
    print(f"Python executable location: {sys.executable}")
    print(f"Python version: {sys.version}")
    print(f"Site-packages location: {site.getsitepackages()[0]}")
    print("Installed packages:")
    for dist in sorted(
        pkg_resources.working_set, key=lambda d: d.project_name.lower()
    ):
        print(f"  {dist.project_name}=={dist.version}")


if __name__ == "__main__":
    print_python_info()
