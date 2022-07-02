import os

import pywebio
from pywebio import start_server
from pywebio.output import put_text, put_image, put_table, use_scope
from getText import get_text
from getText import translate


async def main():

    while True:
        file = await pywebio.input.file_upload("Upload a file")
        open('D:\\Programming\\Python\\textFromPhoto\\imgs\\' + file['filename'], 'wb').write(file['content'])
        path = 'D:\\Programming\\Python\\textFromPhoto\\imgs\\' + file['filename']

        text = get_text(path)
        os.remove(path)
        new_text = translate(text)

        with use_scope('results', clear=True):
            put_table([
                [put_text(text, position=1)],
                [put_text(new_text, position=1)],
                [put_image(file['content'], position=1)]
            ])


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
