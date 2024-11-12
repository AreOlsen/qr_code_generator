from uib_inf100_graphics.simple import canvas, display as dsp

def draw_qr(canvas,x_left,y_top,size,qr):
    '''
    Draw the QR code to canvas using the bit list, and information about window size.
    '''

    #Make grid of window.
    cell_size = size/len(qr)

    #Go through all cells.
    for row_i, row in enumerate(qr):
        for column_i, cell in enumerate(row):
            #If cell is filled.
            if cell:
                #Top left of cell.
                x_0 = x_left+column_i*cell_size
                y_0 = y_top+row_i*cell_size

                #Right bottom of cell.
                x_f = x_left+(column_i+1)*cell_size
                y_f = y_top+(row_i+1)*cell_size

                #Draw cell.
                canvas.create_rectangle(x_0,y_0,x_f,y_f, fill="black", outline="")


def display(matrix, width=400,height=400):
    """
    Display the QR code matrix to a window.
    """
    canvas.create_rectangle(0, 0, width, height, fill='white', outline='')
    draw_qr(canvas, 25, 25, width-50, matrix)
    dsp(canvas)