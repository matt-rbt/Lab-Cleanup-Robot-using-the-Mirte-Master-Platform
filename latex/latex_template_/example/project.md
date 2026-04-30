---
title: Title of thesis
short_title: Written by [...]
description: description of thesis
authors: [name student, name supervisor]
abstract: |
    ```{include} parts/01-abstract.md
    ```
export:
  - format: pdf
    output: exports/thesis.pdf
    template: ../
    id: tud-thesis-export
    cover: cover.png
    logo: cover.png
    show_pagenumbers: arabic
---

```{include} parts/02-introduction.md
```
```{include} parts/03-theory.md
```
