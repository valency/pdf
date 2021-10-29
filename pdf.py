import argparse
import logging
import os

from fpdf import FPDF
from wrenchbox.logging import setup_log


class Synthesis:
    def __init__(self):
        pass

    def generate(self, path):
        for d in os.listdir(path):
            if not os.path.isfile(os.path.join(path, d)):
                logging.info(d)
                pdf = FPDF()
                for f in sorted(os.listdir(os.path.join(path, d))):
                    u = os.path.join(path, d, f)
                    if os.path.isfile(u):
                        if f.endswith(('jpg', 'jpeg', 'png')):
                            logging.info(f)
                            pdf.add_page()
                            pdf.image(u)
                pdf.output(os.path.join(path, '{}.pdf'.format(d)), 'F')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true', default=False, help='show debug information')
    parser.add_argument('dir', type=str, help='parent directory')
    args, _ = parser.parse_known_args()
    setup_log(level=logging.DEBUG if args.debug else logging.INFO)
    Synthesis().generate(args.dir)
