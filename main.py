import json
from pathlib import Path
from draw import display
from masking import get_refined_matrix
from zig_zag import bit_list_to_raw_matrix
from bit_lists import string_to_bit_list


def get_qr_matrix(content_string):
    '''
    Turns a pure string into the QR bit matrix.
    This is the QR code that is scanned when shown on the screen.
    '''

    qr_layout = json.loads(Path('qrv2_layout.json').read_text(encoding='utf-8'))
    bit_list, err_corr = string_to_bit_list(content_string, qr_layout)
    raw_matrix = bit_list_to_raw_matrix(bit_list, qr_layout)
    matrix = get_refined_matrix(raw_matrix, err_corr, qr_layout)
    return matrix


###
#   SHOW THE QR CODE IN A NEW WINDOW.
### 
def qr_code(url='https://areolsen.no/'):
        qr_matrix = get_qr_matrix(url)
        display(qr_matrix)


if __name__ == '__main__':
    qr_code()