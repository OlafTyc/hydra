from rmarkdownreport import report

report("""
---
title: "Test Report"
author: "Mattias"
date: "March 22, 2017"
output:
  html_document:
    highlight: tango
    number_sections: no
    theme: default
    toc: yes
    toc_depth: 3
    toc_float:
      collapsed: no
      smooth_scroll: yes
---


## R Markdown

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

## Summary
Reads have been merged with snakemake@input[[1]]

## Plot
```{r cars}
library(plotly)
readstat = read.csv('readstat.csv')
plot_ly(readstat, y=~avg_len, type='scatter', text=~filename)
```
""", snakemake.params.prefix, **snakemake.input)


