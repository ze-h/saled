Student: Kash Pritt
Class: CS 490
Date Created: 10/15
Engineering Notebook

DATE 9/16
Got app cloned and ran on device per Dr.Liu’s requests
![alt text](image.png)
 


DATE 9/26
Finished up the project proposal before submission


DATE 10/6
Made the Architecture model to show the remote system and the user gui along with the database. Files are loaded into the remote as they are loaded into the host, the transcriber whisper is represented separate rather than a class in salac due to it being a program that has been created
 ![alt text](image-1.png)
 
DATE 10/7
Created Data flow diagram to show how files move throughout the system
 ![alt text](image-2.png)

DATE 10/9
Remade the UML class model. Removed needless callback methods and added in SALAC
 ![alt text](image-3.png)
DATE 10/17
 Created a new gui design in gimp, simple to change design pattern to make changes listed by dr.liu. The new design incorporates file selector, an editor, buttons for transcription, a change to the transcribe readout where it now aligns with the spectrogram. Annotation zones capture things of interest such as callbacks, runways etc.
 ![alt text](image-4.png)
 
DATE: 10/19
 Added a timestamp code callback to be updated on user file change or selection. The timestamp does not follow playtime of audio do to pydubs not having a method for is_playing(), have to find other way to track audio playtime.
        
@callback(
    Output("timestamp","children"),
    Input("global-waveform", "selectedData"),
    Input("file-selector", "value")
)
def updateTimestamp(selection, sample_audio):
    if not sample_audio:
        raise PreventUpdate
    
    audio = AudioSegment.from_file(sample_audio)
  
    start = time.time()
    if selection is not None and "range" in selection.keys():
        left_bound = selection["range"]["x"][0] * 0.01
    else:
        left_bound = 0
    
    
    current = time.strftime("%H:%M:%S", time.gmtime(time.time() % audio.duration_seconds))
    audio_length = audio.duration_seconds
    
    left_ms = int(left_bound % 1 *1000)
    left_seconds = int(left_bound % 60)
    left_minutes = int((left_bound/60)%60)
    left_hours = int((left_bound /3600)%60)
    
    
    #this represents the right sde of the timestamp for audio play
    right_ms = int(audio_length % 1 * 1000)
    right_seconds = int(audio_length % 60)
    right_minutes = int((audio_length / 60) % 60)
    right_hours = int((audio_length / 3600) % 60)
    
    
    return f"{left_hours:02d}:{left_minutes:02d}:{left_seconds:02d}:{left_ms:02d}/{right_hours:02d}:{right_minutes:02d}:{right_seconds:02d}.{right_ms:03d}",



DATE 10/18
Worked on section 2 of SRD, finished up until point needing a USE CASE model to write scenarios.

