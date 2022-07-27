from setuptools import setup

package_name = 'streamlit_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zb',
    maintainer_email='zb@gmail.com',
    description='streamlit user interface package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_streamlit = streamlit_ros.run_streamlit:main'
        ],
    },
)
