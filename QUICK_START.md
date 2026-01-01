# 🚀 QUICK START GUIDE - Virtual Mouse

**For Complete Beginners - Follow these steps exactly!**

---

## ✅ Step-by-Step Installation

### STEP 1: Install Python (if not installed)

1. Go to: https://www.python.org/downloads/
2. Click **"Download Python 3.11"** (or latest version)
3. Run the installer
4. **IMPORTANT**: Check the box ☑️ **"Add Python to PATH"**
5. Click **"Install Now"**
6. Wait for installation to complete

**Verify Python installed:**
- Open PowerShell (search "PowerShell" in Start menu)
- Type: `python --version`
- Should show: `Python 3.11.x`

---

### STEP 2: Get the Virtual Mouse Project

**Option A - Git Clone (Recommended)**
```powershell
git clone git@github.com:Abhayrana84/virtual-mouse.git
cd virtual-mouse
```

**Option B - Download ZIP**
1. Go to: https://github.com/Abhayrana84/virtual-mouse
2. Click green **"Code"** → **"Download ZIP"**
3. Extract the ZIP file to your Desktop
4. Open PowerShell in that folder (right-click → Open PowerShell here)

---

### STEP 3: Install Required Packages

**Copy and paste this command in PowerShell:**

```powershell
pip install -r requirements.txt
```

**Wait for it to finish** (2-3 minutes) ⏳

You should see:
```
Successfully installed opencv-python mediapipe numpy pyautogui pynput
```

---

### STEP 4: Run the Application

**Copy and paste this command:**

```powershell
python virtual_mouse_working.py
```

**That's it!** 🎉 Your camera window will open!

---

## 🎮 How to Use

Once the camera window opens:

| Action | Gesture |
|--------|---------|
| **Move Cursor** | Move your hand (index finger) |
| **Left Click** | Bring index & middle finger close |
| **Right Click** | Extend 3 fingers up |
| **Scroll** | Bring thumb & index close |
| **Screenshot** | Make a fist |
| **Exit App** | Press **ESC** key |

---

## ⚡ Fastest Way to Run (Next Time)

Create a file called `start.bat` in the VirtualMouse folder:

```batch
@echo off
python virtual_mouse_working.py
```

Then just **double-click** `start.bat` to run! 

---

## ❌ Common Issues & Fixes

### Issue 1: "python is not recognized"
**Fix:** Python not in PATH
- Uninstall Python
- Reinstall and **CHECK** "Add Python to PATH"
- Restart PowerShell

### Issue 2: "No module named 'mediapipe'"
**Fix:** Reinstall packages
```powershell
pip install --upgrade -r requirements.txt
```

### Issue 3: "Camera won't open"
**Fix:** 
- Check if another app is using camera
- Give Python camera permissions (Windows Settings → Privacy)
- Try different USB port if using external camera

### Issue 4: "Hand not detected"
**Fix:**
- Improve room lighting (very important!)
- Keep hand fully visible
- Move hand slowly
- Try moving closer to camera

### Issue 5: "hand_landmarker.task not found"
**Fix:** 
- Run the app again (auto-downloads)
- Or wait 30 seconds on first run

---

## 📋 What You Need

- ✅ Python 3.7+ installed
- ✅ Webcam working
- ✅ Good lighting (important!)
- ✅ Stable internet (for downloading model)

---

## 🎬 Video Tutorial

For visual learners, here's what to expect:

1. Open PowerShell
2. Navigate to folder
3. Run: `python virtual_mouse_working.py`
4. Camera opens
5. Green dots appear on your hand
6. Move hand to move cursor
7. Pinch fingers to click

---

## 📞 Need Help?

1. Check the **Troubleshooting** section in README.md
2. Ensure good lighting
3. Make sure webcam is not blocked
4. Try restarting the application
5. Check GitHub issues: https://github.com/Abhayrana84/virtual-mouse/issues

---

## 🎓 Next Steps

After it's working:
- Explore the code in `virtual_mouse_working.py`
- Try modifying gesture detection
- Experiment with different click distances
- Check `util.py` for helper functions
- Read full README.md for advanced features

---

## ✨ You're All Set!

Run: `python virtual_mouse_working.py`

And enjoy your contactless virtual mouse! 🖱️✋

**Questions?** Check README.md or open an issue on GitHub.

---

**Last Updated:** January 1, 2026  
**Difficulty Level:** ⭐ Beginner Friendly
