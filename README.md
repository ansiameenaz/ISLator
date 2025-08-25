# ISLator – Indian Sign Language Translator (Rule-Based)

ISLator is a rule-based system developed to convert Indian Sign Language (ISL) gestures into textual output. This project aims to bridge communication gaps for the Indian hearing-impaired community by providing an accessible and accurate ISL-to-text translation system.

Features

Rule-Based Translation: Utilizes predefined gesture-to-text rules for reliable conversion.

Real-Time Gesture Recognition: Processes video or live camera feed for immediate translation.

Lightweight and Efficient: Does not require heavy deep learning models, making it suitable for low-resource environments.

Text Output: Converts recognized ISL gestures into readable text for communication.

How It Works

Preprocessing:

Input video frames or images are captured.

Hand detection and segmentation are performed to isolate gestures.

Gesture Extraction:

Key features such as hand shape, orientation, and movement are identified.

Rule-Based Mapping:

Each detected gesture is mapped to its corresponding ISL symbol using a set of predefined rules.

Text Generation:

Recognized gestures are converted into meaningful text output.

Installation

Clone the repository:

git clone <link>


Navigate to the project folder:

cd ISLator


Install required dependencies:

pip install -r requirements.txt

Usage

Run the main application:

python main.py


Point your camera at the gesture and observe the text output on the console.

Limitations

Rule-based methods can struggle with ambiguous gestures or variations in hand positioning.

Currently supports a limited set of ISL gestures.

Accuracy depends on lighting and camera quality.

Future Work

Integrate machine learning for better gesture recognition accuracy.

Expand vocabulary to cover more ISL gestures.

Add support for sentence construction and context-based translation.

Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve ISLator.
