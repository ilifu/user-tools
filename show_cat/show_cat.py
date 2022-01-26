#!/usr/bin/env python3
from argparse import ArgumentParser
from logging import getLogger

from coloredlogs import install as coloredlogs_install
from PIL import ImageTk, Image
from tkinter import Label, Tk

logger = getLogger()


def create_argument_parser() -> ArgumentParser:
    new_parser = ArgumentParser(description='View image file')
    new_parser.add_argument(
        'image_file', type=str, nargs=1, help='name of file to display',
    )

    new_parser.add_argument('--debug', action='store_true', default=False, help='More verbose output')
    return new_parser


def display_image(path: str):
    image_window = Tk()
    screen_width, screen_height = image_window.winfo_screenwidth()*0.90, image_window.winfo_screenheight()*0.90

    image = Image.open(path)
    image_width, image_height = image.size

    if image_width > screen_width or image_height > screen_height:
        logger.debug(f'Image is larger than 90% of screen ({image_width}×{image_height} vs {screen_width}×{screen_height})')
        height_ratio, width_ratio = image_height / screen_height, image_width / screen_width
        if height_ratio > width_ratio:
            resize_ratio = height_ratio
        else:
            resize_ratio = width_ratio
        new_size = (int(image_width/resize_ratio), int(image_height/resize_ratio))
        logger.debug(f'Resizing image to: {new_size[0]}×{new_size[1]}')
        image = image.resize(new_size, Image.ANTIALIAS)

    final_image = ImageTk.PhotoImage(image)
    panel = Label(image_window, image=final_image)
    panel.pack(side="bottom", fill="both", expand=True)

    image_window.mainloop()


def main():
    parser = create_argument_parser()
    args = parser.parse_args()

    if args.debug:
        coloredlogs_install(level='DEBUG')
    else:
        coloredlogs_install(level='INFO')

    if len(args.image_file) == 1:
        logger.debug(f'Opening {args.image_file[0]}')
        display_image(args.image_file[0])
    else:
        logger.debug(f'No image specified')
