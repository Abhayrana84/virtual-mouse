# virtual-mouse
AI Based Virtual Mouse Using Hand Gesture Recognition
Control your computer mouse using hand gestures captured through your webcam. This is an AI-powered contactless mouse system that uses computer vision and machine learning to track hand landmarks and map gestures to mouse operations.

## 🎯 Features

✅ **Real-time Hand Tracking** - Detects hand landmarks using MediaPipe AI  
✅ **Cursor Control** - Move your cursor by moving your hand  
✅ **Left Click** - Bring index and middle fingers close  
✅ **Right Click** - Extend index, middle, and ring fingers  
✅ **Scroll** - Bring thumb and index finger close together  
✅ **Screenshot** - Make a fist to capture screenshots  
✅ **Touchless Computing** - No need to touch your device  
✅ **Real-time Display** - See hand landmarks on camera feed  

## 📋 Project Abstract

This project presents an AI-based virtual mouse system that allows users to control computer mouse functions using real-time hand gesture recognition. Using computer vision and machine learning, the system tracks hand landmarks via webcam and maps gestures to mouse operations such as movement, clicking, scrolling and screenshot capture. This reduces dependency on physical hardware and provides a touch-less human-computer interaction interface.

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Webcam
- Windows/Mac/Linux

### Step 1: Clone Repository
```bash
git clone git@github.com:Abhayrana84/virtual-mouse.git
cd virtual-mouse
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `opencv-python` - Computer vision
- `mediapipe` - Hand detection AI
- `numpy` - Numerical computing
- `pyautogui` - Mouse control
- `pynput` - Alternative mouse control

## 🚀 Quick Start

### Run the Application
```bash
python virtual_mouse_working.py
```

Your camera window will open with live hand tracking!

## 🎮 How to Use

### Gesture Controls

| Gesture | Action |
|---------|--------|
| **Hand visible** | Move cursor |
| **Index + Middle close** | Left click |
| **Index + Middle + Ring up** | Right click |
| **Thumb + Index close** | Scroll up |
| **Fist (all fingers closed)** | Take screenshot |
| **Press ESC** | Exit application |

### Example Usage
1. Open the application
2. Move your hand to move the cursor
3. Bring two fingers close to click
4. Make a fist to take a screenshot
5. Press ESC to exit

## 📁 Project Structure

```
VirtualMouse/
├── virtual_mouse_working.py    # Main working application
├── virtual_mouse.py             # Alternative version
├── util.py                      # Helper functions
├── requirements.txt             # Dependencies
├── hand_landmarker.task        # AI model (auto-downloaded)
└── README.md                    # This file
```

## 🧠 How It Works

```
1. Webcam captures video frames
   ↓
2. MediaPipe detects 21 hand landmarks
   ↓
3. System identifies finger positions
   ↓
4. Gestures are recognized based on finger angles & distances
   ↓
5. Corresponding mouse action is performed
   ↓
6. Process repeats at ~30 FPS
```

## 📊 Flowchart

```
┌──────────────┐
│   START      │
└──────┬───────┘
       ↓
┌──────────────────────┐
│ Initialize Webcam &  │
│ Load MediaPipe Model │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Capture Video Frame  │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Convert Frame to RGB │
└──────┬───────────────┘
       ↓
┌────────────────────────────┐
│ Detect Hand & 21 Landmarks │
└──────┬─────────────────────┘
       ↓
┌──────────────────────────┐
│ Extract Finger Positions │
└──────┬───────────────────┘
       ↓
┌──────────────────────────┐
│ Identify Gesture Pattern │
└──────┬───────────────────┘
       ↓
┌───────────────Decision Block────────────────┐
│                                              │
│  Is Hand Visible? ──► Move Cursor            │
│  Are Index & Middle Close? ──► Left Click    │
│  Are 3 Fingers Up? ──► Right Click           │
│  Thumb + Index Close? ──► Scroll             │
│  All Fingers Closed? ──► Screenshot          │
│                                              │
└──────┬───────────────────────────────────────┘
       ↓
┌──────────────────────┐
│ Perform Mouse Action │
└──────┬───────────────┘
       ↓
