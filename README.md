# Enhancing Rider Safety with rideCare: A Comprehensive Ride Monitoring Solution

## Introduction
The rapid growth of ride-hailing services has undoubtedly transformed the transportation landscape. However, this evolution has brought to the forefront concerns regarding rider safety. In response to these concerns, we have devised an innovative solution that aims to ensure the safety and enjoyment of all passengers. Our brainchild, rideCare, introduces a novel hardware component capable of autonomously activating a dashcam to live-stream the unfolding events to authorized personnel. In parallel, the system dispatches real-time text alerts via Twilio to designated emergency contacts, equipping them to take immediate manual actions and ensure the well-being of the riders.

## Functionality
rideCare operates as a seamless fusion of cutting-edge technologies, harnessing the prowess of Machine Learning, specifically Natural Language Processing, in conjunction with hardware like the Raspberry Pi. By employing sophisticated linguistic analysis, the system detects potential conflicts within conversations between the driver and passengers. Subsequently, it triggers alerts, enabling registered emergency contacts to access a transcript of the conversation along with a live-streaming link. Moreover, this capability can be harnessed by emergency services like 911 to intercede as deemed necessary.

## Construction
### System Architecture
![rideCare Logo](https://github.com/pooja-krishan/rideCare/blob/main/rideCare-system-architecture.png)
### Hardware Components
- Raspberry Pi Model 4 B (Running Raspbian OS)
- C922 PRO HD STREAM WEBCAM
- Blue Yeti USB Microphone

### Software Stack
- Python 3
- Vosk for Speech-to-Text Conversion
- Perspective API for Toxic Comment Classification
- OpenCV for Real-Time Video Streaming
- Twilio for SMS Alerts to Emergency Contacts

## Challenges Overcome
Throughout the development process, we encountered several noteworthy challenges:
- Orchestrating a harmonious integration of the entire project, particularly the marriage of React with Flask.
- Leveraging a text-based comment classification library, such as Perspective API, to attain accurate predictions when handling real-time speech input.
- Overcoming the obstacle of sending SMS alerts through Twilio, which initially presented complications due to the presence of a toll-free number on the trial account.
- Devising a robust formula, graded on a scale of 1 to 5, to gauge the severity of conversational toxicity based on weighted labels from the widely available Kaggle dataset employed by Perspective API.

## Proud Achievements
The achievements that particularly stand out in our journey include:
- Incorporating OpenAI API to augment sentiment analysis capabilities, alongside Perspective API.
- Harnessing the capabilities of vosk, a speech-to-text library, to seamlessly transmute real-time speech into text for predictive analyses.
- Successfully designing and implementing a comprehensive solution that integrates both hardware and software components to enhance rider safety.

## Future Trajectory - Advancing SafeRide.ai
Our vision for SafeRide.ai encompasses several forward-looking features and advancements, including:
- Implementation of speaker diarization to accurately identify and alert targeted emergency contacts.
- Construction of an expansive web interface to facilitate seamless data streaming and accessibility.

In conclusion, rideCare epitomizes a pioneering stride towards ensuring rider safety within the ride-hailing domain. By harmonizing sophisticated technology with real-world application, we endeavor to establish a new paradigm of secure and enjoyable journeys.