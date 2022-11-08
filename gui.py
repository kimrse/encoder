import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import encryption


root = tk.Tk()
root.title('Blowfish')
root.geometry('500x250')
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)

main_frame = ttk.Frame(root)
padding = {'padx': 5, 'pady': 5}


txt_label = ttk.Label(main_frame, text='Исходный текст:')
txt_label.grid(column=0, row=0, sticky='w', **padding)

key_label = ttk.Label(main_frame, text='Ключ шифрования:')
key_label.grid(column=0, row=1, sticky='w', **padding)

txt_input = tk.StringVar()
key_input = tk.StringVar()

txt_entry = ttk.Entry(main_frame, width=45, textvariable=txt_input)
txt_entry.grid(column=1, row=0, **padding)
txt_entry.focus()

key_entry = ttk.Entry(main_frame, width=45, textvariable=key_input)
key_entry.grid(column=1, row=1, **padding)


def encrypt_btn_clicked():
    try:
        output_txt.delete('1.0','end')
        txt = txt_input.get()
        key = key_input.get()
        cipher_txt = encryption.main(txt, key)
        output_txt.insert('1.0', cipher_txt['txt_bytes'])
    except ValueError as error:
        showerror(title='Error', message=error)


encrypt_btn = ttk.Button(main_frame, text='Зашифровать')
encrypt_btn.grid(column=1, row=3, sticky='wesn', **padding)
encrypt_btn.configure(command=encrypt_btn_clicked)

# result label
output_label = ttk.Label(main_frame, text='Вывод:')
output_label.grid(column=0, row=4, sticky='w')
output_txt = tk.Text(main_frame, height=5, width=52)
output_txt.grid(column=0, row=5, rowspan=1, columnspan=3)


# add padding to the main_frame and show it
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid(padx=10, pady=10)

# start the app
root.mainloop()


