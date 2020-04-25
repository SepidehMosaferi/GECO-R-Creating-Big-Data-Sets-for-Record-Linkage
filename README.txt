======================================
= README
======================================

*Description of Data Sets for Record Linkage Practice*
Author: Sepideh Mosaferi; Sep. 2017

Contents
1. Intro to GeCo
2. Five Related Modules
3. Created Data Sets with GeCo and R
4. Data Sets and Selection Process
5. Creation of Attributes
6. Creataion of Errors
7. Purpose of Record Linkage Practice

======================================
1. Intro to GeCo
======================================

GeCo (A Data Generator and Corruptor) is an open source Python code available at https:
//dmm.anu.edu.au/geco/index.php, which is capable of producing data set suitable for the record
linkage. One the web page, there is an online version of data generator, but it has limited features in
a special format. In order to change the program in a way that we are interested in, we downloaded
the original source code under the name of geco-data-generator-corruptor.tar.gz from the top of
introduced webpage. Then, we applied all of the necessary changes into the source code.

The software is capable of receiving frequency tables for independent attributes such as given
name, last name, etc. Its data generator can be mostly used as the auxiliary program in conjunction
with others (in our case with R software). We could also define variety of errors or modifications
such as: typographical error, OCR (Optical Character Recognition) error, or phonetical error by
adding Python codes and some frequency tables, which will be explained later.

The program is capable of using three distributions for duplicating the records such as: Uniform,
Zipf, and Poisson: these are the most usable distributions for occuring an event if we define the
event as occurance of duplication. If we assume a same seed for a particular distribution, we are
capable of replicating our experiment in order to receive the exact previous generated data. In
addition, if we use different distributions (but with the same seed) for duplications, the synthesized
data sets are nearly similar.

The original GeCo package contains a ‘look-up files’ folder, ‘tests’ folder, five dependent modules
which are re-called in the main program under the name generate-data-english.py. There are some
other files that we recommend a user to read before implementation 1 . In the ‘look-up files’ folder
we could put different frequency tables for given names, last names, cities, etc. based on the
attributes that we are interested in, and in the modules we explain how things should work.

======================================
2. Five Related Modules
======================================

As we mentioned earlier, the main code depends upon five modules that we provide a brief intro-
duction to them here.

* attrgenfunct: This module is for generating attributes. It can generate phone numbers, credit
card numbers, and other sort of numerical variables.

* basefunctions: This module is for the purpose of providing basic functionality. These func-
tions are for checking the type and range of variables, how to read a “.csv” file with a comma
as a separator among the values, and how to write a “.csv” file by exporting the generated
dataset.

* contdepfunct: This module is for producing dependent attributes such as “salary and age”,
etc. This module has been removed in our process of creating data set as it is not handy and
requires improvements for preserving real dependency.

* corruptor: This module is for corrupting and modifying attributes to define how to apply a
modification, necessary classes, corrupting missing values, and OCR errors which are related
to the optical errors.

* generator: This module is for generating single and compound attributes.

Note: In the modified GeCo, we only keep the four modules attrgenfunct.py, basefunctions.py, cor-
ruptor.py, and generator.py and apply related changes. The main Python code is called generate-
data.py, which conatins codes for generating data– so-called “generate-data-english.py” in the orig-
inal package from the web page.

We also need to keep in mind that we cannot give a whole real dataset to the program as an
in-put. So, if we have a data set in hand, we first need to extract the frequency tables of attributes,
and then give them to the program as an input in the lookup-files folder. Therefore, we might
not be able to define all of dependencies which might occur among attributes as it needs a high
dimensional cross products among all values of attributes. In statistical terminology, we cannot
give the joint distribution of all attributes to the program. We could mainly give a marginal
distribution of attributes and some reasonable number of joint distribution for attributes. Mostly
the joint distribution with given name or surname is unlikely feasible.

======================================
3. Created Data Sets with GeCo and R
======================================

