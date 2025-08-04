# convert the text to speech 
# converting AI text response into speach

import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from pydub import AudioSegment

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

#convert the text to speech using ElevenLabs API 
def text_to_speech_with_elevenlabs(input_text , output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)

    #~ creating the audio file using ElevenLabs API
    audio=client.text_to_speech.convert(
        text= input_text,
        #selecting the type of voice you want to use man,woman,child,robot
        voice_id="Dslrhjl3ZpzrctukrQSN", #"JBFqnCBsd6RMkjVDRZzb",
        # selecting the model you want to use for text to speech 
        model_id="eleven_multilingual_v2",
        output_format= "mp3_44100",
    )

    #~ saving the audio file to the output filepath
    elevenlabs.save(audio, output_filepath)
    
     # 3. Convert MP3 to WAV
    mp3_path = output_filepath
    wav_path = output_filepath.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

     # 4. Play WAV based on OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_path])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_path])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    #~ playing the audio file using the appropriate method based on the operating system
    # os_name = platform.system()
    # try:
    #     #providing different commands for different operating systems to play the audio file
    #     # it smartly detects the operating system and plays the audio file accordingly
    #     if os_name == "Darwin":  # macOS
    #         subprocess.run(['afplay', output_filepath])
    #     elif os_name == "Windows":  # Windows
    #         subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
    #     elif os_name == "Linux":  # Linux
    #         subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
    #     else:
    #         raise OSError("Unsupported operating system")
    # except Exception as e:
    #     print(f"An error occurred while trying to play the audio: {e}")


# input_text = "Hello Akash, this is ElevenLabs speaking."
# output_filepath = "text_to_speech.mp3"
# text_to_speech_with_elevenlabs(input_text, output_filepath)



from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")




# input_text = "Hello, this is a test of the text to speech functionality."
# output_filepath = "text_to_speech.mp3"

# text_to_speech_with_elevenlabs(input_text) # only convert into audio file do not play
# # text_to_speech_with_gtts(input_text, output_filepath)


# sound = AudioSegment.from_mp3("text_to_speech.mp3")
# sound.export("text_to_speech.wav", format="wav")
# wav_path = "text_to_speech.wav"

# # Step 3: Play WAV (manually, not inside function)
# # Example for Windows:
# import subprocess
# subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])