# Functions that can generate attribute values.
#
# These are functions that can be used in the GenerateFuncAttribute() class
# (see module generator.py). They generate values according to some internal
# functionality.
#
# The requirement of any such functions are:
# 1) that it must return a string
# 2) it can have been 0 and 5 parameters
# 
#
# Examples of such functions are:
# - American telephone numbers
# - Date of Birth (DOB)
# - US social security numbers
# - Credit Card Number
# etc.

# Peter Christen and Dinusha Vatsalan, January-March 2012 
# Modified by Sepideh Mosaferi 05/30/2017
# =============================================================================
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# =============================================================================

import random

import basefunctions

# -----------------------------------------------------------------------------
#
def generate_phone_number_usa():
  """Randomly generate an American telephone number made of a three-digit area
     code and a three-digit and a four-digit numbers (with a "-" between). 
     For example: '301-433-2170'
     For details see: http://www.howtocallabroad.com/usa/ and
                      https://en.wikipedia.org/wiki/Telephone_numbers_in_the_Americas
  """
  
  area_code = random.choice(['205', '251', '256', '334', '938',
                             '907', '480', '520', '602', '623',
                             '928', '479', '501', '870', '209', 
                             '213', '310', '323', '408', '415', 
                             '424', '442', '510', '530', '559', 
                             '562', '619', '626', '628', '650', 
                             '657', '661', '669', '707', '714', 
                             '760', '805', '818', '831', '858', 
                             '909', '916', '925', '949', '951',
                             '303', '719', '720', '970', '203', 
                             '475', '860', '959', '302', '239', 
                             '305', '321', '352', '386', '407', 
                             '561', '727', '754', '772', '786', 
                             '813', '850', '863', '904', '941', 
                             '954', '229', '404', '470', '478',  
                             '678', '706', '762', '770', '912',
                             '808', '208', '217', '224', '309', 
                             '312', '331', '618', '630', '708', 
                             '773', '815', '847', '872', '219', 
                             '260', '317', '574', '765', '812', 
                             '930', '319', '515', '563', '641', 
                             '712', '316', '620', '785', '913',
                             '270', '364', '502', '606', '859',
                             '225', '318', '337', '504', '985',
                             '339', '351', '413', '508', '617', 
                             '774', '781', '857', '978', '240', 
                             '301', '410', '443', '667', '207',
                             '231', '248', '269', '313', '517', 
                             '586', '616', '734', '810', '906', 
                             '947', '989', '218', '320', '507', 
                             '612', '651', '763', '952', '314', 
                             '417', '573', '636', '660', '816',
                             '228', '601', '662', '769', '406',
                             '252', '336', '704', '828', '910', 
                             '919', '980', '984', '701', '308', 
                             '402', '531', '603', '201', '551', 
                             '609', '732', '848', '856', '862',
                             '908', '973', '505', '575', '702', 
                             '725', '775', '212', '315', '347', 
                             '516', '518', '585', '607', '631', 
                             '646', '716', '718', '845', '914', 
                             '917', '929', '216', '220', '234', 
                             '330', '380', '419', '440', '513', 
                             '567', '614', '740', '937', '405',
                             '539', '580', '918', '458', '503', 
                             '541', '971', '215', '267', '272',
                             '412', '484', '570', '610', '717', 
                             '724', '814', '878', '401', '803',
                             '843', '854', '864', '605', '423', 
                             '615', '629', '731', '865', '901', 
                             '931', '210', '214', '254', '281', 
                             '325', '346', '361', '409', '430',
                             '432', '469', '512', '682', '713', 
                             '806', '817', '830', '832', '903', 
                             '915', '936', '940', '956', '972', 
                             '979', '385', '435', '801', '276', 
                             '434', '540', '571', '703', '757', 
                             '804', '802', '206', '253', '360',
                             '425', '509', '202', '262', '414', 
                             '534', '608', '715', '920', '304', '307'])

  number1 = random.randint(1,999)
  number2 = random.randint(1,9999)

  oz_phone_str = str(area_code)+'-'+str(number1).zfill(3)+'-'+ \
                 str(number2).zfill(4)
  assert len(oz_phone_str) == 12

  return oz_phone_str

# -----------------------------------------------------------------------------
#
def generate_date_of_birth():
  """Randomly generate a dob made of two two-digit numbers and one 
     four digit number (with a "/" between each number group). 
     For example: '01/29/1990' 'month/day/year'
  """

  number1 = random.randint(01,12)
  assert number1 > 0

  number2 = random.randint(01,30)
  assert number2 > 0

  number3 = random.randint(1947,1997)
  assert number3 > 0

  cc_str = str(number1).zfill(2)+'/'+str(number2).zfill(2)+'/'+ \
           str(number3).zfill(4)

  assert len(cc_str) == 10

  return cc_str

# -----------------------------------------------------------------------------
#
def generate_social_security_number():
  """Randomly generate a SSN made of one three-digit numbers and one 
     two-digit numbers and one four-digit numbers (with a "-" between each number group). 
     The SSN is nine-digit number in the format "AAA-GG-SSSS".
     For more information see
     https://en.wikipedia.org/wiki/Social_Security_number and
     https://en.wikipedia.org/wiki/List_of_Social_Security_Area_Numbers
  """

  number1 = random.randint(001,728)
  assert number1 > 0

  number2 = random.randint(01,99)
  assert number2 > 0

  number3 = random.randint(0001,9999)
  assert number3 > 0

  cc_str = str(number1).zfill(3)+'-'+str(number2).zfill(2)+'-'+ \
           str(number3).zfill(4)

  assert len(cc_str) == 11

  return cc_str