For this study, we have created two data sets: administrative data and survey data. We explicitly
focus on 5 cities: Chicago, Washington DC, Los Angeles, Austin, and New York City. For each
city, we consider upto 20 unique zipcodes listed under zipcode-freq.csv in the lookup-folder, which
could be helpful for the process of making blocks in the record linkage.

======================================
4. Data Sets and Selection Process
======================================

As the process of creating dependent attributes looks inconvenient, we first created a separate data
set for each city with following features. Then we merged the created data sets.

1. For each city, we assign the size of original records equal to 3000, which is [num-org-rec=3000 ]
in the generate-data.py. Then we assign the number of duplications equal to 1200, which is
[num-dup-rec=1200 ] (40% of original records) in the generate-data.py. Therefore, the output
contains 4,200 individuals per city.

2. We consider the maximum number of duplications per record equals to 1 [max-duplicate-per-
record = 1 ] in the generate-data.py.

3. We consider the Zipf distribution for the distribution of duplications.

4. We assing the maximum modification per attribute equals to 1 [num-modification-per-attr=1 ]
and the total number of modifications per record equals to 4 [num-modification-per-record=4 ]
in the generate-data.py.

After creation of five data sets, we merge them and we have a large data set so-called FinalDATA
(see the R code) and contains 21,000 records. We assign IDs to individuals in which the first digit
of ID is associated to the city. The ID creation has been done by GeCo and R. IDs are unique per
individual, for example Kate Ryan who has been duplicated once, has only one unique ID 10003
assigned to her. Then the DUP variable in the data set determines whether a person (for e.g.
Kate here) has been duplicated or not.

DUP =
 1 if record duplicated
 0 otherwise

To explain the IDs more, we have:
• 1...: Washington DC;
• 2...: Los Angeles;
• 3...: Chicago;
• 4...: New York City;
• 5...: Austin.
ID is useful to check whether the process of record linkage with a specific method has been appro-
priately or not.

[[Administrative Data]]
From the FinalDATA, we only explicitly select individuals without replications. Therefore the size
of data is 15,000 (3000 × 5), in which we have 3000 unique individuals per city.

[[Survey Data]]
From the Administrative records, we select a simple random sample without replacement with
the size of 3000. Then from the FinalDATA, we find records who have the same IDs with ones
selected in the process of simple random selection. Therefore, the Survey data contains 3000 unique
individuals plus their replications, which might only occured for some of the individuals. We refer
a reader to the R code for further information:

> Survey_pre <- Administrative[sample(nrow(Administrative),3000),]
> Survey <- FinalDATA[FinalDATA$ID %in% Survey_pre$ID,]

======================================
5. Creation of Attributes
======================================

