# Windows 11 Safe Debloater 🖥️✨

A **beginner-friendly Python GUI tool** to remove unnecessary bloatware, disable telemetry, and improve system performance on **Windows 11**.  
Safe, flexible, and fully guided — every option includes a **tooltip** explaining what it does and whether it’s safe to remove.

---

## ⚡ Features

### 1. App Removal
Remove built-in apps that most users don’t need:

- **Xbox**, **Solitaire**, **Paint 3D**, **Groove Music**, **Bing News**, **TikTok**, **Instagram**, and more.
- **Hover over each option** to see a tooltip explaining the app and whether it’s safe to remove.
- Options are **selectable individually**, giving you full control.

---

### 2. Service Disabling
Optional disabling of Windows services to improve privacy and performance:

- **Telemetry (DiagTrack)**, **Offline Maps (MapsBroker)**, **Remote Registry**, **Fax**, etc.
- Tooltips explain the function and impact of disabling each service.
- Safe for beginners — services are optional.

---

### 3. Performance Tweaks
Optional performance improvements:

- **Visual Effects / Animations**  
  Disables window animations, menu fade-ins, and live window dragging to make Windows feel faster.

- **Search / Indexing Optimization**  
  Stops Windows Search indexing to reduce CPU and disk usage. May slow file searches.

> ⚠️ Optional only — no tweaks are applied unless you explicitly select them.

---

### 4. Restore Apps
- Restore all removed built-in apps easily.
- Safe and simple — no PowerShell knowledge required.

---

### 5. Tooltips & Guidance
- Every option includes a **hover tooltip** describing its purpose and safety.
- Designed for **beginners**, so you don’t need prior Windows tweaking experience.

---

### 6. User-Friendly GUI
- Organized into three tabs:
  1. Apps
  2. Services
  3. Performance Tweaks
- Buttons for **Run Debloat** and **Restore Apps**.
- Optional **Recommended Preset** functionality can be added for quick safe selections.

---

## ⚙️ Requirements

- Windows 11  
- **Python 3.x**  
- Tkinter (`pip install tk`)  
- Must be run with **administrator privileges** to remove system apps or disable services.

---

## 🚀 How to Use

1. **Download or clone** this repository.  
2. Run the script:  
   ```bash
   python debloater.py
