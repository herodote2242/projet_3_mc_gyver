#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""This is the "entrance" module,
the one that launches the game and the other modules."""

import application

if __name__ == "__main__":
    application = application.Application()
    application.startgame()
