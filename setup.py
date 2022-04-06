import platform
from pathlib import Path

from setuptools import (find_packages,
                        setup)

import {{project}}

project_base_url = 'https://github.com/{{github_login}}/{{project}}/'


def read_file(path_string: str) -> str:
    return Path(path_string).read_text(encoding='utf-8')


parameters = dict(
        name={{project}}.__name__,
        packages=find_packages(exclude=('tests', 'tests.*')),
        version={{project}}.__version__,
        description={{project}}.__doc__,
        long_description=read_file('README.md'),
        long_description_content_type='text/markdown',
        author='{{full_name}}',
        author_email='{{email}}',
        license='{{license}}',
        classifiers=[
            '{{license_classifier}}',
{% for minor in range(min_python_version.split(".")[1] | int, (max_python_version.split(".")[1]) | int + 1) %}
            'Programming Language :: Python :: 3.{{minor}}',
{% endfor %}
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
        ],
        url=project_base_url,
        download_url=project_base_url + 'archive/master.zip',
        python_requires='>={{min_python_version}}',
        install_requires=read_file('requirements.txt'))
if platform.python_implementation() == 'CPython':
    from glob import glob
    from typing import Any

    from setuptools import (Command,
                            Extension)
    from setuptools.command.build_ext import build_ext
    from setuptools.command.develop import develop

    class Develop(develop):
        def reinitialize_command(self,
                                 name: str,
                                 reinit_subcommands: int = 0,
                                 **kwargs: Any) -> Command:
            if name == build_ext.__name__:
                kwargs.setdefault('debug', 1)
            result = super().reinitialize_command(name, reinit_subcommands,
                                                  **kwargs)
            if name == build_ext.__name__:
                result.ensure_finalized()
                for extension in result.extensions:
                    extension.undef_macros.append(('NDEBUG',))
            return result


    parameters.update(cmdclass={develop.__name__: Develop},
                      ext_modules=[Extension('_' + {{project}}.__name__,
                                             glob('src/*.c'))],
                      zip_safe=False)
setup(**parameters)
