import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

# ----------------- PowerShell Runner -----------------
def run_powershell(cmd):
    """Run a PowerShell command silently"""
    full_cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", cmd]
    subprocess.run(full_cmd, shell=True)

# ----------------- ToolTip Class -----------------
class CreateToolTip(object):
    """Create a tooltip for a given widget"""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

# ----------------- App, Services, Performance Tweaks -----------------
apps = {
    "Xbox": "*xbox*", 
    "Solitaire Collection": "Microsoft.SolitaireCollection",
    "3D Viewer": "Microsoft.Microsoft3DViewer", 
    "Paint 3D": "Microsoft.Paint3D",
    "Mixed Reality Portal": "Microsoft.MixedReality.Portal", 
    "Groove Music": "Microsoft.ZuneMusic",
    "Movies & TV": "Microsoft.ZuneVideo", 
    "Bing News": "Microsoft.BingNews",
    "Bing Weather": "Microsoft.BingWeather", 
    "Skype": "Microsoft.SkypeApp",
    "Teams": "MicrosoftTeams", 
    "OneNote": "Microsoft.OneNote",
    "Office Hub": "Microsoft.OfficeHub", 
    "Feedback Hub": "Microsoft.WindowsFeedbackHub",
    "Clipchamp": "Clipchamp.Clipchamp", 
    "Spotify": "SpotifyAB.SpotifyMusic",
    "TikTok": "BytedancePte.Ltd.TikTok", 
    "Facebook": "FACEBOOK.Facebook",
    "Instagram": "Instagram.Instagram",
}

app_descriptions = {
    "Xbox": "Xbox gaming app. Optional if you don’t use Xbox.",
    "Solitaire Collection": "Microsoft Solitaire. Safe to remove if you don’t play.",
    "3D Viewer": "3D model viewer. Optional for most users.",
    "Paint 3D": "Paint 3D app. Optional if you don’t use it.",
    "Mixed Reality Portal": "VR/AR portal. Safe to remove on non-VR systems.",
    "Groove Music": "Music app. Optional if you use other music players.",
    "Movies & TV": "Video app. Optional if you use other video players.",
    "Bing News": "News app from Microsoft. Optional.",
    "Bing Weather": "Weather app. Optional.",
    "Skype": "Skype app. Remove if you don’t use Skype.",
    "Teams": "Microsoft Teams. Optional if not used.",
    "OneNote": "Note-taking app. Optional if you don’t use OneNote.",
    "Office Hub": "Office app hub. Optional.",
    "Feedback Hub": "Sends feedback to Microsoft. Optional.",
    "Clipchamp": "Video editor. Optional.",
    "Spotify": "Spotify app. Optional if you use another music service.",
    "TikTok": "TikTok app. Optional.",
    "Facebook": "Facebook app. Optional.",
    "Instagram": "Instagram app. Optional."
}

services = {
    "Telemetry (DiagTrack)": "DiagTrack",
    "Telemetry Push (dmwappushservice)": "dmwappushservice",
    "Offline Maps (MapsBroker)": "MapsBroker",
    "Remote Registry": "RemoteRegistry",
    "Fax Service": "Fax"
}

service_descriptions = {
    "Telemetry (DiagTrack)": "Windows telemetry service. Disabling improves privacy.",
    "Telemetry Push (dmwappushservice)": "Telemetry push service. Optional to disable.",
    "Offline Maps (MapsBroker)": "Offline maps service. Disabling may improve performance.",
    "Remote Registry": "Allows remote registry access. Optional to disable.",
    "Fax Service": "Fax service. Safe to disable if you don’t use fax."
}

performance_tweaks = {
    "Visual Effects / Animations": "Makes Windows feel snappier by removing animations.",
    "Search / Indexing Optimization": "Reduces CPU/disk usage by stopping file indexing. May slow searches."
}

# ----------------- Tkinter Variables -----------------
app_vars = {}
service_vars = {}
perf_vars = {}