┌──────────────────────┐
│ Display Output Frame │
└──────┬───────────────┘
       ↓
┌──────────────┐
│  EXIT (ESC)  │
└──────────────┘
```

## 🔧 Technical Details

### Technologies Used
- **Python 3.11**
- **MediaPipe** - Hand detection and landmark tracking
- **OpenCV** - Video capture and image processing
- **PyAutoGUI** - Mouse control
- **PyInput** - Alternative mouse control library

### Hand Landmarks (21 points)
```
0 - Wrist
1-4 - Thumb
5-8 - Index Finger
9-12 - Middle Finger
13-16 - Ring Finger
17-20 - Pinky Finger
```

### Key Functions
- `fingers_up()` - Detects which fingers are extended
- `find_distance()` - Calculates distance between two points
- `get_distance()` - Gets distance from point list
- `get_angle()` - Calculates angle between three points

## 📦 Requirements

```
opencv-python>=4.5.0
mediapipe>=0.10.0
numpy>=1.21.0
pyautogui>=0.9.53
pynput>=1.8.1
```

## ⚙️ Configuration

You can modify these parameters in `virtual_mouse_working.py`:

```python
# Mouse sensitivity (adjust for your screen size)
mx = np.interp(x, (0, w), (0, screen_w))
my = np.interp(y, (0, h), (0, screen_h))

# Click distance threshold (in pixels)
if find_distance(lm[8], lm[12]) < 30:  # Adjust 30

# Scroll speed
pyautogui.scroll(40)  # Adjust 40 for faster/slower scroll

# Cooldown to prevent accidental clicks
cooldown = 10  # Adjust time between clicks
```

## 🎓 Use Cases

- **Assistive Technology** - For people with mobility issues
- **Presentation Control** - Gesture-based controls
- **Gaming** - Touchless gaming experience
- **Accessibility** - Alternative to traditional mouse
- **Hygiene** - Contactless computer interaction
- **Educational Project** - AI/ML demonstration
- **Research** - Human-Computer Interaction (HCI)

## 🐛 Troubleshooting

### Camera not opening
```bash
# Check if your camera works
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened())"
```

### Hand not detected
- Ensure good lighting
- Keep hand fully visible
- Try adjusting camera angle
- Check `hand_landmarker.task` exists

### Gestures not working
- Increase/decrease distance threshold in code
- Improve lighting conditions
- Try different hand positions
- Check console for error messages

### Slow performance
- Reduce frame resolution
- Lower detection confidence threshold
- Close other applications
- Update graphics drivers

## 📝 Example Output

When running, you'll see:
```
Downloading hand detection model...
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
AI Virtual Mouse window opens with:
- Green dots for hand landmarks
- Blue lines for finger connections
- Real-time cursor movement
- Action labels (Left Click, Right Click, etc)
```

## 🔐 Permissions

The application requires:
- ✅ Webcam access
- ✅ Mouse control
- ✅ File system access (for screenshots)

## 📸 Screenshots & Demos

Gesture recognition in action:
- Hand visible → Cursor follows
- Fingers pinch → Click performed
- Fist closed → Screenshot taken

## 🚀 Future Enhancements

- [ ] Multi-hand support
- [ ] Hand pose recognition (thumbs up, etc)
- [ ] Voice commands integration
- [ ] Gesture customization
- [ ] Desktop GUI
- [ ] Mobile app version
- [ ] Advanced gesture library
- [ ] Performance optimization

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Abhay Rana**  
GitHub: [@Abhayrana84](https://github.com/Abhayrana84)  
Repository: [virtual-mouse](https://github.com/Abhayrana84/virtual-mouse)

## 🙏 Acknowledgments

- MediaPipe team for the hand detection model
- OpenCV for computer vision tools
- PyAutoGUI for mouse control
- Python community for great libraries

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Open an issue on GitHub
3. Check camera and lighting conditions
4. Ensure all dependencies are installed

## 🎉 Enjoy Your Virtual Mouse!

Move your hand, control your mouse - no contact needed! 🖱️✋

---

**Last Updated**: January 1, 2026  
**Version**: 1.0  
**Status**: Production Ready
