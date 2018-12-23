from setuptools import setup

setup(
    name='snapshotanalyzer-30000',
    version='0.1',
    author='Robin Norwood',
    author_email='robin@acloud.guru',
    description='SnapshotAnalyzer-30000 is a tool to manage AWS EC2 snapshots',
    packages=[
        'shotty'
    ],
    url="https://github.com/robin-acloud/snapshotanalyzer-30000",
    install_requires=[
        'boto3',
        'click'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        '''
)