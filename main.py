import os

import pywebio
from pywebio import start_server
from pywebio.output import put_text, put_image, put_table, use_scope, put_button, toast
from getText import get_text
from getText import translate

new_text=""
text = ""
async def main():
    global new_text
    global text
    toast("Max chars to translate = 500.")
    while True:
        file = await pywebio.input.file_upload("Upload a file")
        open('D:\\Programming\\Python\\textFromPhoto\\imgs\\' + file['filename'], 'wb').write(file['content'])
        path = 'D:\\Programming\\Python\\textFromPhoto\\imgs\\' + file['filename']

        with use_scope("btns", clear=True):
            def text_btn():
                global text
                global new_text
                new_text = translate(text)
                put_text(new_text, scope="btns")

            put_button("Translate ", onclick= text_btn)
            text = get_text(path)

        with use_scope('results', clear=True):
            put_table([
                [put_text(text, position=1)],
                [put_image(file['content'], position=1)]
            ])
        os.remove(path)


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
