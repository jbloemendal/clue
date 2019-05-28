---
layout: post
title:  "Prototype release alpha version 0.4a"
date:   2019-05-28 11:33:15 +0200
categories: static-analysis inspection codestyle
---
![Magnifier](https://raw.githubusercontent.com/jbloemendal/clue/gh-pages/tango_system_search.gif)

[Clue complexity article (pdf)](https://github.com/jbloemendal/clue/raw/0.4a/clue-article.pdf)

{% highlight bash%}
NAME
      clue -- code inspection instrument

SYNOPSIS
      clue [-c] [-f FILE] [-g] [-h] [-k] [-p] [-q] [-v]

DESCRIPTION
      Static code inspection instrument, analyses complexity for c-family syntax (C, C++, Java, ECMAScript, C#, ...)
      it parses decisions of a standard data input stream (stdin) and calculates absolute numbers.

      -c            cyclomatic complexity, condition count, O(n)
      -f, --file    read one or more newline separated lines from file
      -g            control flow path conjecture, O(2n)
      -h, --help    show this help message
      -k            clue complexity, regards nested c-family syntax, O(n^2)
      -p            clue path
      -q            all sub paths, O(2^n)
      -v            verify clue path
{% endhighlight %}
