# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. This pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieve filenames from the folder
    filename_list = listdir(image_dir)
    
    # Create an empty dictionary to hold results
    results_dic = dict()
    
    # Process each filename
    for filename in filename_list:
        # Ignore hidden files
        if filename.startswith("."):
            continue

        # Convert filename to lowercase, split by underscores
        word_list = filename.lower().split("_")
        
        # Create pet label by filtering alphabetic words and joining them
        pet_label = " ".join([word for word in word_list if word.isalpha()])
        
        # Add to results dictionary if not already present
        if filename not in results_dic:
            results_dic[filename] = [pet_label.strip()]
        else:
            print(f"** Warning: Duplicate file found: {filename}")

    # Return the results dictionary
    return results_dic
