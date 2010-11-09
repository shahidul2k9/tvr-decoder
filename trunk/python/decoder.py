
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import re
        
class Tag():
    def __init__(self, acronym, field_length, bit_list):
        self.acronym = acronym
        self.field_length = field_length
        self.bit_list = bit_list

tags = {
    'TVR': Tag('TVR', 10, (
    (0x8000000000, 'Offline data authentication was not performed'),
    (0x4000000000, 'SDA failed'),
    (0x2000000000, 'ICC data missing'),
    (0x1000000000, 'Card appears on terminal exception file'),
    (0x0800000000, 'DDA failed'),
    (0x0400000000, 'CDA failed'),
    (0x0080000000, 'ICC and terminal have different application versions'),
    (0x0040000000, 'Expired application'),
    (0x0020000000, 'Application not yet effective'),
    (0x0010000000, 'Requested service not allowed for card product'),
    (0x0008000000, 'New card'),
    (0x0000800000, 'Cardholder verification was not successful'),
    (0x0000400000, 'Unrecognised CVM'),
    (0x0000200000, 'PIN try limit exceeded'),
    (0x0000100000, 'PIN entry required and PIN pad not present or not working'),
    (0x0000080000, 'PIN entry required, PIN pad present, but PIN was not entered'),
    (0x0000040000, 'Online PIN entered'),
    (0x0000008000, 'Transaction exceeds floor limit'),
    (0x0000004000, 'Lower consecutive offline limit exceeded'),
    (0x0000002000, 'Upper consecutive offline limit exceeded'),
    (0x0000001000, 'Transaction selected randomly for online processing'),
    (0x0000000800, 'Merchant forced transaction online'),
    (0x0000000080, 'Default TDOL used'),
    (0x0000000040, 'Issuer authentication failed'),
    (0x0000000020, 'Script processing failed before final GENERATE AC'),
    (0x0000000010, 'Script processing failed after final GENERATE AC'),
    )),
    'TSI': Tag('TSI', 4, (
    (0x8000, 'Offline data authentication was performed'),
    (0x4000, 'Cardholder verification was performed'),
    (0x2000, 'Card risk management was performed'),
    (0x1000, 'Issuer authentication was performed'),
    (0x0800, 'Terminal risk management was performed'),
    (0x0400, 'Script processing was performed'),
    )),
    'AIP': Tag('AIP', 4, (
    (0x4000, 'SDA supported'),
    (0x2000, 'DDA supported'),
    (0x1000, 'Cardholder verification is supported'),
    (0x0800, 'Terminal risk management is to be performed'),
    (0x0400, 'Issuer authentication is supported'),
    (0x0100, 'CDA supported'),
    ))
}
    
def decode(request,tag,value):
    tag = tag.upper()
    errors = is_valid_value(tag, value)
    if len(errors) != 0:
        return render_to_response('errors.html', {
            'errors': errors,
        })

    tag_data = tags[tag]
    set_bits = []
    int_value = int(value, 16)
    for bit in tag_data.bit_list:
        if int_value & bit[0] == bit[0]:
            set_bits.append((('%0' + str(tag_data.field_length) + 'X') % bit[0], bit[1]))
    return render_to_response('results.html', {
        'tags' : set_bits, 'tag' : tag, 'value': value
    })
    

def is_valid_value(tag, value):
    tag_data = tags[tag]
    if tag_data != None and len(value) != tag_data.field_length:
        return '%s must be %d exactly characters long' % (tag, tag_data.field_length)
    if not re.match('^[0-9a-fA-F]+$', value):
        return '%s must contain only hexadecimal characters. ie 0-9 and A-F.' % tag
    return ()

def redirect_to_decode(request):
    return render_to_response('prompt.html', {
        'tags' : (tags['TVR'],tags['TSI'],tags['AIP'])
    })