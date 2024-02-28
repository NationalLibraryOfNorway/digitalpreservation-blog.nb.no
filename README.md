
<div align="center">
  <h1>
    <a href="https://digitalpreservation-blog.nb.no/">digitalpreservation-blog.nb.no</a>
  </h1>
  <h3><b>Blog for the Digital Preservation Team at the National Library of Norway</b></h3>
  <h4>
      <a href="#links">Links</a>
      •
      <a href="#development-guide">Development Guide</a>
      •
      <a href="#deployment">Deployment</a>
      •
      <a href="#contributing">Contributing</a>
      •
      <a href="#contact">Contact</a>
      •
      <a href="#copyright">Copyright</a>
  </h4>
  <h3>
    <a href="https://digitalpreservation-blog.nb.no/">
      <img src="assets/images/cover.webp" alt="Cover image for the Digital Presentation blog website">
    </a>
  </h3>
</div>

## Introduction

This repository contains the source code for the website and blog of the Digital Preservation team at the [National Library of Norway (NLN, Nasjonalbiblioteket)](https://www.nb.no/ "National Library of Norway homepage").
The website is built using the static site generator [Hugo](https://gohugo.io/ "Hugo's homepage") and the theme [Hugo PaperMod](https://adityatelange.github.io/hugo-PaperMod/ "Hugo PaperMod's homepage").

In addition to housing blogposts written by the team, the website also contains information about the team, its members, and the projects it is involved in.
It also contains some policy documents with our principles, ambitions, goals, strategies and much more.
The website is hosted on GitHub Pages and is available at [https://digitalpreservation-blog.nb.no/](https://digitalpreservation-blog.nb.no/ "Digital Preservation team's website").

This website is designed to run in any major browser and is responsive to different screen sizes and devices.
We also try our best to make this site accessible to everyone, including people who use screen readers and other assistive technologies.
However if you notice any issues please let us know by creating an issue in this repository.

## Table of Contents <!-- omit from toc -->
1. [Introduction](#introduction)
1. [Links](#links)
1. [Development Guide](#development-guide)
   1. [Prerequisites](#prerequisites)
      1. [GIT and Editor](#git-and-editor)
      1. [Hugo](#hugo)
      1. [Hugo PaperMod](#hugo-papermod)
   1. [Adding a New Blog Post](#adding-a-new-blog-post)
   1. [Adding a New Document](#adding-a-new-document)
   1. [Running the Website Locally](#running-the-website-locally)
1. [Deployment](#deployment)
1. [Contributing](#contributing)
1. [Contact](#contact)
1. [Copyright](#copyright)

## Links

As mentioned above, the website is available at [https://digitalpreservation-blog.nb.no/](https://digitalpreservation-blog.nb.no/ "Digital Preservation team's website").
The source code for the website is available at [https://github.com/NationalLibraryOfNorway/digitalpreservation-blog.nb.no](https://github.com/NationalLibraryOfNorway/digitalpreservation-blog.nb.no "Digital Preservation team's website source code").
We also have a main homepage for the National Library of Norway at [https://www.nb.no/](https://www.nb.no/ "National Library of Norway homepage").
There you can find a short introduction to the digital preservation at NLN, both in [english](https://www.nb.no/en/digital-preservation/ "English article about digital preservation at NLN"), and [norwegian](https://www.nb.no/digital-bevaring/ "Norwegian article about digital preservation at NLN").

## Development Guide

While you can edit the website directly on GitHub, it is recommended to clone the repository and run the website locally to see the changes before pushing them to the repository.
This is especially important if you are pushing directly to the `main` branch, as the website is automatically built and deployed from the `main` branch.

### Prerequisites

#### GIT and Editor

If you are planning on cloning this project, you need to have [GIT](https://git-scm.com/ "GIT's homepage") installed.
In addition to GIT, you need to have a text editor installed.
Any text editor will work, although it is recommended to use one that supports markdown syntax highlighting.
If you don't have a preferred text editor, you can use [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code's homepage").
It has a [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one "Markdown All in One's homepage") extension that provides a lot of useful features for writing markdown.
Make sure to set emphasis marker to `*` and bold marker to `**` in the settings of the extension, as those are the markers we use in our markdown files.

#### Hugo

In order to run the website locally, you need to have [Hugo](https://gohugo.io/ "Hugo's homepage") installed.
You can find installation instructions for Hugo on their [installation page](https://gohugo.io/installation/ "Page with guides on installing Hugo on MAC, Windows, Linux, and BSD").

After installing it make sure to run `hugo version` to verify that it is installed correctly.
You can learn more about Hugo and how to use it in their [documentation](https://gohugo.io/documentation/ "Hugo's documentation").
Although our sample post found in [samplepost](./content/blog/samplepost.md "Document describing markdown syntax, hugo functions, and style guide for the articles") should cover most of the markdown syntax and frontmatter you will need to know.

#### Hugo PaperMod

The website uses the theme [Hugo PaperMod](https://adityatelange.github.io/hugo-PaperMod/ "Hugo PaperMod's homepage").
It is included as a submodule in the repository, so you don't need to install it separately.
When fetching the project make sure to use the extra parameter with clone `--recurse-submodules` to get the theme.
However, if you had cloned the repository without the `--recurse-submodules`, you need to run `git submodule update --init --recursive` to get the theme.
If you forget to do this, you will get warnings when running local server with `hugo server -D`:

```
WARN  found no layout file for "html" for kind "...": You should create a template file which matches Hugo Layouts Lookup Rules for this combination.
```

### Adding a New Blog Post

In order to add a new blog post, you need to create a new markdown file in the `content/blog` directory.
If you are adding a new post with assets, you should create a new directory for the post and place the markdown file and the assets in that directory.
We recommend creating a folder anyway, as it makes it easier to organize the assets and the markdown file.

The folder should be named with blogpost date and title, for example `2022-01-23-my-new-blog-post`.
The markdown file should be named `index.md` and the assets should be placed in the same directory.
See [Content Organization](https://gohugo.io/content-management/organization/ "Documentation on how to organize content in Hugo") for a more in-depth guide on how to organize content in Hugo.

```
content
└── blog
    ├── Post1            <-- Page bundle for post 1
    │   ├── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── Post2            <-- Page bundle for post 2
    │   └── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    └── _index.md        <-- index/layout definitions for blog overview page (do not edit)
```

If you are unsure how to write markdown or what frontmatter to use, you can check the [samplepost](./content/blog/samplepost.md "Document describing markdown syntax, hugo functions, and style guide for the articles") for all available markdown syntax and explanations for frontmatter.
In addition it contains a style guide for the articles, as well as description of shortcodes.

An example of the frontmatter for a blog post is:

```yaml
---
# Post's front matter is written in YAML and places between two sets of '---' (three dashes)
title: Sample post # Sets the article's title. The title that will be shown on the front page and at the top of the post.
summary: Optional summary of the post # Optional. Short summary to display on the front page. If left empty, the first lines of text from the post will be shown instead.
date: 2001-09-11 # Publication date. As long as this is not set in the future the post will be visible on the front page.
draft: true # Marks the post as a draft, if true it will not be published even when pushed to main. Use it during writing and local testing to see how it looks.
weight:  # To set page order or to pin a post to Top of list, lower the weight, higher the post will appear in the list
category: # Category of the post, for now we just use Blog for all posts
tags: [Tag1, Tag2] # Tags for categorizing the article, will be shown in the Tag overview.
author: [Author 1, Author 2] # Author(s) of post. Accepts multiple values if more than one person contributed to the post.
cover: # Settings for displaying a cover image for the post on the front page. 
  image: /cover.webp # Path to the image. '/cover.webp' is the same as 'assets/images/cover.webp' in the project root, while 'cover.webp' uses file in the blogpost folder.
  hiddenInList: false # Whether to show cover image or not
showtoc: true # Toggle to show table of content at the top of the post
aliases: /samplepost_alias # Alias urls for the post, useful for redirecting old urls to new ones, or for important posts to have distinct urls
---
```

### Adding a New Document

The process for adding documents is similar to adding blog posts.
You need to create a new folder with the document title in the `content/documents` directory.
There you should add three files: `_index.md`, as well as two markdown files for the document, one in english and one in norwegian.

The `_index.md` file should contain the frontmatter for the document, as well as the layout definition.
For example:

```yaml
---
title: Document title in English
summary: Document summary in English
draft: false
layout: "list"
date: 2024-02-03
lastmod: 2024-02-07
ShowReadingTime: false
ShowWordCount: false
hideSummary: false
---
```

While the document files should contain the frontmatter for the document, as well as the content of the document.
They should link to each other, so that the user can easily switch between the two languages.
For example:

```yaml
---
title: Document title in Norwegian [NO]
summary: 🇳🇴 Norwegian primary document
weight: 1
date: 2024-02-03
draft: false
tags: [Tag1, Tag2]
author: [Digital Preservation Team]
showtoc: true
ShowReadingTime: false
hideMeta: false
hideSummary: false
---

English translation can be found [here](/docs/... "Link to the English version of this document").

---

Document content in English...
```

```yaml
---
title: Document title in English [EN]
summary: 🇬🇧 English translation
weight: 2
date: 2024-02-03
draft: false
tags: [Tag1, Tag2]
author: [Digital Preservation Team]
showtoc: true
ShowReadingTime: false
hideMeta: false
hideSummary: false
---

The primary document version in Norwegian can be found [here](/docs/... "Link to the Norwegian version of this document").

---

Document content in English...
```

### Running the Website Locally

If you wish to preview the website locally, you need to run `hugo server -D` in the root of the project.
The `-D` flag is used to include draft posts in the build, so that you can preview them locally.
Make sure that the articles you write are marked as drafts until they are ready to be published.
If you forget to do it and push it to main it will be published on the front page.

Look at the output of the command, it will tell you the address of the local server.
It is usually `http://localhost:1313/`, but it can be different if you have other services running on your computer.
It will also tell you if there are any errors or warnings in the posts, so you can fix them before pushing the changes to the repository.

To stop the local server, press `Ctrl + C` in the terminal where the server is running.

## Deployment

The website is automatically built and deployed from the `main` branch of the repository.
This means that any changes pushed to the `main` branch will be visible on the website after a short delay.
The deployment is handled by GitHub Actions, and the configuration for the deployment can be found in the `.github/workflows/hugo.yml` file.

## Contributing

If you wish to contribute to the website, you can do so by creating a pull request in this repository.
Do this if you wish to fix any issues you find and want to contribute directly instead of creating an issue.
This can be done by forking the repository, making the changes in your fork, and then creating a pull request from your fork to the `main` branch of the original repository.

## Contact

If you wish to contact the Digital Preservation team at the National Library of Norway, you can go to National Library of Norway's [home page](https://www.nb.no "National Library of Norway homepage") and find the contact information there.

If you wish to contact the developers of the website, you can do so by creating an issue in this repository.
You can use that to give feedback on the website, report issues, or ask questions about the website.

## Copyright

Copyright © National Library of Norway 2023-2024