###############################################################################
# This is a small script created to convert the headlines in wiki chapters
# into links. In order to use it copy and paste the headline to convert in
# link inside the frame of the app. If the headline is a main headline, add '+'
# in front of it. Hit convert and the resulting string will be automatically
# added in your clipboard.

### Author: Ioan-Matei Sarivan @ Anybody Technology A/S
### ms@anybodytech.com

############################www.anybodytech.com################################


import tkinter


class Manip(object):

    def __init__(self):

        self.__frame = tkinter.Tk()
        self.__text = tkinter.Text(self.__frame)
        self.__text.pack()
        self.__button = tkinter.Button(self.__frame, text='Convert',
                                       command=self._on_convert)
        self.__button.pack()
        self.__frame.mainloop()

    def _on_convert(self):

        string = self.__text.get('1.0', 'end-1c')
        self.__text.delete('1.0', 'end')

        print(string)

        if string[0] == '+':
            resulted_string = '+ ['
            string = string[1:]
            resulted_string = resulted_string + string+'](#'

        else:
            resulted_string = '    - ['
            resulted_string = resulted_string+string+'](#'

        string = string.lower()

        for index in range(0, len(string)):
            char = string[index]

            if not char.isalpha():
                if char == ' ' or char == '-':
                    char = '-'
                    resulted_string = resulted_string + char

            else:
                resulted_string = resulted_string+char

        resulted_string = resulted_string+')'

        self.__frame.clipboard_clear()
        self.__frame.clipboard_append(resulted_string)

        print(resulted_string)


if __name__ == '__main__':

    app = Manip()
