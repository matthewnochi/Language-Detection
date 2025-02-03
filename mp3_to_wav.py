from pydub import AudioSegment
import os

# Path to the directory containing MP3 files
mp3_dir = "/Users/matthewnochi/Desktop/Hindi/hi/clips"

# Path to the directory where you want to save WAV files
wav_dir = "/Users/matthewnochi/Desktop/Hindi/hi/clips1"

# Create the output directory if it doesn't exist
os.makedirs(wav_dir, exist_ok=True)

# Iterate through each MP3 file in the directory
for filename in os.listdir(mp3_dir):
    if filename.endswith(".mp3"):
        # Load the MP3 file
        mp3_path = os.path.join(mp3_dir, filename)
        sound = AudioSegment.from_mp3(mp3_path)
        
        # Construct the output WAV file path
        wav_path = os.path.join(wav_dir, os.path.splitext(filename)[0] + ".wav")
        
        # Export the audio in WAV format
        sound.export(wav_path, format="wav")

print("Conversion completed.")