# -----------------------------------------------------------------------------
#
def generate_credit_card_number():
  """Randomly generate a credit card made of four four-digit numbers (with a
     space between each number group). For example: '1234 5678 9012 3456'

     For details see: http://en.wikipedia.org/wiki/Bank_card_number
  """

  number1 = random.randint(1,9999)
  assert number1 > 0

  number2 = random.randint(1,9999)
  assert number2 > 0

  number3 = random.randint(1,9999)
  assert number3 > 0

  number4 = random.randint(1,9999)
  assert number4 > 0

  cc_str = str(number1).zfill(4)+' '+str(number2).zfill(4)+' '+ \
           str(number3).zfill(4)+' '+str(number4).zfill(4)

  assert len(cc_str) == 19

  return cc_str

# -----------------------------------------------------------------------------
#
def generate_uniform_value(min_val, max_val, val_type):
  """Randomly generate a numerical value according to a uniform distribution
     between the minimum and maximum values given.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.

     Note that for certain situations and string formats a value outside the
     set range might be returned. For example, if min_val=100.25 and
     val_type='float1' the rounding can result in a string value '100.2' to
     be returned.

     Suitable minimum and maximum values need to be selected to prevent such a
     situation.
  """

  basefunctions.check_is_number('min_val', min_val)
  basefunctions.check_is_number('max_val', max_val)
  assert min_val < max_val

  r = random.uniform(min_val, max_val)

  return basefunctions.float_to_str(r, val_type)

# -----------------------------------------------------------------------------

def generate_normal_value(mu, sigma, min_val, max_val, val_type):
  """Randomly generate a numerical value according to a normal distribution
     with the mean (mu) and standard deviation (sigma) given.

     A minimum and maximum allowed value can given as additional parameters,
     if set to None then no minimum and/or maximum limit is set.

     The value type can be set as 'int', so a string formatted as an integer
     value is returned; or as 'float1' to 'float9', in which case a string
     formatted as floating-point value with the specified number of digits
     behind the comma is returned.
  """

  basefunctions.check_is_number('mu', mu)
  basefunctions.check_is_number('sigma', sigma)
  assert sigma > 0.0

  if (min_val != None):
    basefunctions.check_is_number('min_val', min_val)
    assert min_val <= mu

  if (max_val != None):
    basefunctions.check_is_number('max_val', max_val)
    assert max_val >= mu

  if ((min_val != None) and (max_val != None)):
    assert min_val < max_val

  if (min_val != None) or (max_val != None):
    in_range = False  # For testing if the random value is with the range
  else:
    in_range = True

  r = random.normalvariate(mu, sigma)

  while (in_range == False):
    if ((min_val == None) or ((min_val != None) and (r >= min_val))):
      in_range = True

    if ((max_val != None) and (r > max_val)):
      in_range = False

    if (in_range == True):
      r_str = basefunctions.float_to_str(r, val_type)
      r_test = float(r_str)
      if (min_val != None) and (r_test < min_val):
        in_range = False
      if (max_val != None) and (r_test > max_val):
        in_range = False

    if (in_range == False):
      r = random.normalvariate(mu, sigma)

  if (min_val != None):
    assert r >= min_val
  if (max_val != None):
    assert r <= max_val

  return basefunctions.float_to_str(r, val_type)


# =============================================================================

# If called from command line perform some examples: Generate values
#
if (__name__ == '__main__'):

  num_test = 20

  print 'Generate %d American telephone numbers:' % (num_test)
  for i in range(num_test):
    print ' ', generate_phone_number_usa()
  print

  print 'Generate %d date of births:' % (num_test)
  for i in range(num_test):
    print ' ', generate_date_of_birth()
  print

  print 'Generate %d social security number:' % (num_test)
  for i in range(num_test):
    print ' ', generate_social_security_number()
  print

  print 'Generate %d credit card numbers:' % (num_test)
  for i in range(num_test):
    print ' ', generate_credit_card_number()
  print

  print 'Generate %d uniformly distributed integer numbers between -100' % \
        (num_test) + ' and -5:'
  for i in range(num_test):
    print ' ', generate_uniform_value(-100, -5, 'int'),
  print

  print 'Generate %d uniformly distributed floating-point numbers with ' % \
        (num_test) + '3 digits between -55 and 55:'
  for i in range(num_test):
    print ' ', generate_uniform_value(-55, 55, 'float3')
  print

  print 'Generate %d uniformly distributed floating-point numbers with ' % \
        (num_test) + '7 digits between 147 and 9843:'
  for i in range(num_test):
    print ' ', generate_uniform_value(147, 9843, 'float7')
  print

  print 'Generate %d normally distributed integer numbers between -200' % \
        (num_test) + ' and -3 with mean -50 and standard deviation 44:'
  for i in range(num_test):
    print ' ', generate_normal_value(-50, 44, -200, -3, 'int')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '5 digits between -100 and 100 and with mean 22 and ' + \
        'standard deviation 74:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, -100, 100, 'float5')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '9 digits with mean 22 and standard deviation 74:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=None, max_val= None,
                                     val_type='float9')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '2 digits with mean 22 and standard deviation 24 that' + \
        ' are larger than 10:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=10, max_val=None,
                                     val_type='float2')
  print

  print 'Generate %d normally distributed floating-point numbers with ' % \
        (num_test) + '4 digits with mean 22 and standard deviation 24 that' + \
        ' are smaller than 30:'
  for i in range(num_test):
    print ' ', generate_normal_value(22, 74, min_val=None, max_val=40,
                                     val_type='float4')
  print

