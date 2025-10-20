# surprisalingFactor
Repository for the BrainHack Donostia 2025 project "Helmholtz never published in Nature Neuroscience"

## Project Overview
Surprisal theory in psycholinguistics proposes that the harder a word is to predict from context, the more cognitive effort it takes to process. This project applies surprisal measures to characterize major journals in cognitive neuroscience and experimental psychology, testing whether surprisal distributions align with journal-level metrics (impact factor) or article-level metrics (citations).

We will automate pipelines to extract articles, compute surprisal using open-source LLMs, run exploratory analyses, and write a report exploring whether highly cited papers in neuroscience embrace more or less linguistic surprise.

## Goals
1. Set up an automated pipeline to scrape full-text neuroscience articles from 20-100 major journals in the field
2. Compute surprisal scores using an open-source LLM to calculate average word-level surprisal for a minimum of 50 articles per journal
3. Define exploratory analyses and collect appropriate journal/article metrics (e.g., impact factor, year, citations, sub-field)
4. Produce visualizations comparing surprisal distributions with the collected metrics
5. Generate collaborative interpretation of the results
6. Draft a short report summarizing context, methods, results, and limitations

## Sub-teams
Participants can join one or more of the following sub-teams based on their interests and skills:

- **Automated data pipeline** (advanced programming skills) — scraping and cleaning articles
- **Automated surprisal computation** (intermediate programming skills) — setting up LLM-based analysis
- **Running surprisal computation** (beginner programming skills) — distributed computation across machines
- **Defining exploratory analyses** (beginner to intermediate programming skills) — selecting metrics and hypotheses
- **Visualization** (intermediate programming skills) — creating comparative plots
- **Interpretation & discussion** (no programming skills required) — collaborative analysis
- **Reporting** (no programming skills required) — parallel documentation of methods and results

## Timeline

### Day 1 (Setup & First Samples)
- Data pipeline: scrape and clean a first batch from at least one neuroscience journal
- Surprisal pipeline: choose open-source LLM, compute surprisal scores for one sample article, install pipeline on multiple computers
- Analyses: brainstorm candidate metrics and assign responsibilities
- Reporting: set up shared doc for methods + notes, write the abstract

### Day 2 (Scaling & First Results)
- Data pipeline: expand scraping and consolidate the final dataset
- Surprisal: set up computation for all articles to run overnight
- Analyses: collect external journal/article metadata (impact factors, citations, years)
- Visualization: generate first comparative plots and automate plotting
- Reporting: write context (intro) and methods sections

### Day 3 (Integration & Wrap-up)
- Analyses: run all exploratory analyses
- Visualization: polish plots for final presentation
- Interpretation: produce group consensus on key takeaways
- Reporting: write results and conclusions, finish first draft

## Expected Skills to Learn or Develop

### For Everyone
- Basics of surprisal theory and its link to science communication
- How to read and interpret simple data visualizations
- How to co-write and present fun, accessible results

### For Beginner Coders
- Running an LLM to compute surprisal on text
- Cleaning text and calculating simple stats
- Making basic plots with Python

### For Intermediate/Advanced Coders
- Automating large-scale article scraping and processing
- Automating multi-platform large-scale LLM computations

## Technical Requirements
All you need to bring is your own laptop! We will set up all necessary software, tools, and computational environments together during the Brainhack. No prior installation or configuration is required.
