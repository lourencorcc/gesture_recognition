from setuptools import find_packages, setup

package_name = 'gesture_recognition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/model', [
            'gesture_recognition/model/__init__.py',
        ]),
        ('share/' + package_name + '/model/keypoint_classifier', [
            'gesture_recognition/model/keypoint_classifier/keypoint_classifier_label.csv',
            'gesture_recognition/model/keypoint_classifier/keypoint_classifier.hdf5',
            'gesture_recognition/model/keypoint_classifier/keypoint_classifier.tflite',
            'gesture_recognition/model/keypoint_classifier/keypoint_classifier.py',
            'gesture_recognition/model/keypoint_classifier/keypoint.csv',
        ]),
        ('share/' + package_name + '/model/point_history_classifier', [
            'gesture_recognition/model/point_history_classifier/point_history_classifier_label.csv',
            'gesture_recognition/model/point_history_classifier/point_history_classifier.hdf5',
            'gesture_recognition/model/point_history_classifier/point_history_classifier.tflite',
            'gesture_recognition/model/point_history_classifier/point_history_classifier.py',
            'gesture_recognition/model/point_history_classifier/point_history.csv',
        ]),
        ('share/' + package_name + '/utils', [
            'gesture_recognition/utils/cvfpscalc.py',
            'gesture_recognition/utils/__init__.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lourencorcc',
    maintainer_email='lourencorconceicao@gmail.com',
    description='Hand Gesture Recognition using MediaPipe in ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = gesture_recognition.my_node:main',
            'hand_gesture_node = gesture_recognition.hand_gesture_node:main',
            'webcam_publisher = gesture_recognition.webcam_publisher:main',
        ],
    },
)
