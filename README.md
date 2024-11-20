Here's a simple guide for publishing a new blog post:

# How to Create a New Blog Post

## 1. Create the File
Create a new markdown file in the `content/blog/` directory with the format:
```
content/blog/YYYY-MM-DD-post-title/index.md
```

## 2. Add Frontmatter
At the top of your markdown file, add the following frontmatter:
```yaml
---
title: "Your Post Title"
date: YYYY-MM-DD
description: "A brief description of your post that will appear in previews and meta tags"
tags: ["tag1", "tag2"]
categories: ["category1"]
draft: true  # Set to false when ready to publish
---
```

## 3. Adding Images
1. Put the images in your post directory:
```
content/blog/YYYY-MM-DD-post-title/
├── image1.jpg
├── image2.png
├── diagram.svg
└── index.md
```

2. Reference images in your markdown using either:
   - Standard markdown syntax for regular images (does not work for SVG):
   ```markdown
   ![Image description](image1.jpg)
   ```
   - Hugo figure shortcode for SVG graphics:
   ```markdown
   {{< figure src="diagram.svg" alt="alt text" >}}
   ```

Images are automatically resized to responsive sizes and converted to webp for optimal file sizes, so you can use any format. Avoid using webp, as the reencode will lower quality further and mess with contrast. SVG files are served as-is and maintain their vector quality.

## 4. Writing Content
- Write your content using standard markdown syntax
- Use headings starting with `##` (h2) since the title will be h1
- Code blocks can be added using triple backticks with language identifier:
  ````markdown
  ```python
  def hello_world():
      print("Hello, World!")
  ```
  ````
- For advanced formatting options and additional shortcodes (callouts, cards, tabs, etc.), refer to the [Hextra Documentation](https://imfing.github.io/hextra/docs/guide/)

## 5. Preview & Publish
1. Run the local server to preview:
```bash
hugo server
```
2. Once ready to publish, to draft: false in frontmatter, and commit when ready to publish and push your changes to the repository
3. The github workflow will build and publish the site (if a page with draft: true is committed to the repository, the page will not published)

## Example Post Structure
```
content/blog/2024-03-20-my-new-post/
├── featured.jpg
├── diagram.png
└── index.md
```

```markdown:content/blog/2024-03-20-my-new-post/index.md
---
title: "My New Blog Post"
date: 2024-03-20
description: "A comprehensive guide about something interesting"
tags: ["tutorial", "guide"]
categories: ["tutorials"]
---

## Introduction
Your content starts here...

![Diagram explaining the concept](diagram.png)

## More Content
Continue writing...
```