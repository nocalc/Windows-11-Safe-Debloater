⚡ Features
1. App Removal

Remove built-in apps that most users don’t need:

Examples: Xbox, Solitaire, Paint 3D, Groove Music, Bing News, TikTok, Instagram.

Each app has a tooltip explaining what it is and whether it’s safe to remove.

Options are selectable individually, so you only remove what you want.

2. Service Disabling

Optional disabling of Windows services to improve privacy and performance:

Examples: Telemetry (DiagTrack), Offline Maps, Remote Registry, Fax.

Tooltips explain what each service does and the potential impact of disabling it.

Safe for beginners — services are optional.

3. Performance Tweaks

Visual Effects / Animations: Disables window animations, live window dragging, and menu fade-ins to make Windows feel snappier.

Search / Indexing Optimization: Stops Windows Search indexing to reduce CPU and disk usage.

Optional only — users must explicitly enable these tweaks. Tooltips explain trade-offs.

4. Restore Apps

Easily restore all built-in apps if you accidentally remove something important.

Safe and simple, no need for advanced PowerShell commands.

5. Tooltips & Guidance

Every option includes a hover tooltip describing its function and safety.

Designed for beginners, so no prior Windows tweaking experience is required.

6. User-Friendly GUI

Organized into three tabs: Apps, Services, Performance Tweaks.

Simple checkboxes with explanatory tooltips.

Buttons for "Run Debloat" and "Restore Apps".

Optional “Recommended Preset” functionality can be added for quick safe selections.



⚙️ Requirements

Windows 11

Python 3.x

Tkinter (pip install tk)

Must be run with administrator privileges to remove apps or disable system services.



🚀 How to Use

Download or clone this repository.

Run python debloater.py (or whatever you name the script).

Select the apps, services, and performance tweaks you want to remove or apply.

Hover over each checkbox to read what it does and see if it’s safe.

Click Run Debloat to apply your selections.

Restart your PC for all changes to take effect.

If you need to restore apps, click Restore Apps.



⚠️ Warnings

Must run as administrator to fully remove system apps and disable services.

Some apps or services may be needed depending on your personal workflow. Tooltips provide guidance.

Performance tweaks are optional; they improve responsiveness but may alter the visual experience or search speed.



💡 Why Use This Tool?

Saves disk space by removing unneeded apps.

Improves privacy by disabling telemetry services.

Boosts system performance by turning off animations and indexing.

Safe for beginners, with detailed tooltips and the ability to restore apps.

No scripts or PowerShell knowledge required — simple GUI workflow.


