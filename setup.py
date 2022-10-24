from setuptools import setup

setup(
    name='libcamera-streamer',
    version='0.0.3',
    packages=['libcamera-streamer'],
    scripts=['bin/libcamera-streamer'],
    description='simple mpg streamer for libcamera',
    long_description=open('README.md').read(),
    install_requires=["picamera2", "simplejpeg", 'numpy <= 1.23.4'],
    package_dir={'libcamera-streamer': 'bin'},

)
