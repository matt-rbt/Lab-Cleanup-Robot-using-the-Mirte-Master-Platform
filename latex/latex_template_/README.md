# Jupyter Book Latex template for thesis

<div align="center">
  <img src="images/front-page.png" width="50%">
</div>

This repository provides a LaTeX template for creating JB2 (Jupyter Book 2) books using MyST Markdown, specifically configured for bachelor’s and master’s thesis layouts.

## Using the template

Add the following code to the `myst.yml` file: 

```{code} yml

downloads:
    - id: output-pdf

exports:
    - format: pdf 
        output: exports/output_file.pdf
        template: { - TODO: replace with published link - }
        id: output-pdf
```

This will automatically apply the template when running `jupyter book build --pdf` in the command line. 

## Additional settings 

There are multiple additional settings which can be used to further customise the output PDF (e.g. cover, logo, margins). These can be seen in the `export.yml` file of the example found [here](example/export.yml) 

## Output

The first two pages show to general layout of the template:

<table>
<tr>
<td style="border: 1px solid black; padding: 4px;">
  <img src="images/front-page.png" alt="front page image" width="400">
</td>
<td style="border: 1px solid black; padding: 4px;">
  <img src="images/table-of-contents.png" alt="ToC image" width="400">
</td>
</tr>
</table>

The table of contents can be turned off via the settings in `export.yml`.