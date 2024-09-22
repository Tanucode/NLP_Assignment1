import os
import shutil

# Function to copy files that do not contain bad words
def copy_clean_files(text_folder, output_folder, bad_words):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of all text files in the folder
    text_files = [f for f in os.listdir(text_folder) if f.endswith('.txt')]

    for text_file in text_files:
        file_path = os.path.join(text_folder, text_file)
        
        # Read the content of the text file
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()

        # Check if any bad word is in the content (case insensitive)
        if not any(bad_word.lower() in content.lower() for bad_word in bad_words):
            # If no bad words are found, copy the file to the output folder
            shutil.copy(file_path, os.path.join(output_folder, text_file))
            print(f"Copied {file_path} to {output_folder}")

# List of bad words (can be modified)
bad_words =  ['मौगा', 'भतारकटनी', 'जरलाहा', 'मुहझौसा', 'भकचोनार', 'लबरा', 'चितकाबर', 'छिचलेदार', 
             'बकलोल', 'बरबताह', 'लारचट्टा', 'गरचट्टा', 'बुरचट्टा', 'बुरबक', 'भतार', 
             'सनकि', 'वेश्या', 'धी-चोदा', 'चाक', 'गू', 'रंड', 'लार', 'खसवा', 
             'चितवा', 'थेथर']  # Replace with actual bad words

# Set your text folder path and the output folder path
text_folder = ('./GArticles')
output_folder = ('./Carticles')

# Call the function to copy files that do not contain bad words
copy_clean_files(text_folder, output_folder, bad_words)

print("Task complete.")