# ----------------- Debloat Functions -----------------
def safe_debloat():
    removed = []
    disabled = []

    # Remove apps
    for app_name, app_id in apps.items():
        if app_vars[app_name].get():
            run_powershell(f"Get-AppxPackage -Name {app_id} -AllUsers | Remove-AppxPackage -ErrorAction SilentlyContinue")
            run_powershell(f"Get-AppxProvisionedPackage -Online | Where-Object DisplayName -like {app_id} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue")
            removed.append(app_name)

    # Disable services
    for svc_name, svc_id in services.items():
        if service_vars[svc_name].get():
            run_powershell(f"Stop-Service {svc_id} -ErrorAction SilentlyContinue")
            run_powershell(f"Set-Service {svc_id} -StartupType Disabled -ErrorAction SilentlyContinue")
            disabled.append(svc_name)

    # Disable ads/widgets by default
    run_powershell(r'New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-338387Enabled" -Value 0 -Force')
    run_powershell(r'New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager" -Name "SubscribedContent-353694Enabled" -Value 0 -Force')
    run_powershell(r'New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "TaskbarDa" -Value 0 -Force')
    run_powershell(r'New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "ShowSyncProviderNotifications" -Value 0 -Force')

    # Apply performance tweaks
    if perf_vars["Visual Effects / Animations"].get():
        run_powershell(r'Set-ItemProperty "HKCU:\Control Panel\Desktop" "WindowAnimations" 0')
        run_powershell(r'Set-ItemProperty "HKCU:\Control Panel\Desktop" "MenuShowDelay" 0')
        run_powershell(r'Set-ItemProperty "HKCU:\Control Panel\Desktop" "DragFullWindows" 0')
    if perf_vars["Search / Indexing Optimization"].get():
        run_powershell(r'Stop-Service WSearch')
        run_powershell(r'Set-Service WSearch -StartupType Disabled')

    msg = ""
    if removed:
        msg += f"Removed apps:\n - " + "\n - ".join(removed) + "\n\n"
    if disabled:
        msg += f"Disabled services:\n - " + "\n - ".join(disabled) + "\n\n"
    perf_applied = [k for k,v in perf_vars.items() if v.get()]
    if perf_applied:
        msg += "Applied performance tweaks:\n - " + "\n - ".join(perf_applied) + "\n\n"
    if not msg:
        msg = "No changes made."

    messagebox.showinfo("Debloat Complete", msg + "\n✅ Please restart your PC.")

def restore_apps():
    run_powershell(r'Get-AppxPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml" -ErrorAction SilentlyContinue}')
    messagebox.showinfo("Restore Complete", "Default apps have been restored.\n✅ Please restart your PC.")

# ----------------- GUI -----------------
root = tk.Tk()
root.title("Windows 11 Safe Debloater")
root.geometry("550x750")

notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Apps")
notebook.add(tab2, text="Services")
notebook.add(tab3, text="Performance Tweaks")
notebook.pack(expand=True, fill="both")

# Apps tab
tk.Label(tab1, text="Select apps to remove:", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=5)
for app in apps:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(tab1, text=app, variable=var)
    chk.pack(anchor="w")
    app_vars[app] = var
    CreateToolTip(chk, app_descriptions[app])

# Services tab
tk.Label(tab2, text="Select services to disable:", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=5)
for svc in services:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(tab2, text=svc, variable=var)
    chk.pack(anchor="w")
    service_vars[svc] = var
    CreateToolTip(chk, service_descriptions[svc])

# Performance tab
tk.Label(tab3, text="Select performance tweaks (optional):", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=5)
for tweak in performance_tweaks:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(tab3, text=tweak, variable=var)
    chk.pack(anchor="w")
    perf_vars[tweak] = var
    CreateToolTip(chk, performance_tweaks[tweak])

# Bottom buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Run Debloat", command=safe_debloat, bg="red", fg="white", width=15).pack(side="left", padx=5)
tk.Button(btn_frame, text="Restore Apps", command=restore_apps, bg="green", fg="white", width=15).pack(side="left", padx=5)

root.mainloop()
