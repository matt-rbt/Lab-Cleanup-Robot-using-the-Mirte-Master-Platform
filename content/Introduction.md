---
abstract: |
---

# Introduction


**cite from bib-file**
- `{cite:t}`jupyter2025`` resulting in {cite:t}`jupyter2025`
- `{cite:p}`jupyter2025`` resulting in {cite:p}`jupyter2025`


## Related Works
Jupyter Book has been rebuild with the intend to export content in multiple output formats including HTML, PDF and docx. {numref}`Figure {number} <fig-diagram>` provides this idea.

```{figure} figures/diagram.*
:label: fig-diagram
:alt: Some figure

The myst engine allows Jupyter Notebook, markdown and even tex files to be converted to multiple output formats.
```

As exporting to different formats is possible, it is not always desired. Some content should only be visible in the HTML version, and some content only need to be included in the PDF version. You can use blocks like `+++{"no-pdf":true}` to enable this, as shown below where the figure is seen in the HTML version but not in the PDF version.

+++{"no-pdf":true}
```{figure} figures/delft.*
:label: fig-delft
:alt: picture of the TUD

A figure that is in the website but not in the PDF version.
```

## Contribution
+++