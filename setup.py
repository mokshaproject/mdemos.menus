try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="mdemos.menus",
    version="1.0.2",
    url="http://moksha.fedorahosted.org",
    description="Moksha Menus App",
    license="ASL 2.0",
    long_description="",
    author="Luke Macken",
    author_email="lmacken@redhat.com",
    packages=['mdemos', 'mdemos.menus', 'mdemos.menus.controllers'],
    namespace_packages=['mdemos'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "moksha.wsgi",
        "moksha.hub",
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
