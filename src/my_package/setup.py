from setuptools import setup
from glob  import glob
import os

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='palneel',
    maintainer_email='palneel@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'sample = my_package.sample:main',
        'robot_publisher = my_package.robot_publisher:main',
        'robot_subscriber = my_package.robot_subscriber:main',
        'add_two_ints_server = my_package.add_two_ints_server:main',
        'add_two_ints_client = my_package.add_two_ints_client:main',
        'turtlesim_controller = my_package.turtle_controller:main',
        'turtlesim_chase = my_package.turtle_chase:main'    
        ],
    },
)
