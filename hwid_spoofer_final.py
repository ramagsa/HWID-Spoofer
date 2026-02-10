try:
    import tkinter as tk
    from tkinter import messagebox
    import winreg as reg
    import uuid
    import ctypes
    import os
    import random  # For adding random stars
    print("Imports succeeded. Proceeding...")
except ImportError as e:
    print(f"Critical error: Import failed. Error: {e}")
    print("Install Python from python.org and ensure Tkinter is included.")
    input("Press Enter to exit.")
    exit()

def main():
    print("Script started. Checking admin rights...")
    if not is_admin():
        print("Not running as admin. Attempting to show error...")
        try:
            root = tk.Tk()
            messagebox.showerror("Admin Error", "Run as Administrator.")
            root.destroy()
            print("Admin error shown.")
        except:
            print("Failed to show error window. Please run as admin.")
        return
    print("Admin check passed. Building GUI...")
    
    try:
        root = tk.Tk()
        root.title("Solaris Spoofer")
        root.geometry("600x500")  # Made it larger and more spacious
        root.configure(bg='black')
        print("GUI window created.")
        
        canvas = tk.Canvas(root, width=600, height=400, bg='black', highlightthickness=0)
        canvas.pack(pady=20)  # Added padding for spacing
        print("Canvas created.")
        
        # New space-themed gradient: Dark blue to black
        for i in range(400):  # Extended height for more space
            try:
                r = 0  # Start with dark colors
                g = 0
                b = int(25 * (1 - (i / 400)))  # Fade from dark blue to black
                hex_color = f'#{r:02x}{g:02x}{b:02x}'  # Simple blue-ish gradient
                canvas.create_rectangle(0, i, 600, i+1, fill=hex_color, outline='')
            except Exception as e:
                print(f"Error on gradient line {i}: {e}")
                continue
        
        # Add random stars for a spacey feel
        for _ in range(100):  # Add 100 stars
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            canvas.create_oval(x, y, x+2, y+2, fill='white', outline='')  # Small white dots
        
        print("Space gradient and stars added.")
        
        # Add title label with space theme
        title_label = tk.Label(root, text="Solaris Spoofer", fg='white', bg='black', font=("Arial", 24))  # Larger font for spacing
        title_label.place(x=200, y=420)  # Positioned lower with more space
        print("Title added.")
        
        instructions_label = tk.Label(root, text="Spoof your HWID in the vastness of space!", fg='white', bg='black', font=("Arial", 14))
        instructions_label.place(x=50, y=450)  # Increased spacing
        print("Instructions label added.")
        
        current_hwid_label = tk.Label(root, text="Current HWID: [Loading...]", fg='white', bg='black', font=("Arial", 12))
        current_hwid_label.place(x=50, y=480)  # Further down for spacing
        
        def get_current_hwid():
            print("Fetching HWID...")
            try:
                key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
                value, _ = reg.QueryValueEx(key, "MachineGuid")
                current_hwid_label.config(text=f"Current HWID: {value}")
                print("HWID fetched successfully.")
                reg.CloseKey(key)
            except Exception as e:
                current_hwid_label.config(text=f"Error: {str(e)}")
                print(f"HWID fetch error: {e}")
        
        get_current_hwid()
        
        def spoof_hwid():
            print("Spoof button clicked.")
            if messagebox.askyesno("Confirm Spoof", "Enter the void and spoof your HWID?"):
                print("Confirmed spoof.")
                fake_hwid = str(uuid.uuid4())
                try:
                    key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\SolarisSpoof")
                    reg.SetValueEx(key, "SpoofedHWID", 0, reg.REG_SZ, fake_hwid)
                    reg.CloseKey(key)
                    current_hwid_label.config(text=f"Spoofed HWID: {fake_hwid}")
                    print("Spoof successful.")
                except Exception as e:
                    current_hwid_label.config(text=f"Spoof failed: {str(e)}")
                    print(f"Spoof error: {e}")
            else:
                print("Spoof cancelled.")
        
        spoof_button = tk.Button(root, text="Spoof HWID", command=spoof_hwid, bg='black', fg='green', font=("Arial", 14))  # Green for theme
        spoof_button.place(x=50, y=520)  # More vertical space
        print("Spoof button added.")
        
        # Add the green ASCII skull as a label
        skull_art = """
 .-.
( o o )
| O O |
 \\ - /
  `"`
"""
        skull_label = tk.Label(root, text=skull_art, fg='green', bg='black', font=("Courier", 12), justify='left')  # Fixed-width font for ASCII art
        skull_label.place(x=400, y=450)  # Positioned in the corner for decoration
        print("Green skull added.")
        
        status_label = tk.Label(root, text="For exploratory use only – Navigate the cosmos wisely.", fg='green', bg='black', font=("Arial", 10))
        status_label.place(x=50, y=560)  # Even more spacing at the bottom
        
        print("Starting GUI loop...")
        root.mainloop()
    except Exception as e:
        print(f"GUI setup error: {e}")
        print("Double-check your Python installation.")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Admin check failed: {e}")
        return False

if __name__ == "__main__":
    print("Launching main...")
    main()