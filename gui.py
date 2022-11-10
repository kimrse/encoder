import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import encryption


#500x250
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
        combobox.current(0)
        output_txt.delete('1.0','end')
        txt = txt_input.get()
        key = key_input.get()
        cipher_txt = encryption.main(txt, key)
        output_txt.insert('1.0', cipher_txt['encrypted_iso'])
        return cipher_txt
    except ValueError as error:
        showerror(title='Error', message=error)


def combo_select(event):
    try:
        selection = combobox.get()
        cipherd_txt = encrypt_btn_clicked()
        output_txt.delete('1.0','end')
        
        if selection == combo_opt[0]:
            combobox.current(0)
            output_txt.insert('1.0', cipherd_txt['encrypted_iso'])
        elif selection == combo_opt[1]:
            combobox.current(1)
            output_txt.insert('1.0', cipherd_txt['txt_bits'])
        elif selection == combo_opt[2]:
            combobox.current(2)
            output_txt.insert('1.0', cipherd_txt['txt_bytes'])
        elif selection == combo_opt[3]:
            combobox.current(3)
            output_txt.insert('1.0', cipherd_txt['encrypted_bits'])
        elif selection == combo_opt[4]:
            combobox.current(4)
            output_txt.insert('1.0', cipherd_txt['encrypted_bytes'])
            
    except ValueError as error:
        showerror(title='Error', message=error)


encrypt_btn = ttk.Button(main_frame, text='Зашифровать')
encrypt_btn.grid(column=1, row=3, sticky='wesn', **padding)
encrypt_btn.configure(command=encrypt_btn_clicked)

output_label = ttk.Label(main_frame, text='Вывод:')
output_label.grid(column=0, row=4, sticky='w')
output_txt = tk.Text(main_frame, height=5, width=50)
output_txt.grid(column=0, row=5, rowspan=1, columnspan=3)

combo_opt = ['Зашифрованный текст', 'Исходный текст в битах',
            'Исходный текст в байтах', 'Зашифрованный текст в битах', 
            'Зашифрованный текст в байтах'
]

combobox = ttk.Combobox(main_frame, values=combo_opt, width=30, state="readonly")
combobox.grid(column=0, row=8, sticky='w', columnspan=10, **padding)
combobox.bind("<<ComboboxSelected>>", combo_select)
output_txt.bind('<Control-v>', lambda:'break')

main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid(padx=10, pady=10)

root.mainloop()


