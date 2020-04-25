# generate-data.py - Python module to generate synthetic data based on
#                    look-up files and error tables for JPSM Record Linkage course.
#
# The original program with some attributes was written by Peter Christen
# and Dinusha Vatsalan in January-March 2012.
# Modified by Sepideh Mosaferi 07/01/2017.
# =============================================================================
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# =============================================================================

# Import the necessary other modules of the data generator
#
import basefunctions  # Helper functions
import attrgenfunct   # Functions to generate independent attribute values
import generator      # Main classes to generate records and the data set
import corruptor      # Main classes to corrupt attribute values and records

import random
random.seed(42)  # Set seed for random generator, so data generation can be
                 # repeated

# Set the Unicode encoding for this data generation project. This needs to be
# changed to another encoding for different Unicode character sets.
# Valid encoding strings are listed here:
# http://docs.python.org/library/codecs.html#standard-encodings
#
unicode_encoding_used = 'ascii'

# The name of the record identifier attribute (unique value for each record).
# This name cannot be given as name to any other attribute that is generated.
#
rec_id_attr_name = 'ID'

# Set the file name of the data set to be generated (this will be a comma
# separated values, CSV, file).
#
out_file_name = 'synth-data.csv'

# Set how many original and how many duplicate records are to be generated.
#
num_org_rec = 3000
num_dup_rec = 1200  #40% duplicates

# Set the maximum number of duplicate records can be generated per original
# record.
#
max_duplicate_per_record = 1

# Set the probability distribution used to create the duplicate records for one
# original record (possible values are: 'uniform', 'poisson', 'zipf').
#
num_duplicates_distribution = 'zipf'

# Set the maximum number of modification that can be applied to a single
# attribute (field).
#
max_modification_per_attr = 1

# Set the number of modification that are to be applied to a record.
#
num_modification_per_record = 4

# Check if the given the unicode encoding selected is valid.
#
basefunctions.check_unicode_encoding_exists(unicode_encoding_used)

# -----------------------------------------------------------------------------
# Define the attributes to be generated (using methods from the generator.py
# module).
#
gname_attr = \
    generator.GenerateFreqAttribute(attribute_name = 'First Name',
                          freq_file_name = 'lookup-files/givenname-freq.csv',
                          has_header_line = False,
                          unicode_encoding = unicode_encoding_used)

sname_attr = \
    generator.GenerateFreqAttribute(attribute_name = 'Last Name',
                          freq_file_name = 'lookup-files/surname-freq.csv',
                          has_header_line = False,
                          unicode_encoding = unicode_encoding_used)

gender_marital_status_comp_attr = \
    generator.GenerateCateCateCompoundAttribute(\
          categorical1_attribute_name = 'Gender',
          categorical2_attribute_name = 'Marital Status',
          lookup_file_name = 'lookup-files/gender-maritalstatus.csv',
          has_header_line = True,
          unicode_encoding = 'ascii')

race_attr = \
    generator.GenerateFreqAttribute(attribute_name = 'Race',
                          freq_file_name = 'lookup-files/race-freq.csv',
                          has_header_line = False,
                          unicode_encoding = unicode_encoding_used)

date_of_birth_attr =  \
    generator.GenerateFuncAttribute(attribute_name = 'DOB',
                       function = attrgenfunct.generate_date_of_birth)

social_security_number_attr =  \
    generator.GenerateFuncAttribute(attribute_name = 'SSN',
                       function = attrgenfunct.generate_social_security_number)

sex_income_comp_attr = \
    generator.GenerateCateContCompoundAttribute(\
          categorical_attribute_name = 'Sex',
          continuous_attribute_name = 'Income',
          continuous_value_type = 'float1',
          lookup_file_name = 'lookup-files/gender-income.csv',
          has_header_line = False,
          unicode_encoding = 'ascii')

credit_card_attr =  \
    generator.GenerateFuncAttribute(attribute_name = 'Credit Card Number',
                       function = attrgenfunct.generate_credit_card_number)

#city_state_attr = \
#   generator.GenerateFreqAttribute(attribute_name = 'City State',
#                        freq_file_name = 'lookup-files/city-state-freq.csv',
#                       has_header_line = False,
#                      unicode_encoding = unicode_encoding_used)

zipcode_attr = \
    generator.GenerateFreqAttribute(attribute_name = 'ZIP Code',
                          freq_file_name = 'lookup-files/zipcode-freq.csv',
                          has_header_line = False,
                          unicode_encoding = unicode_encoding_used)

phone_num_attr = \
    generator.GenerateFuncAttribute(attribute_name = 'Telephone Number',
                       function = attrgenfunct.generate_phone_number_usa)

# -----------------------------------------------------------------------------
# Define how the generated records are to be corrupted (using methods from
# the corruptor.py module).

# For a value edit corruptor, the sum or the four probabilities given must
# be 1.0.
#
edit_corruptor = \
    corruptor.CorruptValueEdit(\
          position_function = corruptor.position_mod_normal,
          char_set_funct = basefunctions.char_set_ascii,
          insert_prob = 0.5,
          delete_prob = 0.5,
          substitute_prob = 0.0,
          transpose_prob = 0.0)

edit_corruptor2 = \
    corruptor.CorruptValueEdit(\
          position_function = corruptor.position_mod_uniform,
          char_set_funct = basefunctions.char_set_ascii,
          insert_prob = 0.25,
          delete_prob = 0.25,
          substitute_prob = 0.25,
          transpose_prob = 0.25)

