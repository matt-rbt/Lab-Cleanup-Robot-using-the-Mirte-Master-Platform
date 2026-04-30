# Example article using latex template

### Different formats 

JupyterBook supports producing your report in multiple formats, including:
- **web-based format:** Ideal for online reading, interactive content and sharing with supervisors and collaborators. An example can be seen [here](https://luukfroling.github.io/BEP/)
- **PDF format:** Suitable for official submission and printing. This repository focuses on providing a template specifically designed for the PDF format. 

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
