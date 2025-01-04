# The Elara Handbook

**Welcome to Project Elara!** Project Elara is a mission of a team of committed scientists, engineers, and talented people, working across many different fields, to pass down a better world to our future generations.

## Who we are

We choose to believe in the power of **hope** and we work so that our future descendants can live in a world that we would hope to give them, one where our planet is at peace, and where a quality life is guaranteed to every human being.

These are indeed lofty goals, and we realize that even trying to do so at all is hardly simple. Therefore, we work as a team, across nations and across generations, to accomplish this mission together. To advance, share, and preserve our collective knowledge and expertise, and to build on each other's work, we have put together this book. It is not simply an encylopedia, an open research repository, a wiki, a work of technical documentation, a manifesto of thought, a developer log, a book on software, a textbook, or a manual; it is _all of these_. Everything you'd ever need to learn, develop, or contribute to Project Elara can be found here. And we dedicate this book to not only the ones dear to us, but also to the world.

```{note}
The handbook is actively developed and in some sense it will never be "complete", as it is a continuous work with no singular author and will only grow with time. Information within this handbook can update rapidly. If you find any errors or problems, please report them to us at <https://github.com/elaraproject/elara-handbook/issues>. Thank you very much!
```

## The newcomer's guide

If you're new to the Project, we are very very glad to have you join us! Reading the Elara Handbook is the recommended way to quickly get up to speed with the Project. That said, we understand that reading technical documentation can easily be quite confusing, so we have organized the Handbook to be as easy as possible to get started, and to require **minimal prerequisite knowledge and background** to read.

First, if you are **unfamiliar with calculus, introductory physics, or computer programming (in at least one language)**, we highly recommend you to start from the first chapter, "The Basics". This has two main parts. The first part explains the Project, its mission, and its work. The second covers basic algebra, trigonometry, differential equations, vectors, matrices, and multivariable calculus. If you just need a refresher on one of these topics, it's completely okay to skip a section and move on to the next. After finishing "The Basics", we recommend that you continue on to the second chapter, "The Specifics". This covers the majority of the Project's research and development, as well as the technical prerequisites. While reading everything in this chapter will provide you with a thorough understanding on which to do research, we understand that is not for everyone, so read according to your interests and time.

Second, if you have a **good familiarity with calculus, introductory physics, and computer programming (in at least one language)**, we recommend just reading the first part of "The Basics" (the first chapter). The second part, which covers the math, physics, and programming prerequisites, is not necessary to read, although it may be helpful to skim through. Afterwards, we highly encourage reading through as much of "The Specifics" (the second chapter) as possible. This section covers all the theoretical and applied foundations for understanding the Project's core research, _and_ explains the Project's research. However, it is not necessary to read anything beyond the second chapter.

Third, if you have a **keen interest in theoretical or computational physics, and a strong math and physics background**, we recommend reading the first part of "The Basics" (the first chapter), then jumping straight to "The Expert's Guide" (the third chapter). This chapter is about numerical methods, scientific computing, general relativity, and relativistic quantum mechanics, as well as working on research that pushes the boundaries of modern physics.

Fourth, if you are a **developer and just want to work on code**, we recommend reading the first part of "The Basics", and then jumping straight to the "Developer" section of "The Expert's Guide" (the fourth chapter). You may then choose to read whichever parts suit your interest and the work you plan to do.

We are so grateful for each and every one of our members, and everyone's contributions, **no matter how small**, will be added to the "Contributions" portion at the end of the book. Your work brings us one step closer to changing the world for the better.

## The developer's guide

