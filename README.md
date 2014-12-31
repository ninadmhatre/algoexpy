pylrn
========

Common algorithms & data structure implementation in Python.

I think, good way to learn language if you start implementing basic sorting algorithms, data structures in 
language you want to learn. I was brushing up my knowledge on these algorithms and felt what if i never have to leave the 
terminal (idle) to learn something and then i wrote this module.

I thank, 
- Author of http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python blog post
- Interactivepython.org for superb course on Algorithms & data structures

So here are some of the basic algorithms, data structures and if i manage to finish both then i might add some common puzzles for e.g. pascals triangle

Purpose
========

Sole purpose of this module is for "educational" purpose and its intended to be used via "idle"

Design & Usage
========

1. I have used addon framework, which allows anyone can write these algorithms even user and load them from idle
2. Every addon must have below methods
   - execute      : Wrapper around "logic" [Please see one of the addons to understand] 
   - info         : Information about the algorithm [As of now, its first para from Wiki and Big-O notations]
   - logic        : Any Guesses? [You can have logic in sub modules]
   - info_online  : Opens the default browser with link to Wiki article [No need to google]
   - show_code    : Print source(logic) on idle console [Supports printing multiple methods]
   - \__addon\__    : Name of addons [if you are using addon_generator.py, this will be there]
3. Intended to be used via "Idle"
4. Use "Debug" mode in idle to understand more about the code [add debugger on "execute"]

Note
=====

Please let me know if there is any issue with poor/wrong implementation of algorithms.
