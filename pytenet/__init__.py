#!/usr/bin/env python
import sys

import pyautogui


def main():
    width, height = pyautogui.size()
    pyautogui.moveTo(width / 2, height / 2, 0.5, pyautogui.easeInQuad)


if __name__ == '__main__':
    sys.exit(main())
