import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Create GUI elements
        self.logo_label = tk.Label(root, text="Music player ", font=("Arial", 20))
        self.timeline = ttk.Scale(root, from_=0, to=100, orient="horizontal", length=400)
        self.play_button = ttk.Button(root, text="Play", command=self.play_music)
        self.pause_button = ttk.Button(root, text="Pause", command=self.pause_music)
        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_music)
        self.open_button = ttk.Button(root, text="Open", command=self.open_file)
        self.additional_button = ttk.Button(root, text="Additional Button", command=self.additional_action)

        # Position GUI elements
        self.logo_label.pack(pady=10)
        self.timeline.pack(pady=10)
        self.play_button.pack(side="left", padx=10)
        self.pause_button.pack(side="left", padx=10)
        self.stop_button.pack(side="left", padx=10)
        self.open_button.pack(side="left", padx=10)
        self.additional_button.pack(side="left", padx=10)

        # Initialize mixer
        mixer.init()

    def play_music(self):
        if mixer.music.get_busy():
            mixer.music.unpause()
        else:
            mixer.music.play()

    def pause_music(self):
        mixer.music.pause()

    def stop_music(self):
        mixer.music.stop()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            mixer.music.load(file_path)
            mixer.music.play()

    def additional_action(self):
        print("Perform additional action")

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
