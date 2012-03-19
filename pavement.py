from paver.easy import *
from paver.setuputils import setup, find_package_data, find_packages
from paver.setuputils import install_distutils_tasks
from moksha.lib.paver_tasks import *

install_distutils_tasks()

options(
    setup=Bunch(
        name="mdemos.menus",
        version="0.1",
        release="1",
        url="http://moksha.fedorahosted.org",
        description="Moksha Menus App",
        license="ASL 2.0",
        long_description="",
        author="Luke Macken",
        author_email="lmacken@redhat.com",
        rpm_name='moksha-menus',
        packages=find_packages(),
        package_data=find_package_data(),
        namespace_packages=['mdemos'],
        install_requires=[
            "moksha>=0.7.0a",
        ],
        entry_points={
            'moksha.menu': (
                'default_menu = mdemos.menus:MokshaDefaultMenu',
            ),
            'moksha.application': (
                'menu = mdemos.menus.controllers:MokshaMenuController',
            ),
        }
    ),
)