givenname_misspell_corruptor = \
    corruptor.CorruptCategoricalValue(\
          lookup_file_name = 'lookup-files/givenname-misspell.csv',
          has_header_line = False,
          unicode_encoding = unicode_encoding_used)

surname_misspell_corruptor = \
    corruptor.CorruptCategoricalValue(\
          lookup_file_name = 'lookup-files/surname-misspell.csv',
          has_header_line = False,
          unicode_encoding = unicode_encoding_used)

ocr_corruptor = corruptor.CorruptValueOCR(\
          position_function = corruptor.position_mod_normal,
          lookup_file_name = 'lookup-files/ocr-variations.csv',
          has_header_line = False,
          unicode_encoding = unicode_encoding_used)

keyboard_corruptor = corruptor.CorruptValueKeyboard(\
          position_function = corruptor.position_mod_normal,
          row_prob = 0.5,
          col_prob = 0.5)

phonetic_corruptor = corruptor.CorruptValuePhonetic(\
          lookup_file_name = 'lookup-files/phonetic-variations.csv',
          has_header_line = False,
          unicode_encoding = unicode_encoding_used)

missing_val_corruptor = corruptor.CorruptMissingValue()

zipcode_missing_val_corruptor = corruptor.CorruptMissingValue(\
       missing_val='missing')

given_name_missing_val_corruptor = corruptor.CorruptMissingValue(\
       missing_value='unknown')

# -----------------------------------------------------------------------------
# Define the attributes to be generated for this data set, and the data set
# itself.
#
attr_name_list = ['First Name', 'Last Name', 'Marital Status', 'Race', 
                  'DOB', 'SSN', 'Income', 'Credit Card Number', 
                  'ZIP Code', 'Telephone Number']

attr_data_list = [gname_attr, sname_attr, gender_marital_status_comp_attr,
                  race_attr, date_of_birth_attr, social_security_number_attr, 
                  sex_income_comp_attr, credit_card_attr, zipcode_attr, phone_num_attr]

# Nothing to change here - set-up the data set generation object.
#
test_data_generator = generator.GenerateDataSet(output_file_name = \
                                          out_file_name,
                                          write_header_line = True,
                                          rec_id_attr_name = rec_id_attr_name,
                                          number_of_records = num_org_rec,
                                          attribute_name_list = attr_name_list,
                                          attribute_data_list = attr_data_list,
                                          unicode_encoding = \
                                                         unicode_encoding_used)

# Define the probability distribution of how likely an attribute will be
# selected for a modification.
# Each of the given probability values must be between 0 and 1, and the sum of
# them must be 1.0.
# If a probability is set to 0 for a certain attribute, then no modification
# will be applied on this attribute.
#
attr_mod_prob_dictionary = {'First Name':0.1, 'Last Name':0.1, 
                            'Marital Status':0.05, 'Race':0.1, 
                            'DOB':0.15, 'SSN':0.11,
                            'Income':0.15, 'Credit Card Number':0.16,
                            'ZIP Code':0.0, 
                            'Telephone Number':0.08}

# Define the actual corruption (modification) methods that will be applied on
# the different attributes.
# For each attribute, the sum of probabilities given must sum to 1.0.
#
attr_mod_data_dictionary = {'First Name':[(0.1, givenname_misspell_corruptor),
                                          (0.1, edit_corruptor2),
                                          (0.1, ocr_corruptor),
                                          (0.1, keyboard_corruptor),
                                          (0.6, phonetic_corruptor)],
                            'Last Name':[(0.1, surname_misspell_corruptor),
                                         (0.1, ocr_corruptor),
                                         (0.1, keyboard_corruptor),
                                         (0.7, phonetic_corruptor)],
                            'Marital Status':[(1.0, missing_val_corruptor)],
                            'Race':[(1.0, missing_val_corruptor)],
                            'DOB':[(1.0, edit_corruptor2)],
                            'SSN':[(0.4, edit_corruptor),
                                   (0.6, missing_val_corruptor)],
                            'Income':[(0.4, edit_corruptor),
                                      (0.6, missing_val_corruptor)],
                            'Credit Card Number':[(1.0, edit_corruptor)],
                            'ZIP Code':[(0.8, keyboard_corruptor),
                                        (0.2, zipcode_missing_val_corruptor)],
                            'Telephone Number':[(1.0, missing_val_corruptor)]}

# Nothing to change here - set-up the data set corruption object
#
test_data_corruptor = corruptor.CorruptDataSet(number_of_org_records = \
                                          num_org_rec,
                                          number_of_mod_records = num_dup_rec,
                                          attribute_name_list = attr_name_list,
                                          max_num_dup_per_rec = \
                                                 max_duplicate_per_record,
                                          num_dup_dist = \
                                                 num_duplicates_distribution,
                                          max_num_mod_per_attr = \
                                                 max_modification_per_attr,
                                          num_mod_per_rec = \
                                                 num_modification_per_record,
                                          attr_mod_prob_dict = \
                                                 attr_mod_prob_dictionary,
                                          attr_mod_data_dict = \
                                                 attr_mod_data_dictionary)

# =============================================================================
# No need to change anything below here

# Start the data generation process
#
rec_dict = test_data_generator.generate()

assert len(rec_dict) == num_org_rec  # Check the number of generated records

# Corrupt (modify) the original records into duplicate records
#
rec_dict = test_data_corruptor.corrupt_records(rec_dict)

assert len(rec_dict) == num_org_rec+num_dup_rec # Check total number of records

# Write generate data into a file
#
test_data_generator.write()

# End.
# =============================================================================