[Skip past developer section](#license)

Wanting to edit and add to the Handbook? This book is written using [Jupyterbook](https://jupyterbook.org/), a Python-based tool for making scientific books containing runnable code. The source code is hosted on the Project Elara GitHub at <https://github.com/elaraproject/elara-handbook>. To edit the Handbook, ensure you have Git installed, and then clone the repository:

```sh
git clone https://github.com/elaraproject/elara-handbook
cd elara-handbook
```

To build the book locally, ensure you have Jupyterbook installed, then, with a terminal open to the **root directory of the repository**, run:

```sh
# You MUST run this in the ROOT of the Git repo
jupyter-book build book/
```

Then you can start writing! We recommend using a markdown editor like [Obsidian](https://obsidian.md/) which makes editing _much_ more convenient, but this is not strictly necessary. Simply follow the below instructions:

- To write a new section, first switch to a new editing branch with `git checkout -b YOUR_NEW_BRANCHNAME` (replace `YOUR_NEW_BRANCHNAME` with an appropriate name for the branch as you see fit)
- Copy a template from the `templates/` folder in the repository root and copy it into one of the directories (e.g. `basics/`, `specifics/`, etc.)
- Then rename it to a suitable name and add the filename to `_toc.yml` located in the repository root in the appropriate section
- You can now start editing! Remember to commit and open a pull request on github (github provides automated tools for this on its website) so we can add in your changes!

All material in the Elara Handbook is dedicated to the public domain. You may freely use, redistribute (free or for a fee), copy, modify, and (most importantly of all) learn from this book. Just be aware that this book cannot be copyrighted, patented, or claimed as your own work (as it is inherently in the public domain). You may also make proprietary modifications to this book and/or its included source code and sell it, use this book commercially, or include this book as part of a product. We, however, do not encourage the practice, as it is fundamentally against our values, and we would hope that if you derive profit from this book, you contribute some part of your profits to helping Project Elara and its mission.

## License

[Skip past licensing section](#other-formats)

The Elara Handbook is dual-licensed under the **Unlicense** (Public Domain License) and **Creative Commons CC0 License** as it contains both traditional book content and included executable code. In situations where an ambiguity arises as to which license should be applied, whichever of the two below licenses is **more permissive** will be regarded as the sole license to be applied across the whole work.

### The Unlicense

```text
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org/>
```

### Creative Commons CC0 1.0 Universal

```text
Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes the Waiver for the benefit of each
member of the public at large and to the detriment of Affirmer's heirs and
successors, fully intending that such Waiver shall not be subject to
revocation, rescission, cancellation, termination, or any other legal or
equitable action to disrupt the quiet enjoyment of the Work by the public
as contemplated by Affirmer's express Statement of Purpose.

3. Public License Fallback. Should any part of the Waiver for any reason
be judged legally invalid or ineffective under applicable law, then the
Waiver shall be preserved to the maximum extent permitted taking into
account Affirmer's express Statement of Purpose. In addition, to the
extent the Waiver is so judged Affirmer hereby grants to each affected
person a royalty-free, non transferable, non sublicensable, non exclusive,
irrevocable and unconditional license to exercise Affirmer's Copyright and
Related Rights in the Work (i) in all territories worldwide, (ii) for the
maximum duration provided by applicable law or treaty (including future
time extensions), (iii) in any current or future medium and for any number
of copies, and (iv) for any purpose whatsoever, including without
limitation commercial, advertising or promotional purposes (the
"License"). The License shall be deemed effective as of the date CC0 was
applied by Affirmer to the Work. Should any part of the License for any
reason be judged legally invalid or ineffective under applicable law, such
partial invalidity or ineffectiveness shall not invalidate the remainder
of the License, and in such case Affirmer hereby affirms that he or she
will not (i) exercise any of his or her remaining Copyright and Related
Rights in the Work or (ii) assert any associated claims and causes of
action with respect to the Work, in either case contrary to Affirmer's
express Statement of Purpose.

4. Limitations and Disclaimers.

 a. No trademark or patent rights held by Affirmer are waived, abandoned,
    surrendered, licensed or otherwise affected by this document.
 b. Affirmer offers the Work as-is and makes no representations or
    warranties of any kind concerning the Work, express, implied,
    statutory or otherwise, including without limitation warranties of
    title, merchantability, fitness for a particular purpose, non
    infringement, or the absence of latent or other defects, accuracy, or
    the present or absence of errors, whether or not discoverable, all to
    the greatest extent permissible under applicable law.
 c. Affirmer disclaims responsibility for clearing rights of other persons
    that may apply to the Work or any use thereof, including without
    limitation any person's Copyright and Related Rights in the Work.
    Further, Affirmer disclaims responsibility for obtaining any necessary
    consents, permissions or other rights required for any use of the
    Work.
 d. Affirmer understands and acknowledges that Creative Commons is not a
    party to this document and has no duty or obligation with respect to
    this CC0 or use of the Work.
```

## Other formats

For offline usage, the PDF version of this book can be downloaded from <https://github.com/elaraproject/elara-handbook/releases/latest>.