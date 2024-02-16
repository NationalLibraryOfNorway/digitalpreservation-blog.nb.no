This is the repository for the digital preservation webpage and blog.

---

To preview locally. run `hugo server -D` (builds posts and drafts)
If you just had cloned the repository, you need to run `git submodule update --init --recursive` to get the theme.
If you don't have hugo installed, follow the instructions at [Hugo installation page](https://gohugo.io/installation/ "Page with guides on installing Hugo on MAC, Windows, Linux, and BSD")

See [samplepost](./content/blog/samplepost.md) for all available markdown syntax and explanations for frontmatter.

See [Content Organization](https://gohugo.io/content-management/organization/ "Documentation on how to organize content in Hugo") for a guide on how to organize content in Hugo.

Add new blog posts under content/blog directory. Organize as page bundles if using assets.

```
content
└── blog
    ├── Post1            <-- Page bundle for post 1
    │   ├── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── Post2            <-- Page bundle for post 2
    │   └── index.md     <------ post in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── posttitle.md     <-- post 3 in markdown (w/ no assets) straight under blog directory
    └── _index.md        <-- index/layout definitions for blog overview page (do not edit)
```

Add new documents under content/documents, similarly to blog posts. These posts only show under the documents-tab.

```
content
└── documents
    ├── Document1        <-- Page bundle for document 1
    │   ├── index.md     <------ document 1 in markdown
    │   └── image1.jpeg  <------ asset used in post
    ├── Document2.md     <-- document 2 in markdown (w/ no assets) straight under blog directory
    └── _index.md        <-- index/layout definitions document overview page (do not edit)
```

