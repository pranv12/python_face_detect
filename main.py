import cv2
from train import train_data
import argparse


parser = argparse.ArgumentParser(description='Face recognition System')
parser.add_argument('-r','--record' , default=0, help='Record your face in dataset. \n E.g. -r 1',type=bool)
#parser.add_argument('-R','--reset' , default=0, help='Reset complete program.',action= capture())
args = parser.parse_args()


def capture():
    t = train_data()
    t.record()

def main():
    if args.record:
        capture()

if __name__ == "__main__":
    main()