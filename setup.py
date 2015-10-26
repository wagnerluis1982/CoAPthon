from distutils.core import setup

setup(
    name='CoAPthon',
    version='3.0.0',
    packages=['test', 'coapthon', 'coapthon.layers', 'coapthon.client', 'coapthon.server', 'coapthon.messages'],
    url='https://github.com/Tanganelli/CoAPthon',
    license='MIT License',
    author='Giacomo Tanganelli',
    author_email='giacomo.tanganelli@for.unipi.it',
    description='CoAPthon is a python library to the CoAP protocol. ',
    scripts=['coapserver.py', 'coapclient.py', 'exampleresources.py', 'coapforwardproxy.py', 'coapreverseproxy.py',
             'reverse_proxy_mapping.xml'], requires=['sphinx']
)
