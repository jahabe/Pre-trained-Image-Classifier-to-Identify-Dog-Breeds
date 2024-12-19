#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier  # Importing the classifier function

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares these 
    labels to the pet image labels, and updates the results dictionary with 
    the classifier label and the comparison of the labels.
    Parameters:
     images_dir - The path to the folder of images to be classified (string)
     results_dic - Dictionary with 'key' as image filename and 'value' as a 
                   List. The list contains the following item:
                   index 0 = pet image label (string)
     model - CNN model architecture to use for image classification, 
             values must be either: resnet, alexnet, or vgg (string)
    Returns:
      None - results_dic is mutable so no return needed.
    """
    for filename in results_dic:
        # Full path to the image
        image_path = images_dir + filename

        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)

        # Normalize the classifier label (lowercase and strip whitespace)
        classifier_label = classifier_label.lower().strip()

        # Compare pet image label (index 0) to the classifier label
        pet_label = results_dic[filename][0]

        # Check if pet label is a match within classifier label
        match = 1 if pet_label in classifier_label else 0

        # Add the classifier label and match comparison to the results dictionary
        results_dic[filename].extend([classifier_label, match])
