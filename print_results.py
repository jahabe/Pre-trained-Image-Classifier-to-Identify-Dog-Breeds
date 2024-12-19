#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             

# PROGRAMMER: Jane Choi 
# DATE CREATED: 11/15/2024 
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to print out cases of misclassified
#          dogs and misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
# 

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List:
             (index) idx 0 = pet image label (string)
                     idx 1 = classifier label (string)
                     idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match
                     idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog, 
                            0 = pet image 'is-NOT-a' dog 
                     idx 4 = 1/0 (int)  where 1 = classifier labels image 
                            'as-a' dog, 0 = classifier labels image 'as-NOT-a' dog
                             
      results_stats_dic - Dictionary that contains the results statistics 
                          (either a percentage or a count) where the key is the 
                          statistic's name (starting with 'pct' for percentage 
                          or 'n' for count) and the value is the statistic's value
                          
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images.
              Values must be either: resnet, alexnet, or vgg (string)
              
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)
                             
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool)
                              
    Returns:
           None - simply printing results.
    """
    
    # Print model architecture used
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    
    # Print counts of total images, dog images, and not-a-dog images
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))
    
    # Print percentage statistics
    print("\nSummary Statistics (Percentages):")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):
            print("{:20}: {:5.1f}".format(key, value))
    
    # Print misclassified dogs if requested
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + 
                                 results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        found_misclassified = False
        for key, value in results_dic.items():
            if (value[3] == 1 and value[4] == 0) or (value[3] == 0 and value[4] == 1):
                found_misclassified = True
                print("Pet Label: {:>20}  Classifier Label: {:>30}".format(value[0], value[1]))
        if not found_misclassified:
            print("None found.")
    
    # Print misclassified breeds if requested
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        found_misclassified = False
        for key, value in results_dic.items():
            if (sum(value[3:]) == 2 and value[2] == 0):
                found_misclassified = True
                print("Real: {:>26}   Classifier: {:>30}".format(value[0], value[1]))
        if not found_misclassified:
            print("None found.")