We have created 11 attributes as follows:
• First Name: This attribute comes from “givenname-freq.csv” in the “lookup-files” folder. It
can accept following errors in which the summation of probabilities equals to 1 2 .
[(0.1,givenname_misspell_corruptor),
(0.1,edit_corruptor2),(0.1,ocr_corruptor),
(0.1,keyboard_corruptor),(0.6,phonetic_corruptor)]
For misspelling the first names, we can use the “givenname-misspell.csv” in the “lookup-files”
folder.
• Last Name: This attribute comes from “givenname-freq.csv” in the “lookup-files folder”. It
can accept the following errors:
[(0.1,surname_misspell_corruptor),
(0.1,ocr_corruptor),(0.1,keyboard_corruptor),
(0.7,phonetic_corruptor)]
For misspelling the last names, we can use the “givenname-misspell.csv” in the “lookup-files”
folder.
• Marital Status: This attribute comes from “gender-maritalstatus.csv” in the “lookup-files”
folder. We assigned the following error to it:
[(1.0,missing_val_corruptor)]
• Race: This attribute comes from “race-freq.csv” in the “lookup-files” folder. We assigned the
following error to it:
[(1.0,missing_val_corruptor)]
• DOB: This attribute can be defined in the “attrgenfunct.py” module with the following chuck
code:
def generate_date_of_birth()
We randomly generate a DOB made of two two-digit numbers and one four digit number
(with a “/” between each number group). For example: ‘01/29/1990’ ‘month/day/year’. It
can also receive the following common error:
[(1.0, edit_corruptor2)]
• SSN: This attribute can be defined in the “attrgenfunct.py” module under the following chunk
of code:
def generate_social_security_number()
We randomly generate a SSN made of one three-digit numbers and one two-digit numbers
and one four-digit numbers (with a “-” between each number group). The SSN is nine-digit
number in the format “AAA-GG-SSSS”. We have assigned the following errors to it:
[(0.4, edit_corruptor),(0.6, missing_val_corruptor)]
• Income: This attribute can be generated from “gender-income.csv” in the “lookup-files” folder.
It can also receive the following usual errors:
[(0.4, edit_corruptor),(0.6, missing_val_corruptor)]
• Credit Card Number: This attributte can be defined in “attrgenfunct.py” module. The chunk
of code which can produce it is:
def generate_credit_card_number()
It can also receive the most common error as follows:
[(1.0, edit_corruptor)]
• City: We did not consider any errors for this particular attribute as it could be used for the
blocking variable in the record linkage.
• ZIP Code: The information for generating ZIP codes come from “zipcode-freq.csv” in the
“lookup-files” folder. It can also receive the following common errors:
[(0.8, keyboard_corruptor), (0.2, zipcode_missing_val_corruptor)]
• Telephone Number: This attribute can be defined in “attrgenfunct.py” with the following
chunk code:
def generate_phone_number_usa()
We randomly generate an American telephone number made of a three-digit area code and a
three-digit and a four-digit numbers (with a “-” between). For example: ‘301-345-2192’. We
also considered the following error for it:
[(1.0, missing_val_corruptor)]

======================================
6. Creataion of Errors
======================================

The errors that we have considered for attributes are based on the most common ones occur in the
real life. For example, the misspelled error is more likely to occur for a first name or a last name
rather than an income attribute. While it is more common for income attribute to receive more
missing values. The amount of probabilities assigned for each type of error related to an attribute
can be defined in the generate-data.py and should be sum up to 1.
The errors used for attributes 3 are:
• OCR error: Optical Character Recognition error occurs in the process of converting scanned
images of letters and words into a electronic versions. Detailed of errors are in“ocr-variations.csv”
in the “lookup-files” folder.
• Phonetic variation error: This error is related to the speech sound disorders. Further infor-
mation is in “phonetic-variations.csv” in the “lookup-files” folder.
• Misspelled errors: This error usually occurs in first and last names. The information related
to the different sorts of misspelled names are in “surname-misspell.csv” and “givenname-
misspell.csv” in the “lookup-files” folder.
• Edit Corruptor error: This error is related to how letters of a word can be transposed, deleted,
substituted, or inserted. We have defined two special edit corruptor errors in “generate-
data.py” under the names edit-corruptor and edit-corruptor2.
• Keyboard Corruptor error: This error explains how likely an error in typing occurs using
the keyboard of computer. This error is defined in “generate-data.py” under the name of
keyboar-corruptor.
• missing values: This error defines a situation in which the value of an attribute has not been
reported. The error is listed in “generate-data.py”.

======================================
7. Purpose of Record Linkage Practice
======================================

In this practice, we can match the records from the Survey data to the Administrative records.
The RecordLinkage package in R https://cran.r-project.org/web/packages/RecordLinkage/
index.html can be used for this purpose. There are sufficient documents on CRAN which explain
how to use the record linkage package. We could consider city, or combination of city with
the initial of last name as blocking variable. Then, we can consider different kinds of blocking variables
and compare the results. In addition, different values of threshold in the record linkage can be
considered and the results can be compared. We may want to be innovative and consier other kinds of
thoughts or parameters for conducting the record linkage process. The results could be evaluated
through unique IDs as they have been provided in the data sets.

Note: The GeCo original package has been created by Khoi-Nguyen Tran, Dinusha Vatsalan, and Peter Christen in 2005.



