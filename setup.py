from setuptools import setup

setup(
        name='YiCat',
        version='1.0',
        packages=['Page', 'Page.page', 'Page.testcase', 'model'],
        url='http://git.emao.net/ptc1_test/TestAutomation',
        license='',
        author='chenshiyang',
        author_email='chenshiyang460@emao.com',
        description='Python Web Automation Test Framework with Selenium WebDriver',
        install_requires= ['selenium==2.53.6', 'xlrd', 'xlwt', 'redis', 'importlib', 'xvfbwrapper','requests','fake_useragent']
)
