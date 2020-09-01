#!/usr/bin/env python3

#Paul Croft
#August 28, 2020

from bottle import get, run, static_file, template
import json
import os
from pprint import pformat, pprint
import time
import random

base_list = []
queue = []

@get("/static/<sfile>")
def get_stat(sfile):
    return static_file(sfile, root="static")

@get("/wfs/<mfile>")
def static_audio(mfile):
    if mfile.rsplit('.')[1] == "mp3":
        return static_file(mfile, root="mp3subset")
    return ''


def enqueue():
    while len(queue) < (int(1.5 *  len(base_list))):
        temp = base_list[:]
        random.shuffle(temp)
        queue.extend(temp)

@get("/api/delay")
def small_delay():
    time.sleep(1)
    return "Done"

@get("/api/next")
def get_next_json():
    wrong_answers = False
    while not wrong_answers:
        next_set = queue.pop(0)
        chosen_audio = random.choice(next_set).strip()
        wmcf_url = "/wfs/En-us-{}.mp3".format(chosen_audio)
        try:
            afilepath = "mp3subset/En-us-{}.mp3".format(chosen_audio)
            # print(afilepath)
            os.stat(afilepath)
            wrong_answers = list(map(lambda x:x.upper().strip(), next_set))
        except FileNotFoundError:
            # print("Not found")
            wrong_answers = False
        enqueue()

    # print(next_set, chosen_audio, wmcf_url)
    return template("templates/game_section.html", wmcf_url=wmcf_url, wrong_answers=wrong_answers)


@get("/")
@get("/index")
def mainpage():
    global base_list
    global queue
    base_list = open("cleaned_pairs.txt").readlines()
    base_list = [i.split('|') for i in filter(None, base_list)]
    blen = len(base_list)
    queue = []
    enqueue()

    return template("templates/index.html")

def main():
    run(host="0.0.0.0", port="14243", server="eventlet")

if __name__ == '__main__':
    exit(main())
