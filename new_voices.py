import os
import pygame
import tempfile


def speak(text):
    # Create a temporary file to store the speech
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    temp_file.close()
    
    try:
        # Generate speech to the temporary file
        voice = "en-AU-WilliamNeural"
        os.system(f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "{temp_file.name}"')

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file.name)

        try:
            # Play the speech
            pygame.mixer.music.play()

            # Wait for the speech to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(f"Error playing audio: {e}")

        finally:
            # Clean up pygame resources
            if pygame.mixer.get_init() is not None:
                pygame.mixer.music.stop()
                pygame.mixer.quit()

    finally:
        # Clean up the temporary file
        try:
            os.unlink(temp_file.name)
        except Exception as e:
            print(f"Error cleaning up temporary file: {e}")
