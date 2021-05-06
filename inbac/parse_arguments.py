import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""inbac - interactive batch cropper\n
Left Mouse Button                 - select part of image\n
Z                                 - save selection and go to the next picture\n
X                                 - save selection and stay on the same picture\n
C                                 - rotate current image by 90 degrees\n
Hold Left Shift or Left Ctrl      - drag selection\n
Right Arrow or Right Mouse Button - go to next picture\n
Left Arrow or Middle Mouse Button - go to previous picture\n"""
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        help="input directory (defaults to current working directory)",
        default=None)
    parser.add_argument(
        "output_dir",
        nargs="?",
        help="output directory (defaults to folder crops in input directory)",
        default=argparse.SUPPRESS)
    parser.add_argument("-a", "--aspect_ratio", type=int, nargs=2,
                        help="selection should have specified aspect ratio")
    parser.add_argument(
        "-r",
        "--resize",
        type=int,
        nargs=2,
        help="cropped image will be resized to specified width and height")
    parser.add_argument(
        "-s",
        "--selection_box_color",
        help="color of the selection box (default is black)",
        default="black")
    parser.add_argument(
        "-w",
        "--window_size",
        type=int,
        nargs=2,
        help="initial window size (default is 800x600)",
        default=[
            800,
            600])
    parser.add_argument("-f", "--image_format",
                        help="define the croped image format")
    parser.add_argument("-q", "--image_quality", type=int,
                        help="define the croped image quality", default=100)
    parser.add_argument("-cf", "--crop_file", type=str, default="crop_info.txt")
    args = parser.parse_args()

    return args
