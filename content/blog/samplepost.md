---
# Post's front matter is written in YAML and places between two sets of '---' (three dashes)
title: Sample post # Sets the article's title. The title that will be shown on the front page and at the top of the post.
summary: Optional summary of the post # Optional. Short summary to display on the front page. If left empty, the first lines of text from the post will be shown instead.
date: 2001-09-11 # Publication date. As long as this is not set in the future the post will be visible on the front page.
expiryDate: 2001-09-11
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

Post content, written in Markdown, goes here. 
You can use the [markdown syntax guide](#markdown-syntax-guide "Link to the section for markdown syntax guide") below as a reference.
There are more in depth examples of the Hugo shortcodes in the [hugo shortcodes](#hugo-shortcodes "Link to the section for Hugo shortcodes") section.
As well as a [code syntax guide](#code-syntax-guide "Link to the section for code block syntax guide") for code blocks and inline code.
There are also some general guidelines for writing posts in the [general post writing guidelines](#general-post-writing-guidelines "Link to the section with general post writing guidelines") section.

Keep in mind that there are other guides for markdown available online, such as [GitHub's guide](https://guides.github.com/features/mastering-markdown/ "Link to GitHub's guide to mastering markdown") and [John Gruber's guide](https://daringfireball.net/projects/markdown "Link to John Gruber's article on markdown").

---

# General post writing guidelines

When writing a post, keep in mind that it should be easy to read and understand.

In general try to use:
- Headings to separate sections and make the post easier to navigate
- Lists to make information easier to digest
- Blockquotes to highlight important information
- Images to make the post more visually appealing
- Links to provide sources and additional information
- Code blocks to show code examples
- Footnotes to provide additional information without cluttering the post
- Tables to present data in a structured way
- Shortcodes to embed media and other content
- Abbreviations, subscripts, superscripts, keyboard keys, and highlighted text to make the post more readable
- Use oxford commas in the lists, for example: 
  **"My hobbies include reading, writing, hiking, and watching movies"** 
  this avoids confusion and makes the list easier to read.
  In this example it's clear that "*hiking*" and "*watching movies*" are separate hobbies, and not a single hobby of hiking while watching movies.
- Use the active voice, for example: **"The cat sat on the mat"** instead of **"The mat was sat on by the cat"**

When writing the markdown files themselves try to:
- Avoid punctuation in lists, unless the list item is several sentences long
- Put an empty line between sections, codeblocks, and other elements to make the post easier to read
- When quoting, make sure to use the correct syntax for attribution
- When adding images, links, or other media make sure to include captions, alt text, and titles for accessibility and SEO
- When writing a paragraph put each sentence on a new line, this makes it easier to read and edit.
  In addition it helps with version control, as changes to the paragraph will only affect the changed sentence, not the whole paragraph.
  It also helps to avoid merge conflicts when multiple people are working on the same file.
  Lastly it helps to keep the sentences about the same length, and makes it easy to see if a sentence is too long or too short.

---

# Markdown syntax guide

This article offers a sample of basic Markdown syntax that can be used in Hugo content files.
It also shows how basic HTML elements are decorated with CSS in a Hugo theme.

## Headings

The following HTML `<h1>`—`<h6>` elements represent six levels of section headings. 
`<h1>` is the highest section level while `<h6>` is the lowest.
To render a heading in Markdown, add a number of signs (#) in front of the heading text at the beginning of the line.

```markdown
# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6
```

Will render as:

# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

It's also possible to use a different syntax for headings, where the heading text is underlined by a line of `=` or `-` signs.
For example:

```markdown
Heading level 1
===============

Heading level 2
---------------
```

Will render as:

Heading level 1
===============

Heading level 2
---------------

This works only for headings level 1 and 2, and as such is not recommended.

## Horizontal Rule

A horizontal rule is a thematic break in the content, and is used to separate content.
It's not for separating sections of an article, that's what headings are for.
Use it if you want to separate content within a section, for example to separate a quote from the rest of the text.
Or if you want to separate sections of a post that are not related to each other, for example if you have a theoretical and a practical section in a post.
For example this line:

```markdown
Here is a thematic break:

---

Another part of the post
```

Will render as:

Here is a thematic break

---

Another part of the post

You can also use `***` or `___` to create a horizontal rule, but it's recommended to stick to one format.
You can use more than only three characters to create a horizontal rule.

## Paragraph

Here's an example of how a paragraph looks in Markdown.
As you can see when it is rendered the line breaks between sentences are ignored, and the text is displayed as a single block of text.
It's also a good example of how one sentence per line rule helps with spotting long or short sentences.
Paragraph written like this:

```markdown
Xerum, quo qui aut unt expliquam qui dolut labo.
Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur?
Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur?
Quiatem.
Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga.
Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.
```

Will render as:

---

Xerum, quo qui aut unt expliquam qui dolut labo.
Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur?
Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur?
Quiatem.
Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga.
Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

---

```{hl_lines=[2,3]}markdown
In order to put a linebreak in the text, but not the paragraph, you need to put two spaces at the end of the line before the linebreak.
This will split the text into two lines, but it will still be part of the same paragraph.  
As you can see it happen in this paragraph.  
It can be used to split a long paragraph into smaller parts to make the text easier to read.
However try to write shorter paragraphs that don't need splits as they are even easier to read.
```

The previous example will render as:

In order to put a linebreak in the text, but not the paragraph, you need to put two spaces at the end of the line before the linebreak.
This will split the text into two lines, but it will still be part of the same paragraph.  
As you can see it happen in this paragraph on highlighted lines.  
It can be used to split a long paragraph into smaller parts to make the text easier to read.
However try to write shorter paragraphs that don't need splits as they are even easier to read.

## General Text Formatting

There are several ways to format text in Markdown.

```markdown
_italic_ *italic*

__bold__ **bold**

___bold italic___ ***bold italic***

`inline code`

~~strikethrough~~

<ins>Underline</ins>
```

Will render as:

_italic_ *italic*

__bold__ **bold**

___bold italic___ ***bold italic***

`inline code`

~~strikethrough~~

<ins>Underline</ins>

Even though both `_` and `*` are used for italic, it's recommended to use `_` as it's more widely supported.  
Even though both `__` and `**` are used for bold, it's recommended to use `**` as it's more widely supported.

## Lists

### Ordered Lists

Ordered lists are created using numbers followed by periods.
You can either manually number them (although renderer will still number them in order) or use the number 1 for all items.

```markdown
Numbered list:
1. First item
2. Second item
3. Third item

Using 1 for all items:
1. First item
1. Second item
1. Third item
```

Will render as:

Numbered list:
1. First item
2. Second item
3. Third item

Using 1 for all items:
1. First item
1. Second item
1. Third item

### Unordered Lists

Unordered lists are created using asterisks, plus signs, or hyphens.

```markdown
Hyphen list:
- List item
- Another item

Plus list:
+ List item
+ Another item

Asterisk list:
* List item
* Another item
```

Will render as:

Hyphen list:
- List item
- Another item

Plus list:
+ List item
+ Another item

Asterisk list:
* List item
* Another item

### Nested Lists

It's also possible to nest lists within lists.

```markdown
1. Fruit
    - Apple
    - Orange
    - Banana
2. Dairy
    1. Milk
    2. Cheese
3. Third item
    1. Sub One
    2. Sub Two
```

Will render as:

1. Fruit
    - Apple
    - Orange
    - Banana
2. Dairy
    1. Milk
    2. Cheese
3. Third item
    1. Sub One
    2. Sub Two

### Definition Lists

Definition lists are created using a term followed by a colon and the definition.

```markdown
First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.
```

Which will look like this:

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.  
  This is another line of definition for the second term.

### Task Lists

Task lists are created using a hyphen followed by square brackets.
The square brackets can contain an x to mark the task as complete, or a space to mark it as incomplete.

```markdown
- [x] Task 1
- [ ] Task 2
    - [ ] Subtask 2.1
    - [x] Subtask 2.2
```

Results in:

- [x] Task 1
- [ ] Task 2
  - [ ] Subtask 2.1
  - [x] Subtask 2.2

## Links

There are several ways to create links in Markdown.
In general the simplest way is to put the link text in square brackets, and the link itself in parentheses.

```markdown
If you want to link to [example.com](https://example.com) you can do it like this.
```

However it is recommended to add a title to the link, which will be shown when the user hovers over the link.

```markdown
Just click [here](https://example.com "Link to example.com website with a title") you can do it like this.
```

You can also use reference links, which are especially useful for long links, or if you want to use the same link multiple times.

```markdown
This is [an example][1] reference-style link.

[1]: https://example.com "Link to example.com website with a title"
```

This is similar to how footnotes are used, and the reference can be placed anywhere in the file, as long as it's after the reference.

Lastly we can link to sections of the same page, by using the heading text as the link.
Keep in mind that heading text is converted to lowercase while spaces and special characters are replaced with hyphens.

```markdown
To be a bit meta, here's a link to the [links section](#links "Link to the links section of the same page")
```

If you want to link to [example.com](https://example.com) you can do it like this.

Just click [here](https://example.com "Link to example.com website with a title") you can do it like this.

This is [an example][1] reference-style link.

To be a bit meta, here's a link to the [links section](#links "Link to the links section of the same page")

[1]: https://example.com "Link to example.com website with a title"

## Footnotes

Footnotes are a good way to add additional information to a post without cluttering the main text.
They are especially useful for adding sources, definitions, and explanations to a post.
You can put the footnote definition at the end of the file, end of the section, or end of the paragraph, as long as it's after the footnote reference.
The footnote definition will still be rendered at the end of the post, regardless of where it's placed in the file.
Make sure to add an empty after footnote definition to end it.

```markdown
This has a footnote[^1]

[^1]: This is the content of the footnote  
Rest of the footnote on the next line
```

This has a footnote[^1]
[^1]: This is the content of the footnote  
Rest of the footnote on the next line

As you can see you use `[^1]` to reference the footnote, and `[^1]:` to define the footnote.

## Tables

Tables aren't part of the core Markdown specification, but Hugo supports them out-of-the-box.
Example of a simple table syntax:

```markdown
| Name  | Age |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |
```

Renders to:

| Name  | Age |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |


### Table Alignment

You can align text in the columns to the left, right, or center by adding a colon `:` to the left, right, or on both side of the hyphens within the header row.

```markdown
| Left aligned text column | Center aligned text column | Right aligned Text column |
| :----------------------- | :------------------------: | ------------------------: |
| Some text                | Some more text             | Even more text            |
| Some text                | Some more text             | Even more text            |
```

Results in:

| Left aligned text column | Center aligned text column | Right aligned Text column |
| :----------------------- | :------------------------: | ------------------------: |
| Some text                | Some more text             | Even more text            |
| Some text                | Some more text             | Even more text            |

### Inline Markdown in Tables

When writing tables you can use inline markdown, such as links, inline code, and emphasis.

```markdown
| Italics   | Bold     | Code   | Link     |
| --------- | -------- | ------ | -------- |
| *italics* | **bold** | `code` | [link]() |
```

Will give you:

| Italics   | Bold     | Code   | Link     |
| --------- | -------- | ------ | -------- |
| *italics* | **bold** | `code` | [link]() |

## Comments

If you want to add a comment to your mardkown file, you can do so with the following syntax:

```markdown
<!-- This is a comment -->
```

Which as you can't see will be rendrered as such in the output:

<!-- This is a comment --> 

## Blockquotes

The blockquote element represents content that is quoted from another source.
Optionally they can come with a citation which must be within a `footer` or `cite` element
It can also support regular markdown syntax, such as bold text, lists, links, and more.

### Blockquote Without Attribution

If you just wish to quickly quote something, you can use a blockquote without attribution.

```markdown
> Here is a sample quote from a famous person:
> "Ouch!" - Albert Einstein after stubbing his toe, probably.  
> **Note** that you can use *Markdown syntax* within a blockquote.
>
> - You can use lists
> 
> And links to [sources](https://example.com "example link to example.com")
> 
> > You can also nest blockquotes.
> > > Three levels deep...
> > > > Four levels deep......
> > > > > And more!
> But you can't go back down to a previous level
```

Which will render as:

> Here is a sample quote from a famous person:
> "Ouch!" - Albert Einstein after stubbing his toe, probably.  
> **Note** that you can use *Markdown syntax* within a blockquote.
>
> - You can use lists
> 
> And links to [sources](https://example.com "example link to example.com")
> 
> > You can also nest blockquotes.
> > > Three levels deep...
> > > > Four levels deep......
> > > > > And more!
> But you can't go back down to a previous level

### Blockquote With Attribution

If you wish to add a citation to the quote, you can use a blockquote with attribution.

```markdown
> Don't communicate by sharing memory, share memory by communicating.
>
> — <cite>Rob Pike[^2]</cite>

[^2]: The above quote is excerpted from Rob Pike's [talk](https://www.youtube.com/watch?v=PAAkCSZUG1c) during Gopherfest, November 18, 2015.
```

Which will render as:
> Don't communicate by sharing memory, share memory by communicating.
>
> — <cite>Rob Pike[^2]</cite>

[^2]: The above quote is excerpted from Rob Pike's [talk](https://www.youtube.com/watch?v=PAAkCSZUG1c) during Gopherfest, November 18, 2015.

## HTML Elements — abbr, sub, sup, kbd, and mark

If you wish to, you can use some of the HTML elements in your markdown file.
They will allows you to add extra formatting to your document, such as abbreviations, subscripts, superscripts, keyboard keys, and highlighted text.
However use them sparingly and only when necessary, as they can make the document harder to maintain if others are not used to these tags.
You can use the following HTML elements in your markdown file:

```markdown
<abbr title="Graphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.
```

Which will render as:

<abbr title="Jraphics Interchange Format">GIF</abbr> is a bitmap image format.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Press <kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd> to end the session.

Most <mark>salamanders</mark> are nocturnal, and hunt for insects, worms, and other small creatures.

---

# Code Syntax Guide

There are several ways of adding code examples to the markdown file in Hugo.

## Inline Code

This is a standard way of adding inline code to a markdown file.

```markdown
You can use the `cat` command to output contents of a file to the terminal
```

Which will result in :

You can use the `cat` command to output contents of a file to the terminal

## Codeblock With Spaces

In it's simplest form a code block can be created by indenting the code by four spaces.

```markdown
    def hello_world():
        print("Hello, World!")
```

Which will render as

    def hello_world():
        print("Hello, World!")

## Codeblock With Backticks

Another common, and most widely used way of adding code blocks is by using triple backticks.

````markdown
```
def hello_world():
    print("Hello, World!")
```
````

Which will render as:

```
def hello_world():
    print("Hello, World!")
```

## Using `pre` and `code` tags

You can use the `pre` and `code` HTML tags to display a block of code or inline code respectively.
However there are little reasons to do it and the regular inline code and code blocks with backticks are recommended.

```markdown
Use the <code>tag</code> the same way as you would use backticks to create inline code

I really need some contrived <pre>pretext</pre> to use pre in text.
```

Will output:

Use the <code>tag</code> the same way as you would use backticks to create inline code

I really need some contrived <pre>pretext</pre> to use pre in text.

## Stylizing Code Blocks

There are several ways to stylize code blocks in Hugo, such as adding line numbers, highlighting lines, and specifying the language of the code.

### Code Block With Syntax Highlighting

If you wish to use syntax highlighting add a language name after the opening triple backticks.

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

This results in:

```python
def hello_world():
    print("Hello, World!")
```

### Code Block With Highlighted Lines 

You can use the `hl_lines` parameter to highlight specific lines in the code block.
You surround it by curly braces `{hl_lines}`, and give it lines to highlight as an array `{hl_lines=[2,4]}`.
In this case the numbering starts at 1, not 0.

````markdown
```{hl_lines=[2,4]}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```
````

This will output:

```{hl_lines=[2,4]}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```

### Code Block With Line Numbers

You can enable line numbers with the `{linenos=true}` parameter.

````markdown
```{linenos=true}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```
````

Which will render as:

```{linenos=true}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```

### Code Block With Syntax Highlighting, Highlighted Lines, and Line Numbers

You can combine all of these parameters to create a code block with syntax highlighting, highlighted lines, and line numbers.

````markdown
```python {hl_lines=[2,4],linenos=true}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```
````

Resulting in the following:

```python {hl_lines=[2,4],linenos=true}
def hello_world():
    print("Hello, World!")
    print("How are you?")
    print("I'm fine, thank you!")
    print("Oh, you're welcome!")
```

---

# Hugo shortcodes

Huge offers a variety of shortcodes to embed media and other content in your markdown files.
This makes it easier for you and others to add content to the posts, and makes the posts more visually appealing.
It is generally recommended to use shortcodes instead of raw HTML or markdown, as it makes the posts more consistent, and in case of images it allows for easier resizing and optimization.

## Figure Shortcode

Use the `figure` shortcode to embed images in your posts.
It comes with several parameters to adjust how the figure is displayed, such as the image, caption, etc.
It scales the images so that page can be loaded quickly and then better quality images can load on demand.

The list of parameters is as follows:

src
: URL of the image to be displayed. 
  It can be a relative path to the image in the same folder as the markdown file, or an absolute path to the image on the internet.

link
: URL to link to when the image is clicked. 
  If not set, the image will not be clickable.

target
: Optional.
  Sets the `target` attribute for the URL if the `link` parameter is set.
  Specifies where to open the linked document.
  See the [MDN documentation on target](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#target) for more information.
  
rel
: Optional.
  Sets the `rel` attribute for the URL if the `link` parameter is set.
  Defines relationship between the linked resource and the current document.
  See the [MDN documentation on rel](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel) for more information.

title
: Image title

caption
: Caption text for the image, displayed below the image

alt
: Alternative text for the image, used for accessibility and SEO

align
: Optional, sets the alignment of the image. 
  Can be set to `left`, `right`, or `center`.

height
: Optional, defined image height

width
: Optional, defined image width

attr
: Image attribution text

attrlink
: If the `attr` parameter is set, the `attrlink` parameter can be used to link to the source of the image


```go-html-template
{{</* figure 
  src="https://source.unsplash.com/Z0lL0okYjy0" 
  link="https://example.com"
  title="Image title"
  caption="Caption text"
  alt="Alternative text"
  align=center
  height="300"
  width="500"
  attr="Image attribution text"
  attrlink="https://example.com/source"
*/>}}
```

{{< figure 
  src="https://source.unsplash.com/Z0lL0okYjy0" 
  link="https://example.com"
  title="Image title"
  caption="Caption text"
  alt="Alternative text"
  align=center
  height="300"
  width="500"
  attr="Image attribution text"
  attrlink="https://example.com/source"
>}}

## Github Gist

To display a GitHub Gist in your post, use the `gist` shortcode.
In the gist link identify the two important parts: the username and the gist ID.
For example:

```
https://gist.github.com/adityatelange/376cd56ee2c94aaa2e8b93200f2ba8b5
                        ↑ USER ↑      ↑ GIST_ID ↑
```

With those two you can use the shortcode as such:

```go-html-template
{{</* gist USER GIST_ID */>}}
{{</* gist adityatelange 376cd56ee2c94aaa2e8b93200f2ba8b5 */>}}
```

Which will be rendered to:

{{< gist adityatelange 376cd56ee2c94aaa2e8b93200f2ba8b5 >}}

## Instagram Shortcode

If you wish to embed an Instagram post in your post, you can use the `instagram` shortcode.
It requires the post ID, which can be found in the URL of the post.
It's the string of numbers and letters after the `/p/` in the URL.

So if you have a URL like this:

```
https://www.instagram.com/p/CxOWiQNP2MO
                            ↑ POST_ID ↑
```

Use the shortcode like this:

```go-html-template
{{</* instagram CxOWiQNP2MO */>}}
```

Which will render to:

{{< instagram CxOWiQNP2MO >}}

## Twitter Shortcode

Embedding twitter post works similarly to Gist as it requires both the user and the tweet ID.
The tweet ID and user can be found in the URL of the tweet.
The tweet ID is the string of numbers after the `/status/` in the URL, while the user is *usually* after `twitter.com`, although in some cases it can be after the `@` sign.

Given the following URL:

```
https://twitter.com/SanDiegoZoo/status/1453110110599868418
                    ↑ USER ↑           ↑ TWEET_ID ↑
```

Use the shortcode like this:

```go-html-template
{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}
```

And it will be rendered as:

{{< twitter user="SanDiegoZoo" id="1453110110599868418" >}}

## Vimeo Shortcode

Vimeod shortcode requires the video ID, which can be found in the URL of the video.
It's the string of numbers after the last `/` in the URL, which is also after the username.

Given this URL:

```
https://vimeo.com/channels/staffpicks/55073825
                                      ↑ VIDEO_ID ↑
```

Use the shortcode like this:

```go-html-template
{{</* vimeo 55073825 */>}}
```

To embed a Vimeo video in your post, like this:

{{< vimeo 55073825 >}}

You can also use the `title` parameter to add a title to the video.
Note however that you need to use named parameters for both the `id` and `title` as you cannot mix named and unnamed paramters.
If your CSS has a class for embedded videos, you can set it here too:
  
```go-html-template
{{</* vimeo id="55073825" title="Example Video Title" class="example-video-class" */>}}
```

Video titles are useful for SEO and accessibility.

## YouTube

Embedding YouTube videos works similarly to Vimeo, as it requires only the video ID.
The video ID can be found in the URL of the video.
Either following the `v=` parameter in the URL, or after the last `/` in the URL if it's a shortlink.

Given the URLs:
```
https://www.youtube.com/watch?v=w7Ft2ymGmfc
                                ↑ VIDEO_ID ↑

https://youtu.be/w7Ft2ymGmfc
                 ↑ VIDEO_ID ↑
```

Use the shortcode like this:

```go-html-template
{{</* youtube w7Ft2ymGmfc */>}}
```

To have the video embedded in your post:

{{< youtube w7Ft2ymGmfc >}}

As with Vimeo videos you can also set the following parameters `autoplay` and `title`.

```go-html-template
{{</* youtube id="w7Ft2ymGmfc" autoplay="true" title="Example Video Title" */>}}
```